from math import dist
from random import (
    randint,
    choice
)

from settings.settings import (
    MonsterSettings as MS,
    GameBoardSize as GBS,
    GameBoardElements as GBE
)
from game_mechanics.movement import Movement


class BaseMonster(Movement):
    """Base monster class"""
    def __init__(self, game_board: list[list[str]]) -> None:
        self.string: str = MS.MONSTER_STR
        self.emoji: str = MS.MONSTER
        self.game_board = game_board
        x, y = self.random_xy()
        self.X = x
        self.Y = y
        self.coord = (self.Y, self.X)

    def random_xy(self) -> tuple[int, int]:
        """ """
        random_coord_valid = False
        while not random_coord_valid:
            x = randint(2, GBS.MAP_WIDTH.value - 2)
            y = randint(2, GBS.MAP_HEIGHT.value - (GBS.MAP_HEIGHT.value // 3))
            if self.game_board[y][x] == GBE.MAP_TILES:
                random_coord_valid = True
                coord = (x, y)

        return coord

    def move_if_smell(self, player_coord: tuple[int, int]) -> None:
        """

        Parameters
        ----------
        player_coord: tuple[int, int] : cooordinate of the player


        Returns None
        -------

        """
        if dist(self.coord, player_coord) < 5:
            direction = choice(list(self.movements.keys()))
            self.move(direction)

    def __str__(self) -> str:
        return self.string
