from .validators import PasswordValidator
from helper.exceptions import (
    PasswordSignError,
    PasswordDigitError,
    PasswordLetterError,
    PasswordLengthError,
    PasswordUpperCaseError,
    PasswordLowerCaseError
)


class Password:
    """setting the password"""
    def __init__(self, password: str) -> None:
        self.password: str = password

    @property
    def password(self) -> str:
        """get password"""
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        """checks if password is valid,
        if password is not valid, exceptions are raised

        Parameters
        ----------
        value: str : password


        Returns None
        -------

        """
        password_validator = PasswordValidator(value)
        if not password_validator.check_len():
            raise PasswordLengthError
        if not password_validator.check_letters():
            raise PasswordLetterError
        if not password_validator.check_digits():
            raise PasswordDigitError
        if not password_validator.check_signs():
            raise PasswordSignError
        if not password_validator.check_uppercase():
            raise PasswordUpperCaseError
        if not password_validator.check_lowercase():
            raise PasswordLowerCaseError

        self._password = value

    def __str__(self) -> str:
        return self.password
