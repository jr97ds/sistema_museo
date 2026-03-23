class Catalogo:
    def __init__(self, obras : list):
        self._obras = obras
    
    def mostrar_catalogo(self) -> None:
        for obra in self._obras:
            print(f"\n{obra}")
    
    def agregar_obra(self, obra) -> None:
        self._obras.append(obra)

class Salas:
    def __init__(self, nombre : str, obras : list):
        self._nombre = nombre
        self._obras = obras

class Pantalla: 
    def __init__(self,):
        pass