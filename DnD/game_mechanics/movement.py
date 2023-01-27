from .axis import Axis
from settings.settings import (
    MovementSettings as MS,
    GameBoardElements as GBE
)


class Movement(Axis):
    """Extends the Axis class with movement ability"""

    movements: dict[str, tuple[int, int]] = {
        MS.UP_INPUT.value: MS.UP.value,
        MS.DOWN_INPUT.value: MS.DOWN.value,
        MS.LEFT_INPUT.value: MS.LEFT.value,
        MS.RIGHT_INPUT.value: MS.RIGHT.value
    }

    def __init__(
        self,
        coord: tuple[int, int],
        game_board: list[list[str]]
    ) -> None:
        super().__init__(coord)
        self.game_board = game_board

    def move(self, user_input: str) -> None:
        """

        Parameters
        ----------
        user_input: str : user input


        Returns None
        -------

        """
        x, y = self.coord
        if user_input:
            x_move, y_move = self.movements[user_input]
            new_x = x + y_move
            new_y = y + x_move
            self.coord = (new_x, new_y)

    def check_wall_collision(
        self,
        coord: tuple[int, int],
        gameboard: list[list[str]]
    ) -> bool:
        """Checks whether the object has colided with wall

        Parameters
        ----------
        coord: tuple[int, int]: coordinate of object

        gameboard: list[list[str]] : game board


        Returns bool: True if valid else False
        -------

        """
        valid_pos: bool = False
        if coord:
            x, y = coord
            if not gameboard[x][y] == GBE.MAP_WALLS:
                valid_pos = True

        return valid_pos

    @property
    def coord(self) -> tuple[int, int]:
        return self._coord

    @coord.setter
    def coord(self, value: tuple[int, int]) -> None:
        if self.check_wall_collision(value, self.game_board):
            self._coord = value
