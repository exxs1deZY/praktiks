from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///swords.db'
db = SQLAlchemy(app)

class Sword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    damage = db.Column(db.Integer)
    rarity = db.Column(db.String(50))
