from abc import ABC
from datetime import date, datetime
from obras import Obra

class Tramite (ABC):
    def __init__(self, obra : Obra):
        self._obra = obra
        self._fecha_inicio = None
        self._fecha_fin = None
        self._estado = ""

class Restauracion(Tramite):
    def __init__(self, obra : Obra, fecha_inicio : date, 
                 tipo : str):
        super().__init__(obra)
        self._fecha_inicio = fecha_inicio
        self._estado = "En proceso"
        self._tipo = tipo  
    
    @property
    def tipo(self):
        return self._tipo
    @property
    def estado(self):
        return self._estado
    @property
    def fecha_inicio(self):
        return self._fecha_inicio

    def __str__(self) -> str:
        return (f"Restauración de '{self._obra.titulo}' - " 
                f"Tipo: {self._tipo} - " 
                f"Estado: {self._estado} - Fecha Inicio: "
                f"{self._fecha_inicio} - Fecha Fin: {self._fecha_fin}")

class Cesion(Tramite):
    def __init__(self, obra : Obra, duracion_dias : int, 
                 museo_externo : MuseoExterno, importe : int):
        super().__init__(obra)
        self.duracion_dias = duracion_dias
        self._estado = "Pendiente"
        self._museo_externo = museo_externo
        self._importe = importe
    
    @property
    def museo_externo(self):
        return self._museo_externo
    
    @property
    def estado(self):
        return self._estado
    
    @property
    def fecha_fin(self):
        return self._fecha_fin
    
    @property
    def fecha_inicio(self):
        return self._fecha_inicio
    
    @estado.setter
    def estado(self,nuevo_estado):
        self._estado = nuevo_estado

    @fecha_fin.setter
    def fecha_fin(self, nueva_fecha_fin):
        self._fecha_fin = nueva_fecha_fin
    
    @fecha_inicio.setter
    def fecha_inicio(self, nueva_fecha_inicio):
        self._fecha_inicio = nueva_fecha_inicio
    
    def __str__(self) -> str:
        return (f"Cesión de '{self._obra.titulo}' - Museo: "
                f"{self._museo_externo._nombre} - Importe: "
                f"${self._importe} - Estado: {self._estado} - "
                f"Fecha Inicio: {self._fecha_inicio} - Fecha Fin: "
                f"{self._fecha_fin}")

class MuseoExterno():
    def __init__(self, nombre : str):
        self._nombre = nombre

@property
def nombre(self):
    return self._nombre
