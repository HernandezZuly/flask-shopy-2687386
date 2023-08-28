from flask import render_template
from app.productos import productos
from .forms import NewProductForm

@productos.route('/create')
def crear():
    form = NewProductForm()
    return render_template('new.html',
                            form = form)

@productos.route('/listar')
def listar():
    return 'Aqui vamos a listar productos'

@productos.route('/update')
def actualizar():
    return 'Aqui vamos a actualizar productos'

@productos.route('/delete')
def eliminar():
    return 'Aqui vamos a eliminar productos'