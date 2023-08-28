from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class NewProductForm(FlaskForm):
    nombre = StringField("Ingrese el nombre del producto: ")
    precio = IntegerField("Ingrese el precio del producto: ")
    submit = SubmitField("Guardar")
    