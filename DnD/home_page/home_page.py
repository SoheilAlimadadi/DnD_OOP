from typing import Optional
from logging import getLogger
from time  import sleep

from database.database import DataBase
from helper.messages import HomepageMessages as HM
from settings.settings import HomepageButtons as HB
from helper.utils import Utils
from auth.auth import (
    PasswordAuth,
    UsernameAuth
)
from helper.messages import LogMessages as LG

auth_logger = getLogger('auth')


class HomePage:
    '''The homepage of the game'''
    def __init__(self) -> None:
        self.database = DataBase()
        self.texts: list[str] = [HM.LOGIN_TEXT, HM.REGISTER_TEXT, HM.QUIT_TEXT]
        self.buttons: list[str] = [
            HB.LOGIN_BUTTON,
            HB.REGISTER_BUTTON,
            HB.QUIT_BUTTON
        ]


    def make_home_page(self) -> tuple[str, bool]:
        '''Creates the homepage'''
        self.make_initial_database()
        quit_game: bool = False
        home_page: bool = True
        username: Optional[str] = None
        while home_page:
            Utils.clean()
            Utils.print_logo()
            for text in self.texts:
                print(text)
            
            user_input = input().lower().strip()
            Utils.clean()

            if user_input == HB.QUIT_BUTTON:
                quit_game, home_page = True, False
            if user_input == HB.REGISTER_BUTTON:
                self.register_user()
            if user_input == HB.LOGIN_BUTTON:
                username, logged_in = self.login_user()
                if not logged_in: continue
            
                home_page = False

            
        return username, quit_game


    def register_user(self) -> None:
        '''Registers the user'''
        username_valid: bool = False
        while not username_valid:
            Utils.print_logo()
            username = Utils.get_username()
            username_valid = self.validate_username(username)
            if not username_valid:
                print(HM.USER_EXISTS.format(username))
                sleep(2)
            Utils.clean()

        password, repeat_password = False, True
        while not password == repeat_password:
            if password is False:
                Utils.print_logo()
            password = Utils.get_password()
            password_valid = self.validate_password(password)
            if not password_valid:
                continue
            repeat_password = Utils.repeat_password()
            if not password == repeat_password:
                print(HM.PWS_DONT_MATCH)
                sleep(2)

            Utils.clean()

        self.database.register(username, password)


    def login_user(self) -> bool:
        '''Logs in the user'''
        logged_in: bool = False
        while not logged_in:
            Utils.clean()
            Utils.print_logo()
            print(HM.QUIT_LOGIN)
            username = Utils.get_username()
            if username.lower() == HB.LOGIN_BACK:
                break
            if not self.database.is_username_in_database(username):
                print(HM.USERNAME_NOT_FOUND.format(username))
                Utils.wait_clean()
                continue
            password = Utils.get_password()
            if password.lower() == HB.LOGIN_BACK:
                break
            Utils.clean()

            is_valid: bool = self.database.check_username_password(
                username, password
            )
            if is_valid:
                auth_logger.info(LG.LOGGED_IN.format(username))
                logged_in = True
            else:
                Utils.print_logo()
                print(HM.LOGIN_UNSUCCESSFUL)
                sleep(2)

        return username, logged_in


    def make_initial_database(self) -> None:
        '''Makes the initial database'''
        if not self.database.database_exists():
            self.database.create_database()


    def validate_username(self, username: str) -> bool:
        '''Calls for username validation'''
        if self.database.username_unique(username):
            return UsernameAuth.check_user(username)

    
    def validate_password(self, password: str) -> bool:
        '''Calls for password validation'''
        return PasswordAuth.check_pass(password)
