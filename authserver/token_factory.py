import jwt
import time
from db.models import User


def create(user: User):
    return jwt.encode(
        {
            "sub": str(user.uid),
            "name": user.username,
            "iat": int(time.time())  # issued at
        },
        'secret',
        algorithm="HS256",
    )
