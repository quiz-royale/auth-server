import datetime

import jwt
from flask import Flask, request, render_template, jsonify

from quizroyale.db.db import DummyDbService
from quizroyale.db.errors import NoSuchUserException

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    db = DummyDbService()
    try:
        user = db.get_user_by_credentials(
            request.form['username'],
            request.form['password'],
        )
    except NoSuchUserException as e:
        return e.message, 400

    return jsonify({'token': create_token(user.username, str(user.uid))},), 200


def create_token(username: str, user_id: str):
    return jwt.encode(
        {
            "sub": user_id,
            "name": username,
            "iat": int(datetime.datetime.utcnow().timestamp())  # issued at
        },
        'secret',
        algorithm="HS256",
    )


if __name__ == '__main__':
    app.run(debug=True)
