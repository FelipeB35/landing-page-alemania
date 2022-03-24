from flask import Flask
from routes.spa import spa

app = Flask(__name__)

app.register_blueprint(spa)
