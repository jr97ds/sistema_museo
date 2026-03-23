from abc import ABC
from datetime import date, timedelta

from tramites import Cesion, Restauracion


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

    def enviar_a_restauracion(self, obra, tipo_restauracion) -> None:
        restauracion = Restauracion(obra, date.today(), tipo_restauracion)
        obra.restauraciones.append(restauracion)
        obra.estado = "En restauración"
    
    def finalizar_restauracion(self, obra) -> None:
        for restauracion in obra.restauraciones:
            if restauracion._estado == "En proceso":
                restauracion._estado = "Finalizada"
                restauracion._fecha_fin = date.today()
                obra.estado = "En exhibición"
                return

class DirectorMuseo(Empleado):
    def __init__(self, nombre : str, apellido : str, 
                 usuario : str, contraseña : str):
        super().__init__(nombre, apellido, usuario, contraseña)
        self._cargo = "Director del Museo"

    def crear_cesion(self, obra, museo_externo, importe, duracion_dias) -> Cesion:
        cesion = Cesion(obra, duracion_dias, museo_externo, importe)
        if obra.estado == "En exhibición":
            cesion.estado = "Aprobada" # type: ignore
            cesion.fecha_inicio = date.today() # type: ignore
            cesion.fecha_fin = date.today() + timedelta(days=duracion_dias) # type: ignore
            obra.estado = "En cesión"
        obra.cesiones.append(cesion)
        return cesion


