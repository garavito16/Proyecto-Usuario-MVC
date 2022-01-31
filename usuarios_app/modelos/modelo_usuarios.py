from usuarios_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Usuario:
    def __init__(self, nombre, apellido, nombreUsuario, password,id_departamento):
        self.nombre = nombre
        self.apellido = apellido
        self.nombreUsuario = nombreUsuario
        self.password = password,
        self.id_departamento = id_departamento

    @classmethod
    def agregaUsuario(cls,nuevoUsuario):
        query = "INSERT INTO usuarios(nombre, apellido, nombreUsuario, password,id_departamento) VALUES (%(nombre)s, %(apellido)s, %(nombreUsuario)s, %(password)s, %(id_departamento)s)"
        resultado = connectToMySQL("usuarios_db").query_db(query,nuevoUsuario) #nombre de la base de datos
        return resultado

    @classmethod
    def verificaUsuario(cls,usuario):
        query = "SELECT * FROM usuarios WHERE nombreUsuario = %(nombreUsuario)s;"
        resultado = connectToMySQL("usuarios_db").query_db(query,usuario) #nombre de la base de datos
        if len(resultado) > 0:
            usuarioResultado = Usuario(resultado[0]["nombre"],
            resultado[0]["apellido"],
            resultado[0]["nombreUsuario"],
            resultado[0]["password"],
            resultado[0]["id_departamento"])
            return usuarioResultado
        # usuarioResultado = Usuario()
        else:
            return None
    
    @classmethod
    def obtenerListarUsusarios(self):
        query = "SELECT * FROM usuarios;"
        resultado = connectToMySQL("usuarios_db").query_db(query)
        listaUsuarios = []
        for ususario in resultado:
            usuarioResultado = Usuario(ususario["nombre"],
            ususario["apellido"],
            ususario["nombreUsuario"],
            ususario["password"],
            ususario["id_departamento"])
            listaUsuarios.append(usuarioResultado)
        return listaUsuarios

    @classmethod
    def eliminarUsuarios(self,usuario):
        query = "DELETE FROM usuarios WHERE nombreUsuario = %(nombreUsuario)s;"
        resultado = connectToMySQL("usuarios_db").query_db(query,usuario)
        return resultado

    @classmethod
    def obtenerDatosUsuario(self,usuario):
        query = "SELECT * FROM usuarios WHERE nombreUsuario = %(nombreUsuario)s;"
        resultado = connectToMySQL("usuarios_db").query_db(query,usuario)
        return resultado

    @classmethod
    def editarUsuario(self,usuarioEditar):
        query = "UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, password= %(password)s, id_departamento = %(id_departamento)s WHERE nombreUsuario = %(nombreUsuario)s;"
        resultado = connectToMySQL("usuarios_db").query_db(query,usuarioEditar)
        return resultado