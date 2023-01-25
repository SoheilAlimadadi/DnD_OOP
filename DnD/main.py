import logging
import logging.config
from sys import exit
from typing import Callable

from home_page.home_page import HomePage
from menu.make_menu import Menu
from game_board.game_board import GameBoard
from game_mechanics.game import Game
from players.base import BasePlayer
from enemies.base import BaseMonster
from dungeon_door.door import Door
from helper.utils import Utils
from database.database import DataBase

from helper.messages import (
    GameMessages as GM,
    LogMessages as LG
)
from settings.settings import (
    ValidGameInputs as VGI,
    GameState as GS
)

logging.config.fileConfig(
    fname='log_config.toml',
    disable_existing_loggers=False
)

root_logger = logging.getLogger('root')
game_logger = logging.getLogger('game')


class DungeonAndDragons:
    '''
    Main class of the game
    '''
    def __init__(self) -> None:
        self.home_page = HomePage()
        self.menu = Menu()
        self.game_board = GameBoard()


    def run_menu(self,username=None) -> Callable:
        '''
        runs the homepage and menu
        '''
        root_logger.info(LG.PROGRAM_RUN)
        start_game: bool = False
        while not start_game:
            if not username:
                username, quit_game = self.home_page.make_home_page()
                if quit_game:
                    root_logger.info(LG.PROGRAM_EXITED)
                    exit()
            root_logger.info(LG.LOGGED_IN.format(username))
            logged_out, start_game = self.menu.make_menu(username)
            if logged_out:
                root_logger.info(LG.LOGGED_OUT.format(username))
                username = None
                continue
        
        root_logger.info(LG.STARTED_GAME.format(username))

        return self.run_game(username)


    def run_game(self, username: str) -> Callable:
        '''
        setting up the objects needed in the game
        running the main loop of the game
        '''
        database = DataBase()
        game_board = self.game_board.make_board()
        game = Game(game_board)
        player = BasePlayer(game_board)
        door = Door(game_board)
        monster = BaseMonster(game_board)
        board_elements = [player, door, monster]
        valid_inputs: list[str] = [value for value in VGI.__members__.values()]
        game_end, result = False, None

        while not game_end:
            for element in board_elements:
                GameBoard.place_on_board(
                    game_board, element.coord, element.emoji
                )
            GameBoard.draw_game_board(game_board)
            self.print_info(valid_inputs, player.health)
            user_input = input(GM.MOVE)
            Utils.clean()
            
            if not user_input in valid_inputs:
                continue
            if user_input == VGI.BACK:
                game_logger.info(LG.EXIT_GAME.format(username))
                break
            for element in board_elements: 
                GameBoard.delete(game_board, element.coord)
            player.move(user_input)

            game_state = game.update_game_state(
                player.coord,
                door.coord,
                monster.coord,
                player.health
            )
            if game_state is not GS.ON_GOING:
                result = game.result(game_state)
                game_logger.info(LG.RESULT.format(username, result))
                game_end = True
        if result:
            database.update_database(result, username)

        return self.run_menu(username)


    def print_info(self, valid_inputs: list[str], hp: list[str]) -> None:
        '''Prints info while the game is running'''
        print(GM.HEALTH.format(" ".join(hp)))
        print(GM.MOVEMENTS.format(" ,".join(valid_inputs[:-1])))
        print(GM.BACK.format(VGI.BACK))


if __name__ == "__main__":
    dungeon_and_dragons = DungeonAndDragons()
    dungeon_and_dragons.run_menu()
