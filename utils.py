def seleccion_opcion() -> str:
    opcion = input("\nSeleccione una opción: ")
    return opcion

def no_valido() -> None:
    print("\nOpción no válida. Por favor, elija una opción válida.")