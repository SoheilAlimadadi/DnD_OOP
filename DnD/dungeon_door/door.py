from random import randint

from helper.types import Coordinate
from settings.settings import (
    DungeonDoorSettings as DDS,
    GameBoardSize as GBS,
    GameBoardElements as GBE
)


class Door:
    """
    a class with dungeon door info
    and generates a semi-random location for it
    """

    def __init__(self, game_board: list[list[str]]) -> None:
        self.emoji: str = DDS.EMOJI
        self.string: str = DDS.DOOR_STR
        self.game_board = game_board
        self.coord = self.random_coord()

    def random_coord(self) -> Coordinate:
        """
        Generates a semi-random location for the dungeon door

        returns Coordinate: the dungeon door coord
        """
        coord_valid = False
        while not coord_valid:
            x = randint(1, GBS.MAP_WIDTH.value - 2)
            y = randint(
                1, GBS.MAP_HEIGHT.value - (GBS.MAP_HEIGHT.value // 3 + 2)
            )
            if self.game_board[y][x] == GBE.MAP_TILES:
                coord = (y, x)
                coord_valid = True

        return coord

    def __str__(self) -> str:
        return self.string
