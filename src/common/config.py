import os
import time
from botocore.client import BaseClient

CONFIG = {}  # グローバルキャッシュ

_loaded_at = 0
TTL = 300  # 秒


def load_config(s3_client: BaseClient):
    global CONFIG, _loaded_at
    if CONFIG and time.time() - _loaded_at < TTL:
        return CONFIG  # すでにロード済み（Warm Start）

    bucket = os.environ["CONFIG_BUCKET"]
    key = os.environ["CONFIG_KEY"]

    response = s3_client.get_object(Bucket=bucket, Key=key)
    body = response["Body"].read().decode("utf-8")

    for line in body.splitlines():
        if not line or line.startswith("#"):
            continue
        k, v = line.split("=", 1)
        CONFIG[k] = v

    _loaded_at = time.time()

    return CONFIG
