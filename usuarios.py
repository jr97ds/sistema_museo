from abc import ABC


class UsuarioRegistrado(ABC):
    def __init__(self, nombre, apellido, usuario, contraseña):
        self._nombre = nombre
        self._apellido = apellido
        self._usuario = usuario
        self._contraseña = contraseña

    @property
    def usuario(self):
        return self._usuario
    @property
    def contraseña(self):
        return self._contraseña
    @property
    def nombre_completo(self):
        return f"{self._nombre} {self._apellido}"
    

class Empleado(UsuarioRegistrado):
    def __init__(self, nombre : str, apellido : str, 
                 usuario : str, contraseña : str):
        super().__init__(nombre, apellido, usuario, contraseña)
        self._cargo = None

    @property
    def cargo(self):
        return self._cargo
    

class EncargadoCatalogo(Empleado):
    def __init__(self, nombre : str, apellido : str, 
                 usuario : str, contraseña : str):
        super().__init__(nombre, apellido, usuario, contraseña)
        self._cargo = "Encargado del Catálogo"


class RestauradorJefe(Empleado):
    def __init__(self, nombre : str, apellido : str, 
                 usuario : str, contraseña : str):
        super().__init__(nombre, apellido, usuario, contraseña)
        self._cargo = "Restaurador Jefe"

class DirectorMuseo(Empleado):
    def __init__(self, nombre : str, apellido : str, 
                 usuario : str, contraseña : str):
        super().__init__(nombre, apellido, usuario, contraseña)
        self._cargo = "Director del Museo"

class Autenticacion:
    def __init__(self, usuario, contraseña):
        self._usuario = usuario
        self._contraseña = contraseña



