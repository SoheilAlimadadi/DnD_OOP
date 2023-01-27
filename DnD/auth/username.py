from .validators import UsernameValidator
from helper.exceptions import UsernameLengthError


class Username:
    """setting the username"""
    def __init__(self, username):
        self.username: str = username

    @property
    def username(self) -> str:
        """get username"""
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        """checks if username is valid,
        if username is not valid, exceptions are raised

        Parameters
        ----------
        value: str : username


        Returns None
        -------

        """
        username_validator = UsernameValidator(value)
        if not username_validator.check_username_len():
            raise UsernameLengthError

        self._username = value

    def __str__(self) -> str:
        return self.username
