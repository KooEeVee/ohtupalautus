from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        if len(username) < 3:
            raise UserInputError("Username must contain at least 3 characters a-z")
        if not re.match("^[a-z]+$", username):
            raise UserInputError("Only use characters a-z in your username")
        if len(password) < 8:
            raise UserInputError("Password must contain at least 8 characters")
        if not re.search("[^a-z]", password):
            raise UserInputError("Password must contain other characters than letters a-z")
        


        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
