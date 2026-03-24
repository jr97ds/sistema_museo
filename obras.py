from abc import ABC, abstractmethod
from datetime import date

class Obra(ABC):
    """Clase base para representar una obra de arte en el museo."""
    def __init__(self, nombre: str, autor: str, periodo: str,
                  valor: int, fecha_creacion: date, 
                  fecha_entrada: date):
        self._nombre = nombre
        self._autor = autor
        self._periodo = periodo
        self._valor = valor
        self._fecha_creacion = fecha_creacion
        self._fecha_entrada = fecha_entrada
        self._estado = "En exhibición"
        self._restauraciones = []
        self._cesiones = []

    @abstractmethod
    def detalles_especificos(self) -> str:
        """Método abstracto para obtener detalles específicos de 
        cada tipo de obra."""
        pass

    def __str__(self) -> str:
        inicial = (
        f"Nombre: {self._nombre}, Autor: {self._autor}, "
        f"Periodo: {self._periodo}, Valor: {self._valor}, "
        f"Estado: {self._estado}, Fecha de Creación: {self._fecha_creacion}, "
        f"Fecha de Entrada: {self._fecha_entrada}"
        )
        extras = self.detalles_especificos()
        if extras:
            return inicial + ", " + extras
        else:
            return inicial
    
    @property
    def restauraciones(self):
        return self._restauraciones
    
    @property
    def valor(self):
        return self._valor
    
    @property
    def titulo(self):
        return self._nombre
    
    @property
    def cesiones(self):
        return self._cesiones
    
    @property
    def estado(self):
        return self._estado
    
    @property
    def fecha_entrada(self):
        return self._fecha_entrada
    
    @estado.setter
    def estado(self, nuevo_estado):
        estados_validos = ["En exhibición", "En restauración", "En cesión"]
        # Asegura que solo se puedan asignar estados válidos a la obra
        if nuevo_estado not in estados_validos:
            raise ValueError(
                f"Estado no válido"
                f"Opciones {estados_validos}"
            )
        
        self._estado = nuevo_estado


class Cuadro(Obra):
    """Clase para representar un cuadro, hereda de Obra."""
    def __init__(self, nombre: str, autor: str, periodo: str,
                 valor: int, fecha_creacion: date, 
                 fecha_entrada: date, tecnica: str, 
                 estilo: str):
        super().__init__(nombre, autor, periodo, valor, 
                         fecha_creacion, fecha_entrada)
        self._tecnica = tecnica
        self._estilo = estilo

    def detalles_especificos(self) -> str:
        return f"Técnica: {self._tecnica}, Estilo: {self._estilo}"


class Escultura(Obra):
    """Clase para representar una escultura, hereda de Obra."""
    def __init__(self, nombre: str, autor: str, periodo: str,
                 valor: int, fecha_creacion: date, 
                 fecha_entrada: date, material: str, 
                 estilo: str):
        super().__init__(nombre, autor, periodo, valor, 
                         fecha_creacion, fecha_entrada)
        self._material = material
        self._estilo = estilo

    def detalles_especificos(self) -> str:
        return f"Material: {self._material}, Estilo: {self._estilo}"


class Otro(Obra):
    """Clase para representar otro tipo de obra, hereda de Obra."""
    def __init__(self, nombre: str, autor: str, periodo: str,
                 valor: int, fecha_creacion: date, 
                 fecha_entrada: date):
        super().__init__(nombre, autor, periodo, valor, 
                         fecha_creacion, fecha_entrada)

    def detalles_especificos(self) -> str:
        return ""