
from usuarios import EncargadoCatalogo , RestauradorJefe , DirectorMuseo

login = False # Controla el estado de inicio de sesión
encargado_catalogo = EncargadoCatalogo("Andres", "Gomez", "catalogo", "1234")
restaurador_jefe = RestauradorJefe("Maria", "Lopez", "restaurador", "1234")
director_museo = DirectorMuseo("Carlos", "Perez", "director", "1234")
empleados = [encargado_catalogo, restaurador_jefe, director_museo]

def mostrar_menu_principal() -> None:
    print("Bienvenido")
    print("1. Soy un visitante")
    print("2. Soy un empleado")
    print("0. Salir")

def no_valido() -> None:
    print("Opción no válida. Por favor, elija una opción válida.")

def log_in() -> tuple[EncargadoCatalogo | RestauradorJefe | 
                      DirectorMuseo | None, bool]: # type: ignore
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    for empleado in empleados:
        if empleado.usuario == usuario and empleado.contraseña == contraseña:
            print(f"Bienvenido {empleado.cargo} - {empleado.nombre_completo}")
            return empleado,True # type: ignore
    print("Nombre de usuario o contraseña incorrectos.")
    return None, False # type: ignore

def log_out() -> bool:
    login = False
    print("Sesión cerrada. ¡Hasta luego!")
    return login
    
def seleccion_opccion() -> str:
    opcion = input("Seleccione una opción: ")
    return opcion



# -------- INICIO DEL PROGRAMA --------
mostrar_menu_principal()
# Logica de seleccion de visitante/Empleado
while True:
    opcion = seleccion_opccion()
    
    if opcion == "1":
        print("Bienvenido Visitante")

        # OJO PENDIENTE -----------


    elif opcion == "2":
        print("Inicie sesion para continuar")
        while not login:
            empleado_actual , login = log_in()

        if empleado_actual.cargo == "Encargado del Catálogo":
            pass # OJO PENDIENTE -----------
        elif empleado_actual.cargo == "Restaurador Jefe":
            pass # OJO PENDIENTE -----------
        elif empleado_actual.cargo == "Director del Museo":
            pass # OJO PENDIENTE -----------
        
    elif opcion == "0":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        no_valido()
