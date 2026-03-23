class UsuarioRegistrado:
    def __init__(self, nombre, apellido, usuario, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.contraseña = contraseña

    def mostrar_nombre_completo(self) -> None:
        print(f"Nombre: {self.nombre} {self.apellido}")

class Empleado(UsuarioRegistrado):
    def __init__(self, nombre : str, apellido : str, 
                 usuario : str, contraseña : str, cargo : str):
        super().__init__(nombre, apellido, usuario, contraseña)
        self.cargo = cargo
    

class EncargadoCatalogo(UsuarioRegistrado):
    def __init__(self, nombre : str, apellido : str, usuario : str, contraseña : str, departamento : str):
        super().__init__(nombre, apellido, usuario, contraseña)


class RestauradorJefe(UsuarioRegistrado):
    def __init__(self, nombre : str, apellido : str, usuario : str, contraseña : str, especialidad : str):
        super().__init__(nombre, apellido, usuario, contraseña)

class DirectorMuseo(UsuarioRegistrado):
    def __init__(self, nombre, apellido, usuario, contraseña, departamento):
        super().__init__(nombre, apellido, usuario, contraseña)

class Autenticacion:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña



