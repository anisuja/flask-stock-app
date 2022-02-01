from flask import Flask, escape, render_template, request, session, redirect, url_for, flash
import secrets
import logging


app  = Flask(__name__)
app.secret_key = '\xfc)\x1bx\x9b\xf5\xc3\xed\x90}\x1d\xe6\xb8\x1e\xed#<\xfd5S\x0bsC\x93+>\x8d@]6V[' 

# Logging Configuration
file_handler = logging.FileHandler('flask-stock-portfolio.log')
app.logger.addHandler(file_handler)

# Log that the Flask application is starting
app.logger.info('Starting the Flask Stock Portfolio App...')

# Import the blueprints
from project.stocks import stocks_blueprint
from project.users import users_blueprint

# Register the blueprints
app.register_blueprint(stocks_blueprint)
app.register_blueprint(users_blueprint, url_prefix='/users')

