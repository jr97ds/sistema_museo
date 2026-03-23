from datetime import datetime

from obras import Cuadro, Escultura, Otro
from catalogo import Catalogo
from usuarios import EncargadoCatalogo , RestauradorJefe , DirectorMuseo

login = False # Controla el estado de inicio de sesión

# Datos precargados de empleados para demostración
encargado_catalogo = EncargadoCatalogo("Andres", "Gomez", "catalogo", "1234")
restaurador_jefe = RestauradorJefe("Maria", "Lopez", "restaurador", "1234")
director_museo = DirectorMuseo("Carlos", "Perez", "director", "1234")
empleados = [encargado_catalogo, restaurador_jefe, director_museo]

# Datos precargados de obras para demostración
cuadro1 = Cuadro("La Mona Lisa", "Leonardo da Vinci", "Renacimiento", 100,
                 datetime(1503, 1, 1), datetime(1912, 1, 1), # type: ignore
                 "Óleo sobre tabla", "Renacimiento")    
cuadro2 = Cuadro("La Noche Estrellada", "Vincent van Gogh", "Postimpresionismo", 9,
                 datetime(1889, 1, 1), datetime(1956, 1, 1), # type: ignore
                 "Óleo sobre lienzo", "Postimpresionismo")
escultura1 = Escultura("La Piedad", "Miguel Ángel", "Renacimiento", 100,
                     datetime(1498, 1, 1), datetime(1999, 1, 1), # type: ignore
                     "Mármol", "Renacimiento")
otro = Otro("Otra Obra", "Desconocido", "Contemporáneo", 700,
             datetime(2000, 1, 1), datetime(2005, 1, 1)) # type: ignore

catalogo =Catalogo([cuadro1, cuadro2, escultura1, otro])

def mostrar_menu_principal() -> None:
    print("\nBienvenido")
    print("1. Soy un visitante")
    print("2. Soy un empleado")
    print("0. Salir")

def no_valido() -> None:
    print("\nOpción no válida. Por favor, elija una opción válida.")

def log_in() -> tuple[EncargadoCatalogo | RestauradorJefe | 
                      DirectorMuseo | None, bool]: # type: ignore
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    for empleado in empleados:
        if empleado.usuario == usuario and empleado.contraseña == contraseña:
            print(f"\nBienvenido {empleado.cargo} - {empleado.nombre_completo}")
            return empleado,True # type: ignore
    print("\nNombre de usuario o contraseña incorrectos.")
    return None, False # type: ignore

def log_out() -> bool:
    login = False
    print("\nSesión cerrada. ¡Hasta luego!")
    return login
    
def seleccion_opccion() -> str:
    opcion = input("\nSeleccione una opción: ")
    return opcion



# -------- INICIO DEL PROGRAMA --------

# Logica de seleccion de visitante/Empleado
while True:
    mostrar_menu_principal()
    opcion = seleccion_opccion()
    
    # Ruta para visitantes
    if opcion == "1":
        print("\nBienvenido Visitante")

        # OJO PENDIENTE -----------


    # Ruta para empleados
    elif opcion == "2":
        print("\nInicie sesion para continuar")
        while not login:
            empleado_actual , login = log_in()

        if empleado_actual.cargo == "Encargado del Catálogo": #type: ignore
            while True:
                print("\n¿Qué desea hacer?")
                print("1. Ver catálogo")
                print("2. Agregar obra al catálogo")
                print("0. Cerrar sesión")

                opcion_empleado_catalogo = seleccion_opccion()

                if opcion_empleado_catalogo == "1":
                    catalogo.mostrar_catalogo()
                    continue

                elif opcion_empleado_catalogo == "2":
                    pass # OJO PENDIENTE -----------
                elif opcion_empleado_catalogo == "0":    
                    login = log_out()
                    break
                else:
                    no_valido()


        elif empleado_actual.cargo == "Restaurador Jefe":
            pass # OJO PENDIENTE -----------
        elif empleado_actual.cargo == "Director del Museo":
            pass # OJO PENDIENTE -----------
        
    elif opcion == "0":
        print("Saliendo.")
        break
    else:
        no_valido()
