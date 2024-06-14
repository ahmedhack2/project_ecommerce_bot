from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from resources import ns


app = Flask(__name__)
CORS(app)
api = Api()
api.init_app(app)
api.add_namespace(ns)
if __name__ == "__main__":
    app.run(debug=True)