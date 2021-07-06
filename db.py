import abc
import models


class DbService(abc.ABC):
    @abc.abstractmethod
    def get_users(self) -> list[models.User]:
        ...


class DummyDbService(DbService):
    _USERS = [
        models.User(uid=1, username='Noob', password='12345'),
    ]

    def get_users(self) -> list[models.User]:
        return self._USERS
