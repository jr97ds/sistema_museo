from abc import ABC
from datetime import datetime
from obras import Obra

class Tramite (ABC):
    def __init__(self, obra : Obra, fecha_inicio : datetime):
        self._obra = obra
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = None
        self._estado = ""

class Restauracion(Tramite):
    def __init__(self, obra : Obra, fecha_inicio : datetime, 
                 tipo : str):
        super().__init__(obra, fecha_inicio)
        self._estado = "En proceso"
        self._tipo = tipo  

class Cesion(Tramite):
    def __init__(self, obra : Obra, fecha_inicio : datetime, 
                 museo_externo : MuseoExterno, importe : int , 
                 fecha_fin : datetime):
        super().__init__(obra, fecha_inicio)
        self._estado = "En Revisión"
        self._museo_externo = museo_externo
        self._importe = importe
        self._fecha_fin = fecha_fin

class MuseoExterno():
    def __init__(self, nombre : str):
        self._nombre = nombre

