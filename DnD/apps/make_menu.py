from helper.messages import MenuMessages as MM
from settings.settings import MenuButtons as MB
from .leaderboard import Leaderboard
from helper.utils import Utils


class Menu:
    """
    Menu of the game
    Start game, log out and show leaderboard are the options
    """
    def __init__(self) -> None:
        self.game_diffs: list[str] = [
            MB.EASY_DIFF,
            MB.NORMAL_DIFF,
            MB.HARD_DIFF
        ]
        self.messages: list[str] = [
            MM.GAME_DIFFS_TEXT,
            MM.START_GAME_TEXT,
            MM.LEADERBOARD_TEXT,
            MM.LOGOUT_TEXT
        ]

    def make_menu(self, username=None) -> tuple[bool, bool, int]:
        '''Creates the menu

           return tuple[bool, bool]: is user logged-out, start game or not and
            difficulty of the game
        '''
        menu: bool = True
        logout: bool = False
        start_game: bool = False
        game_diff = 0

        while menu:
            Utils.clean()
            Utils.print_logo()
            print(MM.WELCOME_MESSAGE.format(username))
            for message in self.messages:
                print(message)

            user_input = input().lower().strip()
            Utils.clean()

            if user_input == MB.LOGOUT:
                menu, logout = False, True
            if user_input in self.game_diffs:
                game_diff = int(user_input)
                start_game = True
                menu = False
            if user_input == MB.LEADERBOARD:
                leaderboard = Leaderboard()
                leaderboard.show_leaderboard()

        return logout, start_game, game_diff
