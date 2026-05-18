class UserNotFoundError(Exception):
    """User was not found in collection."""
    pass


class DuplicateUserError(Exception):
    """User with this email already exists."""
    pass