from math import dist

from helper.utils import Utils

from helper.messages import GameResultMessages as GRM
from settings.settings import (
    GameState as GS,
)


class Game:
    """Mechanics of the game are implemented here"""
    def __init__(self, game_board: list[list[str]]):
        self.game_board: list[list[str]] = game_board

    def update_game_state(
        self,
        player_coord: tuple[int, int],
        door_coord: tuple[int, int],
        hp: list[str],
        monsters: list,
        shots: list[tuple[int, int]]
    ) -> tuple[str, list[tuple[int, int]]]:
        """Checks whether the game is on going, won or loss on each loop
        if player is next to the dragon, loses on of his/her healths

        Parameters
        ----------
        player_coord: tuple[int, int] : coordinate of player

        door_coord: tuple[int, int] : cooordinate of the door

        hp: list[str] : a list of healths

        monsters: list : a list of monster objects

        shots: list[tuple[int, int] : a list of shot coordinates


        Returns tuple[str, tuple[int, int]]: state of the game and and and
                                            a list of monster objects
        -------

        """
        game_state: str = GS.ON_GOING
        for monster in monsters:
            if dist(player_coord, monster.coord) <= 1:
                hp.pop()
            if player_coord == monster.coord or not hp:
                game_state: str = GS.LOSE
            for shot in shots:
                if shot == monster.coord:
                    monsters.remove(monster)
        if player_coord == door_coord:
            game_state: str = GS.WIN

        return game_state, monsters

    def result(self, game_state: str) -> str:
        """Prints the result of the game and returns the game state

        Parameters
        ----------
        game_state: str : state of the game


        Returns str: state of the game
        -------

        """
        Utils.clean()
        if game_state is GS.LOSE:
            print(GRM.LOSE)
        else:
            print(GRM.WIN)

        return game_state
