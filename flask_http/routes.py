from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/submit', method=['GET', 'POST'])
def submit():
    name = request.form['name']
    return f'Hi, {name}! Thanks for submitting form'