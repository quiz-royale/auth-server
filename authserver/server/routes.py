from __main__ import app

from http import HTTPStatus

from flask import request, render_template, jsonify

from authserver.db.db import DummyDbService
from authserver.db.errors import NoSuchUserException
import token_factory


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
        return e.message, HTTPStatus.NOT_FOUND

    return jsonify({'token': token_factory.create(user)}), HTTPStatus.OK
