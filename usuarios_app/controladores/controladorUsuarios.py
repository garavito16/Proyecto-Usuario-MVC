

from flask import Flask, render_template, request, redirect, session, flash
from usuarios_app import app #busca por defecto en el archivo __init__
from usuarios_app.modelos.modelo_usuarios import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app) #enviar el flask completo

listaUsuarios = []

#Rutas
@app.route('/',methods=['GET'])
def despliegaRegistroLogin():
    return render_template("index.html")

@app.route('/dashboard',methods=['GET'])
def despliegaDashboard():
    if 'nombre' in session:
        listaUsuarios = Usuario.obtenerListarUsusarios()
        return render_template("dashboard.html",usuarios=listaUsuarios)
    else:
        return redirect('/')

@app.route('/registrarUsuario',methods=['POST'])
def registrarUsuario():
    #el modulo request se usa para traer informacion de la pagina
    print(request.form)
    passwordencriptado = bcrypt.generate_password_hash(request.form["password"])
    nuevoUsuario = {
        "nombre" : request.form["nombre"],
        "apellido" : request.form["apellido"],
        "nombreUsuario" : request.form["usuario"],
        "password" : passwordencriptado,
        "id_departamento" : request.form["departamento"]
    }
    session["nombre"] = request.form["nombre"]
    session["apellido"] = request.form["apellido"]
    
    resultado = Usuario.agregaUsuario(nuevoUsuario)
    # if(resultado == False):
    if type(resultado) is int and resultado == 0:
        print("resultado",resultado)
        return redirect('/dashboard')
    else:
        flash("hubo un problema en el registro, intenta con otro nobre de usuario","registro")
        return redirect('/')


@app.route('/login',methods=['POST'])
def loginUsuario():
    nombreUsuario = request.form["loginUsuario"]
    passwordUsuario = request.form["passwordUsuario"]

    # print(request.form)
    usuario = {
        "nombreUsuario" : nombreUsuario
        # "password" : passwordUsuario
    }

    resultado = Usuario.verificaUsuario(usuario)

    print(resultado)
    # tupla vacia si no lo encuentra
    # diccionario con los datos que coinciden

    if (resultado == None):
        flash("El nombre de usuario no es el correcto","login")
        flash("Por favor verifica tu usuario y password","login")
        return redirect("/")
    else:
        if not (bcrypt.check_password_hash(resultado.password[0],passwordUsuario)):
            flash("El password es incorrecto","login")
            return redirect("/")
        else:
            session["nombre"] = resultado.nombre
            session["apellido"] = resultado.apellido
            return redirect("/dashboard")
    

@app.route('/usuario/remover/<idUsuario>',methods=["POST"])
def removerUsuario(idUsuario):
    print(idUsuario)
    usuario = {
        "nombreUsuario" : idUsuario
    }
    resultado = Usuario.eliminarUsuarios(usuario)
    #si resultado es False entonces no se pudo realizar el Delete
    print(resultado)
    return redirect('/dashboard')

@app.route('/usuario/editar/<idUsuario>',methods=["GET"])
def despliegaEditar(idUsuario):
    usuario = {
        "nombreUsuario" : idUsuario
    }
    resultado = Usuario.obtenerDatosUsuario(usuario)
    print(resultado[0])
    return render_template("editarUsuario.html",usuario=resultado[0])

@app.route('/usuario/editar/<idUsuario>',methods=["POST"])
def editarUsuario(idUsuario):
    editarUsuario = {
        "nombre" : request.form["nombre"],
        "apellido" : request.form["apellido"],
        "nombreUsuario" : idUsuario,
        "password" : request.form["password"],
        "id_departamento" : request.form["departamento"]
    }
    resultado = Usuario.editarUsuario(editarUsuario);
    print(resultado)
    return redirect('/dashboard')

@app.route('/logout',methods=["GET"])
def logoutUsuario():
    session.clear()
    return redirect('/')


