from math import dist

from helper.utils import Utils

from helper.messages import GameResultMessages as GRM
from settings.settings import GameState as GS


class Game:
    """
    Mechanics of the game are implemented here
    """
    def __init__(self, game_board: list[list[str]]):
        self.game_board: list[list[str]] = game_board


    def update_game_state(
        self,
        player_coord: tuple[int, int],
        door_coord: tuple[int, int],
        monster_coord: tuple[int, int],
        hp: list
    ) -> str:
        '''Checks whether the game is on going, won or loss on each loop'''
        game_state: str = GS.ON_GOING
        if dist(player_coord, monster_coord) <= 1:
            hp.pop()
        if player_coord == monster_coord or not hp:
            game_state: str = GS.LOSE
        if player_coord == door_coord:
            game_state: str = GS.WIN

        return game_state


    def result(self, game_state: str) -> str:
        '''Prints the result of the game and returns the game state'''
        back_to_menu: bool = False
        while not back_to_menu:
            Utils.clean()
            if game_state is GS.LOSE:
                print(GRM.LOSE)
            else:
                print(GRM.WIN)

            user_input: str = input(GRM.AFTER_GAME)
            if not user_input:
                back_to_menu = True
        Utils.clean()

        return game_state
