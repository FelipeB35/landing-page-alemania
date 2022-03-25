from flask import Blueprint, render_template, request, redirect
from models.spadb import Spa
from utils.db import db


spa = Blueprint('spa', __name__)

@spa.route('/')
def web_page():
    return render_template('spa.html')

@spa.route('/new', methods = ['POST'])
def add_contact():
    #Extrayendo datos del form y guardandolos en una variable
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    
    #Usando la funcion de model para introducir valores en la columna correspondiente
    new_contact = Spa(fullname, email, phone, message)
    
    #Añadiendo los valores a la tabla en la bd
    db.session.add(new_contact)
    db.session.commit()
    
    return redirect('/')
