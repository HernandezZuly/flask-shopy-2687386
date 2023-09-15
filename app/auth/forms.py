from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField(label = "Nombre de usuario",
                           validators = [ InputRequired(message = 'El nombre de usuario es obligatorio') ])
    password = PasswordField(label = "Clave",
                           validators = [ InputRequired(message = 'La clave es obligatoria') ])
    submit = SubmitField(label = "Iniciar sesión")