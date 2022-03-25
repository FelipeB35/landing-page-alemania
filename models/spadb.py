from utils.db import db

class Spa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    message = db.Column(db.String(100))
    
    #Permite que cada vez que se ejecute se guarde cada valor de la consulta
    def __init__(self, fullname, email, phone, message):
        self.fullname = fullname
        self.email = email
        self.phone = phone
        self.message = message
        