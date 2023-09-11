from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import InputRequired, Email

class ClientForm():
    username = StringField("Ingrese el nombre de usuario: ",
                            validators = [ InputRequired(message = 'Usuario requerido') ])
    password = StringField("Ingrese la contraseña del cliente: ",
                            validators = [ InputRequired(message = 'Contraseña requerida') ])
    email = EmailField("Ingrese el correo del cliente: ",
                            validators = [ InputRequired(message = 'Correo requerido'), Email('El correo esta mal recuerde que se necesita un "@" y un "."')])
    
class NewClientForm(FlaskForm, ClientForm):
    submit = SubmitField("Guardar")

class EditClientForm(FlaskForm, ClientForm):
    submit = SubmitField("Actualizar")