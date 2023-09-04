from flask import render_template
from app.productos import productos
import app
import os
from .forms import NewProductForm

@productos.route('/create', methods = ['GET', 'POST'])
def crear():
    p = app.models.Producto()
    form = NewProductForm()
    if form.validate_on_submit():
        form.populate_obj(p),
        p.imagen = form.imagen.data.filename
        app.db.session.add(p),
        app.db.session.commit()
        #campo de imagen (filestorage)
        archivo = form.imagen.data
        archivo.save(os.path.abspath(os.getcwd() + "/app/productos/imagenes/" + p.imagen))
        return 'Producto registrado'
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