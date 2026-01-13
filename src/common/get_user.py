from typing import Any

def get_user(user_id: int) -> dict:
    """ユーザー ID でデータベースからユーザー情報を取得する。

    Args:
        user_id (int): ユーザーの一意な識別子。

    Returns:
        dict: 取得したユーザー情報。
    """
    return db.fetch(user_id)
    """Fetch a user by ID from the database.

    Args:
        user_id (int): The unique identifier of the user.

    Returns:
        Any: The user record fetched from the database.
    """
    return db.fetch(user_id)
