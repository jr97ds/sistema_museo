class Catalogo:
    def __init__(self, obras : list):
        self._obras = obras
    
    def mostrar_obras(self) -> None:
        for obra in self._obras:
            print(f"\n{obra}")
    
    def agregar_obra(self, obra) -> None:
        self._obras.append(obra)
    
    def mostrar_restauraciones(self) -> None:
        encontradas = False
        for obra in self._obras:
            if obra.restauracion is not None:
                encontradas = True
                for restauracion in obra.restauracion:
                    print(restauracion)
        if not encontradas:
            print("\nNo hay obras en restauración.")

class Salas:
    def __init__(self, nombre : str, obras : list):
        self._nombre = nombre
        self._obras = obras

class Pantalla: 
    def __init__(self,):
        pass