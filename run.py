from flask import Flask

if __name__ == '__main__':
    app = Flask(__name__, template_folder='authserver/server/templates')
    import authserver.server.routes
    
    app.run(debug=True)
