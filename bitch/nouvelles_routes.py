from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///collections.db'
db = SQLAlchemy(app)

# Vos autres routes et configurations pour la base de données...
