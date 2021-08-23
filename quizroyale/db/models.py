from dataclasses import dataclass


@dataclass
class User:
    uid: int
    username: str
    password: str
    refresh_token: str
