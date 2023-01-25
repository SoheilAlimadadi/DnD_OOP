from .messages import PasswordErrorMessages as pass_esmg
from .messages import UsernameErrorMessages as user_esmg
from .messages import AxisErrorMessages as axis_emsg
from settings.settings import GameMechanicElemenets as GME


class WrongPasswordError(ValueError):
    '''Password is not acceptable'''
    def __str__(self) -> str:
        return pass_esmg.PASSWORD_GENERIC_ERROR


class PasswordLengthError(WrongPasswordError):
    '''Password must be atleast 8 characters'''
    def __str__(self) -> str:
        return pass_esmg.PASSWORD_LENGTH_ERROR


class PasswordLetterError(WrongPasswordError):
    '''Password must have atleast 2 letters'''
    def __str__(self) -> str:
        return pass_esmg.PASSWORD_LETTER_ERROR

class PasswordLowerCaseError(WrongPasswordError):
    '''Password must have atleast 1 lowercase letter'''
    def __str__(self) -> str:
        return pass_esmg.PASSWORD_LOWER_ERROR


class PasswordUpperCaseError(WrongPasswordError):
    '''Password must have atleast 1 uppercase letter'''
    def __str__(self) -> str:
        return pass_esmg.PASSWORD_UPPER_ERROR


class PasswordSignError(WrongPasswordError):
    '''Password must have atleast 1 sign character'''
    def __str__(self) -> str:
        return pass_esmg.PASSWORD_SIGN_ERROR


class PasswordDigitError(WrongPasswordError):
    '''Password must have atleast 1 digit'''
    def __str__(self) -> str:
        return pass_esmg.PASSWORD_DIGIT_ERROR


class UsernameLengthError(ValueError):
    '''Username must be atleast 4 characters'''
    def __str__(self) -> str:
        return user_esmg.USERNAME_LENGTH_ERROR


class XAxisTypeError(TypeError):
    '''Non-integer value was assinged to X'''
    def __str__(self) -> str:
        return axis_emsg.AXIS_TYPE_ERROR.format(GME.X)


class YAxisTypeError(TypeError):
    '''Non-integer value was assinged to Y'''
    def __str__(self) -> str:
        return axis_emsg.AXIS_TYPE_ERROR.format(GME.Y)


class XAxisNegativeError(ValueError):
    '''Negative value was assigned to X'''
    def __str__(self) -> str:
        return axis_emsg.VALUE_NEGATIVE.format(GME.X)


class YAxisNegativeError(ValueError):
    '''Negative value was assigned to Y'''
    def __str__(self) -> str:
        return axis_emsg.VALUE_NEGATIVE.format(GME.Y)
