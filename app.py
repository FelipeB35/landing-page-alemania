from flask import Flask
from routes.spa import spa
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@localhost:3306/contactsdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


SQLAlchemy(app)


app.register_blueprint(spa)
