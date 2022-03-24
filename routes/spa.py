from flask import Blueprint, render_template, request, redirect

#Guardando las rutas en un blueprint
spa = Blueprint('spa', __name__)

@spa.route('/')
def web_page():
    return render_template('spa.html')