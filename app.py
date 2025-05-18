from flask import Flask
from routes.routes import register_routes

app = Flask(__name__)
app.config.from_pyfile('config.py')

register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)