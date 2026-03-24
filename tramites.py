from abc import ABC, abstractmethod
from datetime import date
from obras import Obra

class Tramite (ABC):
    """Clase base para representar un trámite relacionado con una obra"""
    ESTADOS_VALIDOS = []

    def __init__(self, obra: Obra):
        self._obra = obra
        self._fecha_inicio = None
        self._fecha_fin = None
        self._estado = ""

    @property
    def estado(self):
        return self._estado
    
    @property
    def fecha_inicio(self):
        return self._fecha_inicio
    
    @property
    def fecha_fin(self):
        return self._fecha_fin

    @estado.setter
    def estado(self,nuevo_estado):
        # Asegura que solo se puedan asignar estados válidos al trámite
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            raise ValueError(f"Estado no válido."
                             f"Estados válidos: {self.ESTADOS_VALIDOS}")
        self._estado = nuevo_estado

    @fecha_fin.setter
    def fecha_fin(self, nueva_fecha_fin):
        self._fecha_fin = nueva_fecha_fin
    
    @fecha_inicio.setter
    def fecha_inicio(self, nueva_fecha_inicio):
        self._fecha_inicio = nueva_fecha_inicio
    
    # Método abstracto para añadir detalles específicos de cada tipo de trámite
    @abstractmethod
    def detalles_especificos(self) -> str:  
        pass

    def __str__(self) -> str:
        inicial = (f"Obra: '{self._obra.titulo}' - "  
                f"Estado: {self._estado} - Fecha Inicio: "
                f"{self._fecha_inicio} - Fecha Fin: {self._fecha_fin}")
        extras = self.detalles_especificos()
        if extras:
            return inicial + ", " + extras
        else:
            return inicial

class Restauracion(Tramite):
    """Clase para representar un trámite de restauración, hereda de Tramite."""
    # Define los estados válidos para el trámite de restauración
    ESTADOS_VALIDOS = ["En proceso", "Finalizada"]

    def __init__(self, obra: Obra, fecha_inicio: date, 
                 tipo: str):
        super().__init__(obra)
        self._fecha_inicio = fecha_inicio
        self.estado = "En proceso"
        self._tipo = tipo  
    
    @property
    def tipo(self):
        return self._tipo
    
    def detalles_especificos(self) -> str:
        return f"Tipo de Restauración: {self._tipo}"

class MuseoExterno():
    """Clase para representar un museo al que se le puede ceder una obra."""
    def __init__(self, nombre: str):
        self._nombre = nombre
    
    @property
    def nombre(self):
        return self._nombre
    

class Cesion(Tramite):
    """Clase para representar un trámite de cesión, hereda de Tramite."""
    # Define los estados válidos para el trámite de cesión
    ESTADOS_VALIDOS = ["Pendiente", "Aprobada", "Finalizada"]

    def __init__(self, obra: Obra, duracion_dias: int, 
                 museo_externo: MuseoExterno, importe: int):
        super().__init__(obra)
        self._duracion_dias = duracion_dias
        self.estado = "Pendiente"
        self._museo_externo = museo_externo
        self._importe = importe
    
    @property
    def museo_externo(self):
        return self._museo_externo
    
    @property
    def importe(self):
        return self._importe
    
    def detalles_especificos(self) -> str:
        return (f"Museo: {self._museo_externo.nombre}, "
                f"Duración (días): {self._duracion_dias}, "
                f"Importe: {self._importe}")


