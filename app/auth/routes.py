from flask_login import login_user, current_user, logout_user
from flask import render_template, redirect, flash
from app.auth import auth
from .forms import LoginForm
import app

@auth.route('/login',
            methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #se selecciona al cliente por usename
        c = app.models.Cliente.query.filter_by(username = form.username.data).first()
        if c is None or not c.check_password(form.password.data):
            flash('Usuario no existente o clave invalida')
            return redirect('/auth/login')
        else:
            login_user(c, remember = True)
            return redirect ('/productos/listar')
    return render_template('login.html',
                            form = form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect('/auth/login')