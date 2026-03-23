from abc import ABC


class UsuarioRegistrado(ABC):
    def __init__(self, nombre, apellido, usuario, contraseña):
        self._nombre = nombre
        self._apellido = apellido
        self._usuario = usuario
        self._contraseña = contraseña

    def mostrar_nombre_completo(self) -> None:
        print(f"Nombre: {self._nombre} {self._apellido}")

class Empleado(UsuarioRegistrado):
    def __init__(self, nombre : str, apellido : str, 
                 usuario : str, contraseña : str, cargo : str):
        super().__init__(nombre, apellido, usuario, contraseña)
        self._cargo = cargo

class EncargadoCatalogo(UsuarioRegistrado):
    def __init__(self, nombre : str, apellido : str, 
                 usuario : str, contraseña : str):
        super().__init__(nombre, apellido, usuario, contraseña)


class RestauradorJefe(UsuarioRegistrado):
    def __init__(self, nombre : str, apellido : str, 
                 usuario : str, contraseña : str):
        super().__init__(nombre, apellido, usuario, contraseña)

class DirectorMuseo(UsuarioRegistrado):
    def __init__(self, nombre : str, apellido : str, 
                 usuario : str, contraseña : str):
        super().__init__(nombre, apellido, usuario, contraseña)

class Autenticacion:
    def __init__(self, usuario, contraseña):
        self._usuario = usuario
        self._contraseña = contraseña



