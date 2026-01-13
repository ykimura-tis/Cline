from typing import Any

def get_user(user_id: int) -> Any:
    """Fetch a user by ID from the database.

    Args:
        user_id (int): The unique identifier of the user.

    Returns:
        Any: The user record fetched from the database.
    """
    return db.fetch(user_id)
