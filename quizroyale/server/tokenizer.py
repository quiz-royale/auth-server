import datetime
import jwt

from .utils import Secret


def create_token(username: str, user_id: str, secret: Secret):
    return jwt.encode(
        {
            "sub": user_id,
            "name": username,
            "iat": int(datetime.datetime.utcnow().timestamp())  # issued at
        },
        secret.value,
        algorithm="HS256",
    )
