# Importaciones/dependencias del proyecto
from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Inicializar el objeto flask 
app = Flask (__name__)
app.config.from_object(Config)

# Inicializar el objeto SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app , db)

#      MODELOS - ENTIDADES
class Cliente(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(100), unique = True)
    
    