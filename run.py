from flask import Flask

if __name__ == '__main__':
    app = Flask(__name__, template_folder='authserver/server/templates')
    import authserver.server.routes # noqa
    app.run(debug=True)
