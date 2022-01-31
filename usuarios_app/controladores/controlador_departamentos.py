
from flask import Flask, render_template, request, redirect, session
from usuarios_app import app
from usuarios_app.modelos.modelo_departamentos import departamento

@app.route('/departamentos',methods=['GET'])
def despliegaDepartamentos():
    listaDepartamentos = departamento.obtenerListaDepartamentos()
    listaDepartamentosConUsuarios = departamento.obtenerListaDepartamentosConUsuarios()
    print(listaDepartamentosConUsuarios)
    return render_template("departamentos.html",listaDepartamentos= listaDepartamentos, listaDepartamentosConUsuarios= listaDepartamentosConUsuarios)