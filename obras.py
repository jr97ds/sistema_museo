from abc import ABC
from datetime import date
from catalogo import Sala

class Obra(ABC):
    def __init__(self, nombre : str, autor : str, periodo : str,
                  valor : int, fecha_creacion : date, 
                  fecha_entrada : date, sala : Sala ):
        self._nombre = nombre
        self._autor = autor
        self._periodo = periodo
        self._valor =  valor
        self._fecha_creacion = fecha_creacion
        self._fecha_entrada = fecha_entrada
        self._estado = "En exhibición"
        self._restauraciones = []
        self._cesiones = []
        self._sala = sala

    def __str__(self) -> str:
        return (
        f"Nombre: {self._nombre}, Autor: {self._autor},"
        f"Periodo: {self._periodo}, Valor: {self._valor},"
        f"Estado: {self._estado} , Fecha de Creación: {self._fecha_creacion}, "
        f"Fecha de Entrada: {self._fecha_entrada} , Sala: {self._sala.nombre}"
        )
    
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
        self._estado = nuevo_estado

class Cuadro(Obra):
    def __init__(self, nombre : str, autor : str, periodo : str,
                 valor : int, fecha_creacion : date, 
                 fecha_entrada : date, tecnica : str , 
                 estilo : str , sala : Sala):
        super().__init__(nombre, autor, periodo, valor, 
                         fecha_creacion, fecha_entrada, sala)
        self._tecnica = tecnica
        self._estilo = estilo

    def __str__(self) -> str:
        return (super().__str__() + 
        f", Técnica: {self._tecnica},"
        f"Estilo: {self._estilo}"
        )

class Escultura(Obra):
    def __init__(self, nombre : str, autor : str, periodo : str,
                 valor : int, fecha_creacion : date, 
                 fecha_entrada : date, material : str , 
                 estilo : str , sala : Sala):
        super().__init__(nombre, autor, periodo, valor, 
                         fecha_creacion, fecha_entrada, sala) 
        self._material = material
        self._estilo = estilo

    def __str__(self) -> str:
        return (super().__str__() + 
        f", Material: {self._material},"
        f"Estilo: {self._estilo}"
        )

class Otro(Obra):
    def __init__(self, nombre : str, autor : str, periodo : str,
                 valor : int, fecha_creacion : date, 
                 fecha_entrada : date, sala : Sala):
        super().__init__(nombre, autor, periodo, valor, 
                         fecha_creacion, fecha_entrada, sala)