
from usuarios_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from usuarios_app.modelos.modelo_usuarios import Usuario

class departamento:
    def __init__(self,id, nombre):
        self.id = id
        self.nombre = nombre
        self.usuarios = []
    
    def agregarUsuario(self,usuario):
        self.usuarios.append(usuario)

    @classmethod
    def obtenerListaDepartamentos(cls):
        query = "SELECT * FROM departamentos"
        resultado = connectToMySQL("usuarios_db").query_db(query)
        listaDepartamentos = []
        for departamento in resultado:
            listaDepartamentos.append(cls(departamento["id"],departamento["nombre"]))
        return listaDepartamentos

    @classmethod
    def obtenerListaDepartamentosConUsuarios(cls):
        # query = "SELECT * FROM departamentos d, usuarios u WHERE d.id = u.id_departamento;"
        query = "SELECT * FROM departamentos d LEFT JOIN usuarios u ON d.id = u.id_departamento;"
        resultado = connectToMySQL("usuarios_db").query_db(query)
        listaDepartamentosConUsuario = []
        

        for renglon in resultado:
            indice = existeDepartamentoEnArreglo(renglon["id"],listaDepartamentosConUsuario)
            if(indice == -1):
                departamentoAgregar = departamento(renglon["id"],renglon["nombre"])
                departamentoAgregar.agregarUsuario(Usuario(renglon["u.nombre"],renglon["apellido"],renglon["nombreUsuario"],renglon["password"],renglon["id"]))
                listaDepartamentosConUsuario.append(departamentoAgregar)
            else:
                listaDepartamentosConUsuario[indice].agregarUsuario(Usuario(renglon["u.nombre"],renglon["apellido"],renglon["nombreUsuario"],renglon["password"],renglon["id"]))
        return listaDepartamentosConUsuario

def existeDepartamentoEnArreglo(nombre, listaDepartamentos):
    for i in range(0,len(listaDepartamentos)):
        if listaDepartamentos[i].id == nombre:
            return i
    return -1