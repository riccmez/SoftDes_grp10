from flask import Flask, flash, render_template, redirect, url_for, request, session
from dao.DAOUsuario import DAOUsuario


app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = DAOUsuario()

ruta='/usuario'

@app.route('/')
def inicio():
    return render_template('index.html')

################### Cliente ####################
    
@app.route('/cliente')
def cliente_idx():
    return render_template('cliente/index.html')


@app.route('/cliente/pedidos')
def cliente_pedidos():
    data = db.read_pedidos(None)
    return render_template('cliente/pedidos.html', data = data)


@app.route('/cliente/favoritos')
def cliente_favoritos():
    return render_template('cliente/favoritos.html')

@app.route('/cliente/recarga')
def cliente_recarga():
    return render_template('cliente/recarga.html')


@app.route('/Admin')
def Admin():
    return render_template('Admin.html')

@app.route('/Registro')
def Register():
    return render_template('Registro.html')

@app.route('/register', methods = ['POST', 'GET'])
def registeruser():
    if request.method == 'POST' and request.form['Register']:
        print(request.form)
        if db.insert_reg(request.form):
            flash("Nuevo usuario creado")
        else:
            flash("ERROR, al crear usuario")

        return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/About')
def About():
    return render_template('About.html')

############## Admin #############

@app.route(ruta+'/')
def index():
    data = db.read_reg(None)
    return render_template('usuario/index.html', data = data)

@app.route('/usuario/dashboard')
def dashb():
    return render_template('usuario/Dashboard.html')

@app.route('/usuario/empleados')
def empleados():
    data = db.read(None)
    return render_template('usuario/empleados.html',data=data)


@app.route(ruta+'/add/')
def add():
    return render_template('/usuario/add.html')

@app.route(ruta+'/addusuario', methods = ['POST', 'GET'])
def addusuario():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("Nuevo usuario creado")
        else:
            flash("ERROR, al crear usuario")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route(ruta+'/update/<int:id>/')
def update(id):
    data = db.read_reg(id)
    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('usuario/update.html', data = data)

@app.route(ruta+'/updateusuario', methods = ['POST'])
def updateusuario():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route(ruta+'/delete/<int:id>/')
def delete(id):
    data = db.read_reg(id)
    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('usuario/delete.html', data = data)

@app.route(ruta+'/deleteusuario', methods = ['POST'])
def deleteusuario():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('Usuario eliminado')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

################ Empleados ################

@app.route(ruta+'/update2/<int:id>/')
def update2(id):
    data = db.read(id)
    if len(data) == 0:
        return redirect(url_for('empleados'))
    else:
        session['update'] = id
        return render_template('usuario/update2.html', data = data)

@app.route(ruta+'/updateusuario2', methods = ['POST'])
def updateusuario2():
    if request.method == 'POST' and request.form['update']:

        if db.update2(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('empleados'))
    else:
        return redirect(url_for('empleados'))

@app.route(ruta+'/delete2/<int:id>/')
def delete2(id):
    data = db.read(id)
    if len(data) == 0:
        return redirect(url_for('empleados'))
    else:
        session['delete'] = id
        return render_template('usuario/delete2.html', data = data)

@app.route(ruta+'/deleteusuario2', methods = ['POST'])
def deleteusuario2():
    if request.method == 'POST' and request.form['delete']:

        if db.delete2(session['delete']):
            flash('Usuario eliminado')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('empleados'))
    else:
        return redirect(url_for('empleados'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

############### Vendedor ##############

@app.route('/vender')
def vende():
    return render_template('vender.html')

@app.route('/vendedor/index')
def vendedor():
    return render_template('vendedor/index.html')

@app.route('/vendedor/ventas')
def ventas():
    data = db.read_ventas(None)
    return render_template('vendedor/ventas.html',data=data)

@app.route('/vendedor/productos')
def productos():
    data = db.read_prod(None)
    return render_template('vendedor/productos.html',data=data)

@app.route('/vendedor/add')
def add_prod():
    return render_template('/vendedor/addProduct.html')

@app.route('/vendedor/addprod', methods = ['POST', 'GET'])
def addProd():
    if request.method == 'POST' and request.form['AddProd']:
        if db.insert_prod(request.form):
            flash("Nuevo producto creado")
        else:
            flash("ERROR, al crear producto")

        return redirect(url_for('productos'))
    else:
        return redirect(url_for('productos'))

@app.route('/vendedor/addventa')
def add_venta():
    return render_template('/vendedor/addVenta.html')

@app.route('/vendedor/addVenta', methods = ['POST', 'GET'])
def addVenta():
    print(request.form['AddVentas'])
    if request.method == 'POST' and request.form['AddVentas']:
        if db.insert_Venta(request.form):
            flash("Nueva venta registrada")
        else:
            flash("ERROR, al crear venta")

        return redirect(url_for('ventas'))
    else:
        return redirect(url_for('ventas'))

@app.route('/vendedor/update/<int:id>/')
def updateVenta(id):
    data = db.read_ventas(id)
    if len(data) == 0:
        return redirect(url_for('ventas'))
    else:
        session['update'] = id
        return render_template('vendedor/update.html', data = data)

@app.route('/vendedor/updateventa', methods = ['POST'])
def updateventa():
    if request.method == 'POST' and request.form['update']:

        if db.updateVenta(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('ventas'))
    else:
        return redirect(url_for('ventas'))

@app.route('/vendedor/delete/<int:id>/')
def deleteVentas(id):
    data = db.read_ventas(id)
    if len(data) == 0:
        return redirect(url_for('ventas'))
    else:
        session['delete'] = id
        return render_template('vendedor/delete.html', data = data)

@app.route('/vendedor/delete', methods = ['POST'])
def deleteventa():
    if request.method == 'POST' and request.form['delete']:

        if db.deleteVenta(session['delete']):
            flash('Venta eliminada')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('ventas'))
    else:
        return redirect(url_for('ventas'))      

@app.route('/vendedor/updateProd/<int:id>/')
def updateProd(id):
    data = db.read_prod(id)
    if len(data) == 0:
        return redirect(url_for('productos'))
    else:
        session['update'] = id
        return render_template('vendedor/updateProd.html', data = data)

@app.route('/vendedor/updateprod', methods = ['POST'])
def updateprod():
    if request.method == 'POST' and request.form['update']:

        if db.updateProd(session['update'], request.form):
            flash('Se actualizo correctamente')
        else:
            flash('ERROR en actualizar')

        session.pop('update', None)

        return redirect(url_for('productos'))
    else:
        return redirect(url_for('productos'))

@app.route('/vendedor/deleteProd/<int:id>/')
def deleteProdc(id):
    data = db.read_prod(id)
    if len(data) == 0:
        return redirect(url_for('productos'))
    else:
        session['delete'] = id
        return render_template('vendedor/deleteProd.html', data = data)

@app.route('/vendedor/deleteprod', methods = ['POST'])
def deleteprod():
    if request.method == 'POST' and request.form['delete']:

        if db.deleteProd(session['delete']):
            flash('Producto eliminado')
        else:
            flash('ERROR al eliminar')
        session.pop('delete', None)

        return redirect(url_for('productos'))
    else:
        return redirect(url_for('productos'))      

if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0",debug=True)
