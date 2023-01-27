from string import (
    ascii_letters,
    digits,
    punctuation,
    ascii_lowercase,
    ascii_uppercase
)


class PasswordValidator:
    """
    Contains methods to check is password is valid or not.
    """
    def __init__(self, password: str) -> None:
        self.password: str = password

    def check_len(self) -> bool:
        """Checks if the length of the password is more than 8"""
        password_is_valid: bool = True
        if len(self.password) < 8:
            password_is_valid = False

        return password_is_valid

    def check_letters(self) -> bool:
        """Checks if the password contains the alphabet letters"""
        password_is_valid: bool = True
        if not any(map(lambda x: x in ascii_letters, self.password)):
            password_is_valid = False

        return password_is_valid

    def check_digits(self) -> bool:
        """Checks if the password contains the digits"""
        password_is_valid: bool = True
        if not any(map(lambda x: x in digits, self.password)):
            password_is_valid = False

        return password_is_valid

    def check_signs(self) -> bool:
        """Checks if the password contains the signs"""
        password_is_valid: bool = True
        if not any(map(lambda x: x in punctuation, self.password)):
            password_is_valid = False

        return password_is_valid

    def check_uppercase(self) -> bool:
        """Checks if the password contains the uppercase characters"""
        password_is_valid: bool = True
        if not any(map(lambda x: x in ascii_uppercase, self.password)):
            password_is_valid = False

        return password_is_valid

    def check_lowercase(self) -> bool:
        """Checks if the password contains the lowercase characters"""
        password_is_valid: bool = True
        if not any(map(lambda x: x in ascii_lowercase, self.password)):
            password_is_valid = False

        return password_is_valid


class UsernameValidator:
    """
    Contains methods to check is username is valid or not.
    """
    def __init__(self, username: str) -> None:
        self.username: str = username

    def check_username_len(self) -> bool:
        """Checks if the length of the username is more than 3"""
        username_valid: bool = False

        if len(self.username) >= 4:
            username_valid = True

        return username_valid
