from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class ClientForm():
    username = StringField("Ingrese el nombre de usuario: ",
                            validators = [ InputRequired(message = 'Usuario requerido') ])
    password = StringField("Ingrese la contraseña del cliente: ",
                            validators = [ InputRequired(message = 'Contraseña requerida') ])
    email = StringField("Ingrese el correo del cliente: ",
                            validators = [ InputRequired(message = 'Correo requerido') ])
    
class NewClientForm(FlaskForm, ClientForm):
    submit = SubmitField("Guardar")

class EditClientForm(FlaskForm, ClientForm):
    submit = SubmitField("Actualizar")