import logging
import logging.config
from sys import exit
from typing import Callable

from apps.home_page import HomePage
from apps.make_menu import Menu
from game_board.game_board import GameBoard
from game_mechanics.game import Game
from players.player import Player
from enemies.dragon import Dragon
from dungeon_door.door import Door
from helper.utils import Utils
from database.database import DataBase

from helper.messages import (
    GameMessages as GM,
    LogMessages as LG,
    GameResultMessages as GRM
)
from settings.settings import (
    ValidGameInputs as VGI,
    GameState as GS,
    PlayerSettings as PS,
    ShootValidInputs as SVI
)

logging.config.fileConfig(
    fname='log_config.toml',
    disable_existing_loggers=False
)

root_logger = logging.getLogger('root')
game_logger = logging.getLogger('game')


class DungeonAndDragons:
    """Main class of the game, which is responsible for running the game"""
    def __init__(self) -> None:
        self.home_page = HomePage()
        self.menu = Menu()
        self.game_board = GameBoard()


    def run_pregame(self, username: str=None) -> Callable:
        """runs the homepage and menu

        Parameters
        ----------
        username str: username
             (Default value = None)

        Returns Callable: run_game method is called after this method
        -------

        """
        root_logger.info(LG.PROGRAM_RUN)
        start_game: bool = False
        while not start_game:
            if not username:
                username, quit_game = self.home_page.make_home_page()
                if quit_game:
                    root_logger.info(LG.PROGRAM_EXITED)
                    exit()
            root_logger.info(LG.LOGGED_IN.format(username))
            logged_out, start_game, diff = self.menu.make_menu(username)
            if logged_out:
                root_logger.info(LG.LOGGED_OUT.format(username))
                username = None
                continue
        
        root_logger.info(LG.STARTED_GAME.format(username))

        return self.run_game(username, diff)


    def run_game(self, username: str, diff: int) -> Callable:
        """setting up the objects needed in the game
        running the main loop of the game

        Parameters
        ----------
        username: str : username
            
        diff: int : game difficulty
            

        Returns Callable: run_pregame method is called after run_game
        -------

        """
        database = DataBase()
        game_board = self.game_board.make_board()
        game = Game(game_board)
        player = Player(game_board)
        door = Door(game_board)
        monsters = [Dragon(game_board) for _ in range(diff)]
        valid_inputs: list[str] = [value for value in VGI.__members__.values()]
        valid_shot_inputs: list[str] = [
            value for value in SVI.__members__.values()
        ]
        all_valid_inputs = valid_shot_inputs + valid_inputs
        game_end, result= False, None

        while not game_end:
            shots = list()
            board_elements = [player, door, *monsters]
            for element in board_elements:
                GameBoard.place_on_board(
                    game_board, element.coord, element.emoji
                )
            GameBoard.draw_game_board(game_board)
            self.print_info(valid_shot_inputs, valid_inputs, player.health)
            user_input = input(GM.MOVE)
            Utils.clean()

            if user_input not in all_valid_inputs:
                continue
            if user_input == VGI.BACK:
                game_logger.info(LG.EXIT_GAME.format(username))
                break

            for element in board_elements:
                GameBoard.delete(game_board, element.coord)

            if user_input in valid_shot_inputs:
                shots = player.shoot(user_input)
                for shot in shots:
                    GameBoard.place_on_board(game_board ,shot, PS.SHOTS)
            else:
                player.move(user_input)

            for monster in monsters:
                monster.move_if_smell(player.coord)

            game_state, monsters = game.update_game_state(
                player.coord,
                door.coord,
                player.health,
                monsters,
                shots
            )
            if game_state is not GS.ON_GOING:
                result = game.result(game_state)
                game_logger.info(LG.RESULT.format(username, result))
                user_input: str = input(GRM.AFTER_GAME)
                Utils.clean()
                game_end = True

        if result:
            database.update_database(result, username)

        return self.run_pregame(username)


    def print_info(
        self,
        valid_shoot_inputs: list[str],
        valid_inputs: list[str],
        hp: list[str]
    ) -> None:
        """Prints info while the game is running

        Parameters
        ----------
        valid_shoot_inputs: list[str] : valid inputs for shooting
            
        valid_inputs: list[str] : valid inputs for movements
            
        hp: list[str] : a list of healths
            

        Returns None
        -------

        """
        print(GM.HEALTH.format(" ".join(hp)))
        print(GM.MOVEMENTS.format(" ,".join(valid_inputs[:-1])))
        print(GM.SHOOT.format(" ,".join(valid_shoot_inputs)))
        print(GM.BACK.format(VGI.BACK))

        
if __name__ == "__main__":
    dungeon_and_dragons = DungeonAndDragons()
    dungeon_and_dragons.run_pregame()
