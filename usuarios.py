from __future__ import annotations
from abc import ABC
from datetime import date
from obras import Obra
from tramites import Cesion, MuseoExterno, Restauracion
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from catalogo import Catalogo, Sala


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

    def agregar_obra(self, catalogo: Catalogo, obra: Obra, sala: Sala) -> str:
        catalogo.agregar_obra(obra)
        sala.agregar_obra(obra)
        return f"Obra '{obra.nombre}' agregada al catálogo y asignada a la sala '{sala.nombre}'."

    def eliminar_obra(self, catalogo: Catalogo, titulo: str) -> str:
        obra = catalogo.buscar_obra(titulo)
        if not obra:
            return f"Obra '{titulo}' no encontrada en el catálogo."
        catalogo.eliminar_obra(obra)
        return f"Obra '{obra.nombre}' eliminada del catálogo."

class RestauradorJefe(Empleado):
    """Clase para representar un restaurador jefe"""
    def __init__(self, nombre: str, apellido: str, 
                 usuario: str, contraseña: str):
        super().__init__(nombre, apellido, usuario, contraseña)
        self._cargo = "Restaurador Jefe"

    def enviar_a_restauracion(self, catalogo: Catalogo, titulo: str,
                               tipo_restauracion: str) -> str:
        obra_a_restaurar = catalogo.buscar_obra(titulo)
        if not obra_a_restaurar:
            return (f"Obra '{titulo}' no encontrada en el catálogo.")
        if obra_a_restaurar.estado == "En restauración":
            return (f"Obra '{titulo}' ya está en restauración.")
        restauracion = Restauracion(obra_a_restaurar, date.today(), tipo_restauracion)
        obra_a_restaurar.agregar_restauracion(restauracion)
        obra_a_restaurar.estado = "En restauración"
        return (f"Obra '{titulo}' enviada a restauración.")

    def finalizar_restauracion(self, catalogo: Catalogo, 
                               titulo: str) -> str:
        obra_a_finalizar = catalogo.buscar_obra(titulo)
        
        if obra_a_finalizar:
            if obra_a_finalizar.estado == "En restauración":
                 for restauracion in obra_a_finalizar.restauraciones:
                    if restauracion.estado == "En proceso":
                        restauracion.finalizar() 
                        obra_a_finalizar.estado = "En exhibición"
                        return (f"Restauración de "
                                f"'{obra_a_finalizar.titulo}' finalizada.")
            else:
                return (f"Obra '{obra_a_finalizar.titulo}' "
                        f"no está en restauración.")
        else:
                return (f"Obra '{titulo}' no encontrada")

class DirectorMuseo(Empleado):
    """Clase para representar el director del museo"""
    def __init__(self, nombre: str, apellido: str, 
                 usuario: str, contraseña: str):
        super().__init__(nombre, apellido, usuario, contraseña)
        self._cargo = "Director del Museo"

    def crear_cesion(self, catalogo: Catalogo, 
                     titulo: str, 
                     nombre_museo: str, 
                     museos_externos: list[MuseoExterno], 
                     importe: int, 
                     duracion_dias: int) -> str:
        
        obra = catalogo.buscar_obra(titulo)
        if not obra:
            return  f"Obra '{titulo}' no encontrada."
        museo_escogido = None
        for m in museos_externos:
            if m.nombre.lower() == nombre_museo.lower():
                museo_escogido = m
                break
        if not museo_escogido:
            return f"Museo externo '{nombre_museo}' no encontrado."
        
        cesion = Cesion(obra, duracion_dias, museo_escogido, importe)
        if obra.estado == "En exhibición":
            cesion.aprobar(date.today()) 
            obra.estado = "En cesión"
        obra.agregar_cesion(cesion)
        return f"Cesion creada para obra '{obra.nombre}'- Estado: '{cesion.estado}'."
    
