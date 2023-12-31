#Importaciones
from flask import Flask, render_template
from .config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .mi_blueprint import mi_blueprint
from app.productos import productos
from app.clientes import clientes
from flask_bootstrap import Bootstrap

# Inicializar el objeto flask
app = Flask (__name__)
app.config.from_object(Config)

#Objeto del bootstrap
bootstrap = Bootstrap(app)

# Inicializar el objeto SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app , db)

#Registrar modulos (blueprints)
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)
app.register_blueprint(clientes)

#Se importan las clases del archivo models
from .models import Cliente, Producto, Venta, Detalle

#Creación de ruta
@app.route('/prueba')
def prueba():
    return render_template("base.html")