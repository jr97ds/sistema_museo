
from abc import ABC, abstractmethod

from catalogo import Catalogo, Sala
from obras import Obra
from main import crear_producto
from usuarios import Empleado, EncargadoCatalogo
from auth import Auth

def seleccion_opcion() -> str:
    opcion = input("\nSeleccione una opción: ")
    return opcion

def no_valido() -> None:
    print("\nOpción no válida. Por favor, elija una opción válida.")


class Menu(ABC):
    """Clase base para representar un menú en el sistema del museo."""
    def __init__(self, empleado: Empleado, **contexto):
        self.empleado = empleado
        self.contexto = contexto
    
    @abstractmethod
    def ejecutar(self) -> None:
        """Método abstracto para ejecutar loop del menu"""
        pass

    @abstractmethod
    def crear_menu(self,empleado: Empleado, **kwargs) -> None:
        """Método abstracto para crear el menú específico 
        según el tipo de empleado"""
        if isinstance(empleado, EncargadoCatalogo):
            return MenuEncargadoCatalogo(empleado, **kwargs)
        elif isinstance(empleado, RestauradorJefe):
            return MenuRestauradorJefe(empleado, **kwargs)
        elif isinstance(empleado, DirectorMuseo):
            return MenuDirectorMuseo(empleado, **kwargs)
        raise ValueError("Tipo de empleado no reconocido para crear menú.")
    
    class MenuEncargadoCatalogo(Menu):
    
    while True:
        print("\n¿Qué desea hacer?")
        print("1. Ver catálogo")
        print("2. Agregar obra al catálogo")
        print("0. Cerrar sesión")
        opcion_empleado_catalogo = seleccion_opcion()
        # Mostrar Catalogo
        if opcion_empleado_catalogo == "1":
            catalogo.mostrar_obras()
            continue
        # Agregar Producto
        elif opcion_empleado_catalogo == "2":
            nueva_obra = crear_producto()
            catalogo.agregar_obra(nueva_obra)
            print("\nObra agregada al catálogo:")
            print(nueva_obra)
            continue 
        # Cerrar Sesión de Empleado
        elif opcion_empleado_catalogo == "0":
            Auth.logout(): # type: ignore
            print("\nSesión cerrada.")
            break
        else:
            no_valido()
