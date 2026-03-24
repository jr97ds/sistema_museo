
from abc import ABC, abstractmethod
from datetime import date
from typing import Optional
from catalogo import Catalogo, Sala
from obras import Cuadro, Escultura, Obra, Otro
from tramites import MuseoExterno
from usuarios import Empleado
from usuarios import DirectorMuseo, EncargadoCatalogo, RestauradorJefe
from utils import no_valido, seleccion_opcion



def asignar_sala(salas) -> Sala:
    for idx, sala in enumerate(salas):
        print(f"{idx + 1}. {sala.nombre}")
    while True:
        opcion_sala = int(input("\nSeleccione la sala para la obra: "))
        if 1 <= opcion_sala <= len(salas):
            sala_seleccionada = salas[opcion_sala - 1]
            return sala_seleccionada
        else:
            print("\nOpción de sala no válida.")

class Menu(ABC):
    """Clase base para representar un menú en el sistema del museo."""
    def __init__(self, empleado: Empleado, **contexto):
        self._empleado = empleado
        self._contexto = contexto
    
    @abstractmethod
    def ejecutar(self) -> None:
        """Método abstracto para ejecutar loop del menu"""
        pass

    @staticmethod
    def crear_menu(empleado: Empleado, **kwargs) -> "Menu":
        """Crea el menú adecuado según el tipo de empleado"""

        if isinstance(empleado, EncargadoCatalogo):
            return MenuEncargadoCatalogo(empleado, **kwargs) #type: ignore
        elif isinstance(empleado, RestauradorJefe):
            return MenuRestauradorJefe(empleado, **kwargs) #type: ignore
        elif isinstance(empleado, DirectorMuseo):
            return MenuDirectorMuseo(empleado, **kwargs) #type: ignore  
        raise ValueError("Tipo de empleado no reconocido para crear menú.")
    
class MenuEncargadoCatalogo(Menu):
    """Clase para representar el menú del encargado del catálogo"""

    def ejecutar(self) -> None:
        catalogo = self._contexto["catalogo"]
        salas = self._contexto["salas"]
        while True:
            print("\n¿Qué desea hacer?")
            print("1. Ver catálogo")
            print("2. Agregar obra al catálogo")
            print("0. Cerrar sesión")
            opcion_empleado_catalogo = seleccion_opcion()
            # Mostrar Catalogo
            if opcion_empleado_catalogo == "1":
                catalogo.mostrar_obras()
            # Agregar Producto
            elif opcion_empleado_catalogo == "2":
                nueva_obra = self._crear_obra(catalogo, salas)
                print("\nObra agregada al catálogo:")
                print(nueva_obra) 
            # Cerrar Sesión de Empleado
            elif opcion_empleado_catalogo == "0":
                break
            else:
                no_valido()

    def _crear_obra(self, catalogo: Catalogo,
                     salas: list[Sala]) -> Optional[Obra]:
        """Crear una nueva obra a partir de la entrada del usuario"""
        while True:
            print("\n¿Qué tipo de obra desea agregar?")
            print("1. Cuadro")
            print("2. Escultura")   
            print("3. Otro")
            tipo_obra = seleccion_opcion()
            if tipo_obra not in ["1", "2", "3"]:
                print("Opción no válida.")
                continue
            nombre = input("Nombre del cuadro: ")
            autor = input("Autor del cuadro: ")
            periodo = input("Periodo del cuadro: ")

            try:
                valor = int(input("Valor: "))
                fecha_creacion = date.fromisoformat(input(
                    "Fecha de creación (YYYY-MM-DD): "))
            except ValueError: 
                print("\nValor o fecha no válidos. " \
                "Por favor, ingrese un número para el valor y " \
                "una fecha en formato YYYY-MM-DD.")
                return None

            fecha_entrada = date.today() # Fecha actual

            if tipo_obra == "1":
                tecnica = input("Técnica del cuadro: ")
                estilo = input("Estilo del cuadro: ")
                nueva_obra = Cuadro(nombre, autor, periodo, valor, 
                                    fecha_creacion, fecha_entrada, 
                                    tecnica, estilo)
                       
            elif tipo_obra == "2":
                material = input("Material de la escultura: ")
                estilo = input("Estilo de la escultura: ")
                nueva_obra = Escultura(nombre, autor, periodo, valor, 
                                            fecha_creacion, fecha_entrada, 
                                            material, estilo)
            
            elif tipo_obra == "3":
                nueva_obra = Otro(nombre, autor, periodo, valor, 
                                fecha_creacion, fecha_entrada)
            else:
                no_valido()

            sala = asignar_sala(salas)
            sala.agregar_obra(nueva_obra)
            catalogo.agregar_obra(nueva_obra)
            return nueva_obra


class MenuRestauradorJefe(Menu):
    """Clase para representar el menú del restaurador jefe"""
    def ejecutar(self) -> None:
        empleado = self._empleado
        catalogo = self._contexto["catalogo"]

        while True:
            print("\n¿Qué desea hacer?")
            print("1. Ver obras en exhibición")
            print("2. Ver restauraciónes")
            print("3. Enviar obra a restauración")
            print("4. Finalizar restauración")
            print("0. Cerrar sesión")
            opcion_empleado_restauracion = seleccion_opcion()
            # Mostrar Obras en Exhibición
            if opcion_empleado_restauracion == "1":
                catalogo.mostrar_obras()
            # Mostrar Restauraciones
            elif opcion_empleado_restauracion == "2":
                self._mostrar_restauraciones(catalogo)
            # Enviar obra a restauración
            elif opcion_empleado_restauracion == "3":
                self._enviar_a_restauracion(self._empleado, # type: ignore
                                            catalogo) 
            # Marcar obra como restaurada
            elif opcion_empleado_restauracion == "4":
                self._finalizar_restauracion(self._empleado, # type: ignore
                                             catalogo) 
                    
            elif opcion_empleado_restauracion == "0":
                break   
            else:
                no_valido()

    @staticmethod
    def _mostrar_restauraciones(catalogo: Catalogo) -> None:
        organizadas = []
        for obra in catalogo.obras:
            for restauracion in obra.restauraciones:
                organizadas.append(restauracion)

        if organizadas:
            organizadas.sort(key=lambda r: r.fecha_inicio)
            for restauracion in organizadas:
                print(restauracion)
        else:
            print("\nNo hay obras en restauración.")

    @staticmethod
    def _enviar_a_restauracion(empleado: RestauradorJefe, 
                               catalogo: Catalogo) -> None:
        """Ruta para enviar obra a restaurar"""

        titulo_obra = input("\nIngrese el título de la obra a restaurar: ")
        obra_a_restaurar = catalogo.buscar_obra(titulo_obra)
    
        if not obra_a_restaurar:
            print(f"\nObra '{titulo_obra}' no encontrada en exhibición.")
            return
        if obra_a_restaurar.estado == "En restauración":
            print(f"\nLa obra '{obra_a_restaurar.titulo}'"
                    f"ya está en restauración.")
            return
        tipo_restauracion = input("Ingrese el tipo de restauración: ")
        empleado.enviar_a_restauracion(obra_a_restaurar,
                                        tipo_restauracion) 
        print(f"\nObra '{obra_a_restaurar.titulo}' enviada a restauración.")

    @staticmethod
    def _finalizar_restauracion(empleado: RestauradorJefe, 
                                catalogo: Catalogo) -> None:
        """Ruta para finalizar restauración de obra"""

        titulo_obra = input(
            "\nIngrese el título de la obra a finalizar: "
            )
        obra_a_finalizar = catalogo.buscar_obra(titulo_obra)
        
        if obra_a_finalizar:
            if obra_a_finalizar.estado == "En restauración":
                empleado.finalizar_restauracion(obra_a_finalizar)
                print(f"\nLa restauracion de la obra "
                      f"'{obra_a_finalizar.titulo}' fue finalizada.")
                return
            else:
                print(f"\nLa obra '{obra_a_finalizar.titulo}'"
                      f" no está en restauración.")
                return
        else:
                print(f"\nObra '{titulo_obra}' no encontrada")
                return  


class MenuDirectorMuseo(Menu):
    """Clase para representar el menú del director del museo"""
    def ejecutar(self) -> None:
        empleado = self._empleado
        catalogo = self._contexto["catalogo"]
        museos_externos = self._contexto["museos_externos"]
        
        while True:
            print("\n¿Qué desea hacer?")
            print("1. Ver valor total del catálogo")
            print("2. Ver todas las cesiones")
            print("3. Crear nueva cesión")
            print("0. Cerrar sesión")
            opcion_empleado_director = seleccion_opcion()
            
            # Mostrar valor total del catálogo
            if opcion_empleado_director == "1":
                valor_total = catalogo.calcular_valor_total()
                print(f"\nValor total del catálogo: ${valor_total}")
                
            # Ver todas las cesiones
            elif opcion_empleado_director == "2":
                self._mostrar_cesiones(catalogo)
                
            #Crear nueva cesion
            elif opcion_empleado_director == "3":
                self._crear_cesion(self._empleado, catalogo, # type: ignore
                                    museos_externos) 

            elif opcion_empleado_director == "0":
                break
            else:
                no_valido()


    @staticmethod               
    def _mostrar_cesiones(catalogo: Catalogo) -> None:
        """Muestra todas las cesiones del catálogo 
        ordenadas por fecha de inicio"""
        encontradas = False
        for obra in catalogo.obras:
            if obra.cesiones:
                encontradas = True
                for cesion in obra.cesiones:
                    print(cesion)
        if not encontradas:
            print("\nNo hay obras en cesión.")
    
    @staticmethod
    def _crear_cesion(empleado: DirectorMuseo, catalogo: Catalogo, 
                      museos_externos: list[MuseoExterno]) -> None:
        """Crea una nueva cesión para una obra del catálogo"""

        input_titulo = input(
            "\nIngrese el título de la obra para la cesión: "
            )
        obra = catalogo.buscar_obra(input_titulo)
        if not obra:
            print(f"\nObra '{input_titulo}' no encontrada.")
            return
        input_museo = input(
            "\nIngrese el nombre del museo externo para la cesión: "
            )
        museo = None
        for m in museos_externos:
            if m.nombre.lower() == input_museo.lower():
                museo = m
                break
        if not museo:
            print(f"\nMuseo externo '{input_museo}' no encontrado.")
            return


        try:
            importe = int(input("\nIngrese el importe de la cesión: "))
            duracion_dias = int(
                input("\nIngrese la duración de la cesión en días: ")
                )
        except ValueError:
            print("\nValores invalidos. Por favor, ingrese números enteros.")
            return
        
        cesion = empleado.crear_cesion(obra, museo, importe, duracion_dias) 
        print(f"\nSolicitud de Cesión creada: {cesion}")
        print(f"\nEstado: {cesion.estado}")
        
        
       