from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField , FileRequired, FileAllowed

class NewProductForm(FlaskForm):
    nombre = StringField("Ingrese el nombre del producto: ", 
                          validators = [ InputRequired(message = 'Nombre requerido') ])
    precio = IntegerField("Ingrese el precio del producto: ",
                          validators = [ InputRequired(message = 'Precio requerido'),
                                         NumberRange(message = 'Precio fuera de rango',
                                                     min = 10000,
                                                     max = 100000) 
                                        ])
    imagen = FileField(label = "Imagen del producto",
                       validators = [ FileRequired(message = 'Suba una imagen'),
                                      FileAllowed(
                                          ["jpg", "png"],
                                          message = 'Solo se aceptan imagenes'
                                      )])
    submit = SubmitField("Guardar")
    