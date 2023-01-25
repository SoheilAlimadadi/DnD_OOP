import os
import json
from typing import Any
from logging import getLogger

from helper.messages import (
    DatabaseVariables as DV,
    LogMessages as LG
)
from auth.hash import Hash

auth_logger = getLogger('auth')


class DataBase:
    """
    A Database class that contains methods to create and use it
    """
    def __init__(self):
        self.database_name: str = DV.DATABASE_NAME
        self.players: str = DV.PLAYERS
        self.win_ratio: str = DV.WIN_RATIO
        self.password: str = DV.PASSWORD
        self.write: str = DV.WRITE
        self.read: str = DV.READ
        self.salt: str = DV.SALT
        self.games_won: str = DV.GAMES_WON
        self.games_lost: str = DV.GAMES_LOST


    def database_exists(self) -> bool:
        """Checks if database exists in the directory"""
        database_exists: bool = False
        if self.database_name in os.listdir():
            database_exists = True

        return database_exists


    def create_database(self) -> None:
        """Creates the database"""
        data_dict: dict = dict()
        with open(self.database_name, self.write) as database_object:
            data_dict.setdefault(self.players, dict())
            jason_database = json.dumps(data_dict, indent=4)
            database_object.write(jason_database)


    def register(self, username: str, password: str) -> None:
        """Registers the user info to the database"""
        database = self.read_database()
        database[self.players].setdefault(username, dict())
        salt, hashed_password = Hash.password(password)
        database[self.players][username][self.password] = hashed_password
        database[self.players][username][self.salt] = salt
        database[self.players][username][self.games_won] = 0
        database[self.players][username][self.games_lost] = 0
        database[self.players][username][self.win_ratio] = 0

        with open(self.database_name, self.write) as database_object:
            updated_database = json.dumps(database, indent=4)
            database_object.write(updated_database)
            auth_logger.info(LG.REGISTERED.format(username))



    def check_username_password(self, username: str, pw: str) -> bool:
        """Checks whether the username and password from user, match"""
        password_matches: bool = False
        database = self.read_database()
        password = database[self.players][username][self.password]
        salt = database[self.players][username][self.salt]
        _, hashed_pw = Hash.password(pw, salt)
        if hashed_pw == password:
            password_matches = True

        return password_matches


    def username_unique(self, username: str) -> bool:
        """Checks whether username is unique"""
        username_valid: bool = False
        database = self.read_database()

        if username not in database[self.players]:
            username_valid = True

        return username_valid


    def is_username_in_database(self, username: str) -> bool:
        """Checks whether username is in database"""
        username_in_db: bool = False
        database = self.read_database()
        if username in database[self.players]:
            username_in_db = True

        return username_in_db

    
    def read_database(self) -> dict[str, Any]:
        with open(self.database_name, self.read) as database_object:
            database = json.load(database_object)

        return database


    def write_to_database(self, data) -> None:
        """Writes to database"""
        with open(self.database_name, self.write) as file_obj:
            json_data = json.dumps(data, indent=4)
            file_obj.write(json_data)



    def update_database(self, game_result: str, username: str) -> None:
        """Updates the database after user wins or loses"""
        database = self.read_database()
        database[self.players][username][game_result] += 1

        games_won = database[self.players][username][self.games_won]
        games_lost = database[self.players][username][self.games_lost]
        win_ratio = (games_won / (games_won + games_lost)) * 100
        database[self.players][username][self.win_ratio] = win_ratio

        self.write_to_database(database)
