from datetime import date
from auth import Auth
from menus import Menu, no_valido, seleccion_opcion
from obras import Cuadro, Escultura, Otro
from catalogo import Catalogo, Pantalla, Sala
from servicios_diarios import VerificarCesionesVencidas, RestauracionesAutomaticas
from tramites import MuseoExterno
from usuarios import EncargadoCatalogo , RestauradorJefe , DirectorMuseo
from utils import no_valido, seleccion_opcion

# -----------------PRECARGA DE DATOS PARA DEMOSTRACIÓN----------------- #
# Datos precargados de empleados para demostración
encargado_catalogo = EncargadoCatalogo("Andres", "Gomez", "catalogo", "1234")
restaurador_jefe = RestauradorJefe("Maria", "Lopez", "restaurador", "1234")
director_museo = DirectorMuseo("Carlos", "Perez", "director", "1234")
empleados = [encargado_catalogo, restaurador_jefe, director_museo]

# Datos precargados de museos externos para demostración
museo1 = MuseoExterno("Museo de Arte Moderno")
museo2 = MuseoExterno("Museo Nacional de Bellas Artes")
museo3 = MuseoExterno("Museo de Arte Contemporáneo")
museos_externos = [museo1, museo2, museo3]

# Datos precargados de salas para demostración
sala1 = Sala("Sala 1")
sala2 = Sala("Sala 2")
sala3 = Sala("Sala 3")
salas = [sala1, sala2, sala3]

# Datos precargados de obras para demostración
cuadro1 = Cuadro("La Mona Lisa", "Leonardo da Vinci", "Renacimiento", 100,
                date(1503, 1, 1), date(2023, 1, 1), 
                "Óleo sobre tabla", "Renacimiento") 
sala1.agregar_obra(cuadro1) 
cuadro2 = Cuadro("La Noche Estrellada", "Vincent van Gogh", "Postimpresionismo"
                , 9, date(1889, 1, 1), date(2022, 1, 1), 
                "Óleo sobre lienzo", "Postimpresionismo") 
sala2.agregar_obra(cuadro2)
escultura1 = Escultura("La Piedad", "Miguel Ángel", "Renacimiento", 100,
                    date(1498, 1, 1), date(2026, 1, 1),
                    "Mármol", "Renacimiento") 
sala3.agregar_obra(escultura1)
otro = Otro("Otra Obra", "Desconocido", "Contemporáneo", 700,
            date(2000, 1, 1), date(2020, 1, 1))
sala1.agregar_obra(otro)
catalogo =Catalogo([cuadro1, cuadro2, escultura1, otro])

# Inicialización de la pantalla con las salas precargadas
pantalla = Pantalla(salas)

# Contexto para pasar a los menús de empleados
contexto = {
    "catalogo": catalogo,
    "museos_externos": museos_externos,
    "salas": salas
}

# Inicialización del sistema de autenticación con los empleados precargados
auth = Auth(empleados)

def mostrar_menu_principal() -> None:
    print("\nBienvenido")
    print("1. Ver Pantallas para visitantes")
    print("2. Sistema de Empleados")
    print("0. Salir")
    
# ----------------- INICIO DEL PROGRAMA ----------------- #

# Procesos Diarios
servicio_cesiones_vencidas = VerificarCesionesVencidas()
servicio_cesiones_vencidas.ejecutar(catalogo)
servicio_restauraciones_por_edad = RestauracionesAutomaticas()
servicio_restauraciones_por_edad.ejecutar(catalogo, restaurador_jefe)

# Logica de seleccion de visitante/Empleado
while True:
    mostrar_menu_principal()
    opcion = seleccion_opcion()
    # Ruta para visitantes
    if opcion == "1":
        pantalla.mostrar_salas()
        input("\nPresione Enter para volver al menú principal...")
    # Ruta para empleados
    elif opcion == "2":
        # Ciclo de inicio de sesión
        while not auth.is_login:
            print("\nInicie sesion para continuar")
            input_usuario = input("Usuario: ")
            input_contraseña = input("Contraseña: ")    
            # Intento de inicio de sesion
            if not auth.login(input_usuario, input_contraseña):
                print("\nCredenciales incorrectas. Intente de nuevo.")
        # Si login exitoso , mostrar menu correspondiente al tipo de empleado
        if auth.empleado_actual:
            print(f"\nBienvenido {auth.empleado_actual.cargo} - " 
                  f"{auth.empleado_actual.nombre_completo}") 
            menu = Menu.crear_menu(auth.empleado_actual,**contexto) 
            menu.ejecutar()
            auth.cerrar_sesion()
    elif opcion == "0":
        print("Saliendo.")
        break
    else:
        no_valido()
