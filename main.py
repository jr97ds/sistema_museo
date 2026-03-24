from datetime import date
import Auth
from obras import Cuadro, Escultura, Otro
from catalogo import Catalogo, Pantalla, Sala
from tramites import MuseoExterno
from usuarios import Empleado, EncargadoCatalogo , RestauradorJefe , DirectorMuseo

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


# Datos precargados pantalla para demostración
pantalla = Pantalla(salas)



def mostrar_menu_principal() -> None:
    print("\nBienvenido")
    print("1. Ver Pantallas para visitantes")
    print("2. Sistema de Empleados")
    print("0. Salir")

def mostrar_menu_encargado_catalogo(catalogo: Catalogo, salas: list[Sala]) -> None:
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

def mostrar_menu_restaurador_jefe(empleado: RestauradorJefe, catalogo: Catalogo) -> None:
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
                    continue
                # Mostrar Restauraciones
                elif opcion_empleado_restauracion == "2":
                    mostrar_restauraciones(catalogo)
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
                            if obra_a_restaurar.estado == "En restauración":
                                print(f"\nLa obra '{obra_a_restaurar.titulo}' ya está en restauración.")
                                break
                            # Ruta para enviar obra a restuarar
                            else:
                                tipo_restauracion = input(
                                "Ingrese el tipo de restauración: "
                                )
                                empleado.enviar_a_restauracion(obra_a_restaurar, #type: ignore
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
                            if obra_a_finalizar.estado == "En restauración":
                                empleado.finalizar_restauracion(obra_a_finalizar) # type: ignore
                                print(f"\nLa restauracion de la obra '{obra_a_finalizar.titulo}' fue finalizada.")
                                break
                            else:
                                print(f"\nLa obra '{obra_a_finalizar.titulo}' no está en restauración.")
                                break
                        else:
                                print(f"\nObra '{titulo_obra}' no encontrada")
                                continue  
                        
                elif opcion_empleado_restauracion == "0":
                    Auth.logout()
                    print ("\nSesión cerrada.")
                    break   
                else:
                    no_valido()
                    continue

def mostrar_menu_director_museo(empleado: DirectorMuseo, catalogo: Catalogo, museos_externos: list[MuseoExterno]) -> None:
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
                    continue
                # Ver todas las cesiones
                elif opcion_empleado_director == "2":
                    mostrar_cesiones(catalogo)
                    continue
                #Crear nueva cesion
                elif opcion_empleado_director == "3":
                    while True:
                        input_titulo = input("\nIngrese el título de la obra para la cesión: ")
                        obra = catalogo.buscar_obra(input_titulo)
                        if not obra:
                            print(f"\nObra '{input_titulo}' no encontrada.")
                            continue
                        input_museo = input("\nIngrese el nombre del museo externo para la cesión: ")
                        for museo in museos_externos:
                            if museo.nombre.lower() == input_museo.lower():
                                museo_externo = museo
                                break
                        else:
                            print(f"\nMuseo externo '{input_museo}' no encontrado.")
                            continue

                        importe = int(input("\nIngrese el importe de la cesión: "))
                        duracion_dias = int(input("\nIngrese la duración de la cesión en días: "))
                        cesion = empleado.crear_cesion(obra, museo_externo, importe, duracion_dias) # type: ignore
                        print(f"\nCesión creada: {cesion}")
                        break

                elif opcion_empleado_director == "0":
                    Auth.logout() # type: ignore
                    print("\nSesión cerrada.")
                    break
                else:
                    no_valido()
                    continue

def no_valido() -> None:
    print("\nOpción no válida. Por favor, elija una opción válida.")
    
def seleccion_opcion() -> str:
    opcion = input("\nSeleccione una opción: ")
    return opcion

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
            continue

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
            sala = asignar_sala(salas)
            nuevo_cuadro = Cuadro(nombre, autor, periodo, valoracion, 
                                fecha_creacion, fecha_entrada, tecnica, estilo)
            sala.agregar_obra(nuevo_cuadro)
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
            sala = asignar_sala(salas)
            nueva_escultura = Escultura(nombre, autor, periodo, valoracion, 
                                        fecha_creacion, fecha_entrada, 
                                        material, estilo)
            sala.agregar_obra(nueva_escultura)
            return nueva_escultura
        
        elif tipo_obra == "3":
            nombre = input("Nombre de la obra: ")
            autor = input("Autor de la obra: ")
            periodo = input("Periodo de la obra: ")
            valoracion = int(input("Valor: "))
            fecha_creacion = date.fromisoformat(input(
                "Fecha de creación (YYYY-MM-DD): "))
            fecha_entrada = date.today() # Fecha actual
            sala = asignar_sala(salas)
            nueva_obra = Otro(nombre, autor, periodo, valoracion, 
                            fecha_creacion, fecha_entrada)
            sala.agregar_obra(nueva_obra)
            return nueva_obra
        else:
            no_valido()
            continue

def mostrar_restauraciones(catalogo: Catalogo) -> None:
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

def mostrar_cesiones(catalogo: Catalogo) -> None:
        encontradas = False
        for obra in catalogo.obras:
            if obra.cesiones:
                encontradas = True
                for cesion in obra.cesiones:
                    print(cesion)
        if not encontradas:
            print("\nNo hay obras en cesión.")

def verificar_cesiones_vencidas(catalogo: Catalogo) -> None:
    hoy = date.today()
    for obra in catalogo.obras:
        for cesion in obra.cesiones:
            if cesion.estado == "Aprobada" and cesion.fecha_fin < hoy:
                cesion.estado = "Finalizada"
                obra.estado = "En exhibición"
        for cesion_pendiente in obra.cesiones:
            if cesion_pendiente.estado == "Pendiente":
                cesion_pendiente.estado = "Aprobada"
                obra.estado = "En cesión"
# Restauracion si lleva 5 años sin restauracion, se hace de forma automatica
def restauraciones_automaticas(catalogo: Catalogo, restaurador_jefe: RestauradorJefe) -> None:
    hoy = date.today()
    for obra in catalogo.obras:
        if obra.estado == "En exhibición" and not obra.restauraciones:
            if (hoy - obra.fecha_entrada).days >= 5 * 365:
                restaurador_jefe.enviar_a_restauracion(obra, "Automática")
        elif obra.estado == "En exhibición" and obra.restauraciones:
                ultima_restauracion = obra.restauraciones[-1]
                if (hoy - ultima_restauracion.fecha_fin).days >= 5 * 365:
                    restaurador_jefe.enviar_a_restauracion(obra, "Automática")
# -------- INICIO DEL PROGRAMA --------

# Procesos Diarios
verificar_cesiones_vencidas(catalogo) 
restauraciones_automaticas(catalogo, restaurador_jefe)


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
        while not Auth.is_login:
            print("\nInicie sesion para continuar")
            input_usuario = input("Usuario: ")
            input_contraseña = input("Contraseña: ")    
            # Intento de inicio de sesion
            if not Auth.is_login(input_usuario, input_contraseña):
                print("\nCredenciales incorrectas. Intente de nuevo.")
                continue
        # Saludo si login es exitoso
        print(f"\nBienvenido {Auth.empleado_actual.cargo} -" 
              f"{Auth.empleado_actual.nombre_completo}") 
                

        # Ruta para encargado del catalogo
        if empleado_actual.cargo == "Encargado del Catálogo": #type: ignore
            mostrar_menu_encargado_catalogo(catalogo, salas)

        # Ruta para restaurador jefe
        elif empleado_actual.cargo == "Restaurador Jefe": # type: ignore
              mostrar_menu_restaurador_jefe(empleado_actual, catalogo) # type: ignore

        elif empleado_actual.cargo == "Director del Museo": # type: ignore
             mostrar_menu_director_museo(empleado_actual, catalogo, museos_externos) # type: ignore
           
        
    elif opcion == "0":
        print("Saliendo.")
        break
    else:
        no_valido()
