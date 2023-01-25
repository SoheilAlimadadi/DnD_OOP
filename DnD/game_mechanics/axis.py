from logging import getLogger

from helper.exceptions import (
    XAxisTypeError,
    YAxisTypeError,
    XAxisNegativeError,
    YAxisNegativeError
)

game_logger = getLogger('game')


class XYValidator:
    '''
    Validates the X and Y axis
    '''
    def is_x_int(x: int, _) -> bool:
        '''Raises XAxisTypeError if x is not int'''
        if not isinstance(x, int):
            raise XAxisTypeError


    def is_x_positive(x: int) -> bool:
        '''Raises XAxisNegativeError if x is a negative number'''
        if not x >= 0:
            raise XAxisNegativeError


    def is_y_int(y: int, _) -> bool:
        '''Raises YAxisTypeError if x is not int'''
        if not isinstance(y, int):
            raise YAxisTypeError


    def is_y_positive(y: int) -> bool:
        '''Raises YAxisNegativeError if y is a negative number'''
        if not y >= 0:
            raise YAxisNegativeError


class Axis(XYValidator):
    '''
    Validates and sets the Axis
    '''
    def __init__(self, coord: tuple[int, int]) -> None:
        x, y  = coord
        self.X = x
        self.Y = y
        self.coord = (self.Y, self.X)

    @property
    def X(self) -> int:
        return self._X


    @X.setter
    def X(self, value: int) -> None:
        try:
            self.is_x_int(value)
            self.is_x_positive(value)
        except XAxisTypeError as e:
            game_logger.info(e)
        except XAxisNegativeError as e:
            game_logger.info(e)

        self._X = value


    @property
    def Y(self) -> int:
        return self._Y

    
    @Y.setter
    def Y(self, value: int) -> None:
        try:
            self.is_y_int(value)
            self.is_y_positive(value)
        except YAxisTypeError as e:
            game_logger.info(e)
        except YAxisNegativeError as e:
            game_logger.info(e)

        self._Y = value
