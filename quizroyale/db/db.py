import abc

from quizroyale.server.utils import Secret
from quizroyale.server.tokenizer import create_token
from quizroyale.db import models
from quizroyale.db.errors import NoSuchUserException


class DbService(abc.ABC):
    @abc.abstractmethod
    def get_users(self) -> list[models.User]:
        ...

    @abc.abstractmethod
    def get_user_by_credentials(
            self,
            username: str,
            password: str,
    ) -> models.User:
        ...


class DummyDbService(DbService):
    _USERS = [
        models.User(uid=1,
                    username="Noob",
                    password="12345",
                    refresh_token=create_token("Noob", "12345",
                                               Secret.ACCESS_TOKEN_SECRET)),
    ]

    def get_users(self) -> list[models.User]:
        return self._USERS

    def get_user_by_credentials(self,
                                username: str,
                                password: str,
                                ) -> models.User:
        for user in self.get_users():
            if user.username == username and user.password == password:
                return user
        raise NoSuchUserException
