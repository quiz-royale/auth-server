import datetime

import jwt
from flask import Flask, request, render_template, jsonify

from .utils import Secret
from .tokenizer import create_token
from quizroyale.db.db import DummyDbService
from quizroyale.db.errors import NoSuchUserException

app = Flask(__name__)

db = DummyDbService()


@app.route("/")
def hello_world():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    try:
        user = db.get_user_by_credentials(
            request.form['username'],
            request.form['password'],
        )
    except NoSuchUserException as e:
        return e.message, 400

    return jsonify(
        {'token': create_token(user.username, str(user.uid),
                               Secret.ACCESS_TOKEN_SECRET)}, ), 200


@app.route('/renew_token', methods=['POST'])
def validate_refresh_token():
    # Do we need to check if user exist?
    user = db.get_user_by_credentials(
        request.form['username'],
        request.form['password'],
    )
    # Don't know how to store it in cookie at the moment
    if user.refresh_token == request.form['refresh_token']:
        decoded_request_token = jwt.decode(
            request.form['refresh_token'],
            Secret.REFRESH_TOKEN_SECRET,
            "HS256",
        )
        if decoded_request_token['iat'] + datetime.timedelta(days=1) < int(
                datetime.datetime.utcnow().timestamp()):
            new_access_token = create_token(user.username, str(user.uid),
                                            Secret.ACCESS_TOKEN_SECRET)
            return new_access_token  # somehow add it to cookie


if __name__ == '__main__':
    app.run(debug=True)
