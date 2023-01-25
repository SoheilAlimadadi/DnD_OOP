from logging import getLogger
from .password import Password
from .username import Username
from helper.messages import LogMessages as LG
from helper.exceptions import (
    PasswordSignError,
    PasswordDigitError,
    UsernameLengthError,
    PasswordLetterError,
    PasswordLengthError,
    PasswordUpperCaseError,
    PasswordLowerCaseError,
)

auth_logger = getLogger('auth')


class PasswordAuth:
    '''
    Password validation
    '''
    
    @staticmethod
    def check_pass(password: str) -> bool:
        '''
        Check password validation
        '''
        password_valid: bool = False
        try:
            Password(password)
        except PasswordLengthError as e:
            auth_logger.info(e)
            print(e)
        except PasswordLetterError as e:
            auth_logger.info(e)
            print(e)
        except PasswordDigitError as e:
            auth_logger.info(e)
            print(e)
        except PasswordSignError as e:
            auth_logger.info(e)
            print(e)
        except PasswordLowerCaseError as e:
            auth_logger.info(e)
            print(e)
        except PasswordUpperCaseError as e:
            auth_logger.info(e)
            print(e)
        else:
            password_valid = True

        return password_valid


class UsernameAuth:
    '''
    Username validation
    '''

    @staticmethod
    def check_user(username: str) -> bool:
        '''
        Check password validation
        '''

        username_valid: bool = False
        try:
            Username(username)
        except UsernameLengthError as e:
            auth_logger.info(LG.FAILED_USERNAME_REGISTER.format(username))
            print(e)
        else:
            auth_logger.info(LG.USERNAME_REGISTER.format(username))
            username_valid = True

        return username_valid