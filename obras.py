from abc import ABC
from datetime import date

class Obra(ABC):
    def __init__(self, nombre : str, autor : str, periodo : str,
                  valor : int, fecha_creacion : date, 
                  fecha_entrada : date ):
        self._nombre = nombre
        self._autor = autor
        self._periodo = periodo
        self._valor =  valor
        self._fecha_creacion = fecha_creacion
        self._fecha_entrada = fecha_entrada
        self._estado = "En exhibición"
        self._restauraciones = []
        self._cesiones = []

    def __str__(self) -> str:
        return (
        f"Nombre: {self._nombre}, Autor: {self._autor},"
        f"Periodo: {self._periodo}, Valor: {self._valor},"
        f"Estado: {self._estado} , Fecha de Creación: {self._fecha_creacion}, "
        f"Fecha de Entrada: {self._fecha_entrada}"
        )
    
    @property
    def restauraciones(self):
        return self._restauraciones

class Cuadro(Obra):
    def __init__(self, nombre : str, autor : str, periodo : str,
                 valor : int, fecha_creacion : date, 
                 fecha_entrada : date, tecnica : str , 
                 estilo : str ):
        super().__init__(nombre, autor, periodo, valor, 
                         fecha_creacion, fecha_entrada)
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
                 estilo : str ):
        super().__init__(nombre, autor, periodo, valor, 
                         fecha_creacion, fecha_entrada)
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
                 fecha_entrada : date):
        super().__init__(nombre, autor, periodo, valor, 
                         fecha_creacion, fecha_entrada)