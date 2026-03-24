from abc import ABC
from datetime import date, timedelta
from obras import Obra
from tramites import Cesion, MuseoExterno, Restauracion


class UsuarioRegistrado(ABC):
    """Clase base para representar un usuario registrado en el sistema"""
    def __init__(self, nombre: str, apellido: str, 
                 usuario: str, contraseña: str):
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
    
    def verificar_credenciales(self, usuario: str, contraseña: str) -> bool:
        return self._usuario == usuario and self._contraseña == contraseña
    
class Empleado(UsuarioRegistrado):
    """Clase para representar un empleado del museo"""
    def __init__(self, nombre: str, apellido: str, 
                 usuario: str, contraseña: str):
        super().__init__(nombre, apellido, usuario, contraseña)
        self._cargo = None

    @property
    def cargo(self):
        return self._cargo
    

class EncargadoCatalogo(Empleado):
    """Clase para representar un encargado del catálogo"""
    def __init__(self, nombre: str, apellido: str, 
                 usuario: str, contraseña: str):
        super().__init__(nombre, apellido, usuario, contraseña)
        self._cargo = "Encargado del Catálogo"
        
class RestauradorJefe(Empleado):
    """Clase para representar un restaurador jefe"""
    def __init__(self, nombre: str, apellido: str, 
                 usuario: str, contraseña: str):
        super().__init__(nombre, apellido, usuario, contraseña)
        self._cargo = "Restaurador Jefe"

    def enviar_a_restauracion(self, obra: Obra, tipo_restauracion: str) -> None:
        restauracion = Restauracion(obra, date.today(), tipo_restauracion)
        obra.agregar_restauracion(restauracion)
        obra.estado = "En restauración"
    
    def finalizar_restauracion(self, obra: Obra) -> None:
        for restauracion in obra.restauraciones:
            if restauracion.estado == "En proceso":
                restauracion.finalizar() 
                obra.estado = "En exhibición"
                return

class DirectorMuseo(Empleado):
    """Clase para representar el director del museo"""
    def __init__(self, nombre: str, apellido: str, 
                 usuario: str, contraseña: str):
        super().__init__(nombre, apellido, usuario, contraseña)
        self._cargo = "Director del Museo"

    def crear_cesion(self, obra: Obra, museo_externo: MuseoExterno,
                      importe: int, duracion_dias: int) -> Cesion:
        cesion = Cesion(obra, duracion_dias, museo_externo, importe)
        if obra.estado == "En exhibición":
            cesion.aprobar(date.today()) 
            obra.estado = "En cesión"
        obra.agregar_cesion(cesion)
        return cesion


