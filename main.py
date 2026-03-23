from datetime import datetime, date

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
cuadro2 = Cuadro("La Noche Estrellada", "Vincent van Gogh", "Postimpresionismo"
                , 9, datetime(1889, 1, 1), datetime(1956, 1, 1), # type: ignore
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
    
def seleccion_opcion() -> str:
    opcion = input("\nSeleccione una opción: ")
    return opcion

def crear_producto():
    while True:
        print("\n¿Qué tipo de obra desea agregar?")
        print("1. Cuadro")
        print("2. Escultura")   
        print("3. Otro")
        tipo_obra = seleccion_opcion()

    
        if tipo_obra == "1":
            nombre = input("Nombre del cuadro: ")
            autor = input("Autor del cuadro: ")
            periodo = input("Periodo del cuadro: ")
            valoracion = int(input("Valor: "))
            fecha_creacion = date.fromisoformat(input(
                "Fecha de creación (YYYY-MM-DD): "))
            fecha_entrada = date.today() # Fecha actual
            tecnica = input("Técnica del cuadro: ")
            estilo = input("Estilo del cuadro: ")
            nuevo_cuadro = Cuadro(nombre, autor, periodo, valoracion, 
                                fecha_creacion, fecha_entrada, tecnica, estilo)
            return nuevo_cuadro
    
        elif tipo_obra == "2":
            nombre = input("Nombre de la escultura: ")
            autor = input("Autor de la escultura: ")
            periodo = input("Periodo de la escultura: ")
            valoracion = int(input("Valor: "))
            fecha_creacion = date.fromisoformat(input(
                "Fecha de creación (YYYY-MM-DD): "))
            fecha_entrada = date.today() # Fecha actual
            material = input("Material de la escultura: ")
            estilo = input("Estilo de la escultura: ")
            nueva_escultura = Escultura(nombre, autor, periodo, valoracion, 
                                        fecha_creacion, fecha_entrada, 
                                        material, estilo)
            return nueva_escultura
        
        elif tipo_obra == "3":
            nombre = input("Nombre de la obra: ")
            autor = input("Autor de la obra: ")
            periodo = input("Periodo de la obra: ")
            valoracion = int(input("Valor: "))
            fecha_creacion = date.fromisoformat(input(
                "Fecha de creación (YYYY-MM-DD): "))
            fecha_entrada = date.today() # Fecha actual
            nueva_obra = Otro(nombre, autor, periodo, valoracion, 
                            fecha_creacion, fecha_entrada)
            return nueva_obra
        else:
            no_valido()
            continue

def mostrar_restauraciones(catalogo: Catalogo) -> None:
        encontradas = False
        for obra in catalogo._obras:
            if obra.restauraciones:
                encontradas = True
                for restauracion in obra.restauraciones:
                    print(restauracion)
        if not encontradas:
            print("\nNo hay obras en restauración.")


# -------- INICIO DEL PROGRAMA --------

# Logica de seleccion de visitante/Empleado
while True:
    mostrar_menu_principal()
    opcion = seleccion_opcion()
    
    # Ruta para visitantes
    if opcion == "1":
        print("\nBienvenido Visitante")

        # OJO PENDIENTE -----------


    # Ruta para empleados
    elif opcion == "2":
        print("\nInicie sesion para continuar")
        while not login:
            empleado_actual , login = log_in()

        # Ruta para encargado del catalogo
        if empleado_actual.cargo == "Encargado del Catálogo": #type: ignore
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
                    login = log_out()
                    break
                else:
                    no_valido()

        # Ruta para restaurador jefe
        elif empleado_actual.cargo == "Restaurador Jefe":# type: ignore
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
                    catalogo.mostrar_obras() #type: ignore
                    continue
                # Mostrar Restauraciones
                elif opcion_empleado_restauracion == "2":
                    mostrar_restauraciones(catalogo) #type: ignore
                    continue
                # Enviar obra a restauración
                elif opcion_empleado_restauracion == "3":
                    while True:
                        titulo_obra = input(
                            "\nIngrese el título de la obra a restaurar: "
                            )
                        obra_a_restaurar = catalogo.buscar_obra(titulo_obra)
                    
                        if obra_a_restaurar:
                            # Si ya esta en restauración, no se puede enviar de nuevo
                            if obra_a_restaurar.estado == "En restauración": # type: ignore
                                print(f"\nLa obra '{obra_a_restaurar.titulo}' ya está en restauración.")
                                break
                            # Ruta para enviar obra a restuarar
                            else:
                                tipo_restauracion = input(
                                "Ingrese el tipo de restauración: "
                                )
                                empleado_actual.enviar_a_restauracion(obra_a_restaurar, #type: ignore
                                                                    tipo_restauracion) 
                                print(f"\nObra '{obra_a_restaurar.titulo}' enviada a restauración.")
                                break
                        else:
                            print(f"\nObra '{titulo_obra}' no encontrada en exhibición.")
                            continue
                        
                # Marcar obra como restaurada
                elif opcion_empleado_restauracion == "4":
                    while True:
                        titulo_obra = input(
                            "\nIngrese el título de la obra a finalizar: "
                            )
                        obra_a_finalizar = catalogo.buscar_obra(titulo_obra)
                        
                        if obra_a_finalizar:
                            if obra_a_finalizar.estado == "En restauración": # type: ignore
                                empleado_actual.finalizar_restauracion(obra_a_finalizar) # type: ignore
                                print(f"\nLa restauracion de la obra '{obra_a_finalizar.titulo}' fue finalizada.") # type: ignore
                                break
                            else:
                                print(f"\nLa obra '{obra_a_finalizar.titulo}' no está en restauración.") # type: ignore
                                break
                        else:
                                print(f"\nObra '{titulo_obra}' no encontrada") # type: ignore
                                continue  
                else:
                    no_valido()
                    continue



        elif empleado_actual.cargo == "Director del Museo":
            pass # OJO PENDIENTE -----------
        
    elif opcion == "0":
        print("Saliendo.")
        break
    else:
        no_valido()
