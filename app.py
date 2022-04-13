from flask import Flask
from flask_restful import Api

from api import include_urls

app = Flask(__name__)
api = Api(app)
include_urls(api)


app.run()
