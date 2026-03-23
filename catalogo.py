class Catalogo:
    def __init__(self, obras : list):
        self._obras = obras
    
    def mostrar_obras(self) -> None:
        for obra in self._obras:
            print(f"\n{obra}")
    
    def agregar_obra(self, obra) -> None:
        self._obras.append(obra)

    def buscar_obra(self, titulo : str):
        for obra in self._obras:
            if obra.titulo.lower() == titulo.lower():
                return obra
        return None
    
class Salas:
    def __init__(self, nombre : str, obras : list):
        self._nombre = nombre
        self._obras = obras

class Pantalla: 
    def __init__(self,):
        pass