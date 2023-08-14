# Importaciones/dependencias del proyecto
from flask import Flask, render_template
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField


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
    
class Producto(db.Model):
    __tablename__ = "productos"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(120), unique = True)
    precio = db.Column(db.Numeric(precision = 10, scale = 2))
    imagen = db.Column(db.String(120), unique = True)
      
class Venta(db.Model):
    __tablename__ = "ventas"
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime, default = datetime.utcnow)
#                PARA SABER QUE ES UNA LLAVE FORANEA('nOMBRETABLA.CAMPO')
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))

class Detalle(db.Model):
    __tablename__ = "detalles"
    id = db.Column(db.Integer, primary_key = True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    venta_id = db.Column(db.Integer, db.ForeignKey('ventas.id'))
    cantidad = db.Column(db.Integer)


#CREACIÓN DE FORMULARIO PARA EL REGISTRO DE UN CLIENTE 
class RegistroClienteForm(FlaskForm):
    username = StringField("Nombre de Usuario")
    password = PasswordField("Password de Usuario")
    email = StringField("Email")
    submit = SubmitField("Registrar Cliente")


#RUTAS
#para agregar
@app.route('/clientes/create' , methods = ['GET' , 'POST'])
def crear_cliente():
    #Instanciar formulario 
    form = RegistroClienteForm()
    #Validación si el formulario se mostro desde el navegador o cuando se dio click en registrar
    if form.validate_on_submit():
        #Crear el nuevo cliente
        c = Cliente(username = form.username.data, email = form.email.data, password = form.password.data)
        db.session.add(c)
        db.session.commit()
        return "Cliente Registrado"
    return render_template('registro.html', form = form)

#para consultar o mostrar
@app.route('/clientes' , methods = ['GET'])
def listar():
    #seleccionar todos los clientes 
    clientes = Cliente.query.all()
    return render_template('listar.html', clientes = clientes) 

