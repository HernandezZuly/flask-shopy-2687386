from flask import render_template, redirect, flash
from flask_login import login_required
from app.clientes import clientes
import app
from .forms import NewClientForm, EditClientForm

@clientes.route('/createCli', methods = ['GET', 'POST'])
@login_required
def crear():
    p = app.models.Cliente()
    form = NewClientForm()
    if form.validate_on_submit():
        form.populate_obj(p),
        app.db.session.add(p),
        app.db.session.commit()
        flash("Cliente registrado correctamente")
        return redirect('/clientes/listarCli')
    return render_template('newCli.html',
                            form = form)

@clientes.route('/listarCli')
@login_required
def listar():
    clientes = app.models.Cliente.query.all()
    return render_template("listarCli.html",
                            clientes = clientes)

@clientes.route('/editarCli/<cliente_id>', methods = ['GET', 'POST'])
@login_required
def editar(cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    form = EditClientForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('Cliente actualizado')
        return redirect('/clientes/listarCli')
    return render_template("newCli.html",
                            form = form)

@clientes.route('/eliminarCli/<cliente_id>')
@login_required
def eliminar(cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('Cliente eliminado')
    return redirect('/clientes/listarCli')