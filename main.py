from flask import Flask
from routes.route import route_setup


app = Flask(__name__)

route_setup(app)

if __name__ == "__main__":
    app.run(debug = True)
