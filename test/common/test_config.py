from common.config import load_config, CONFIG


def setup_function():
    CONFIG.clear()  # キャッシュクリア


def test_load_config(mocker):
    mock_s3_client = mocker.Mock()
    mock_body = mocker.Mock()
    mock_body.read.return_value = b"DB_HOST=test-host\nDB_USER=test-user\n"
    mock_s3_client.get_object.return_value = {"Body": mock_body}

    config1 = load_config(mock_s3_client)
    config2 = load_config(mock_s3_client)

    assert config1["DB_HOST"] == "test-host"
    assert config1["DB_USER"] == "test-user"

    assert config1 == config2
    mock_s3_client.get_object.assert_called_once()
