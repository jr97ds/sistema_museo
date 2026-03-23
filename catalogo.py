class Catalogo:
    def __init__(self, obras : list):
        self._obras = obras
    
    @property
    def obras(self):
        return self._obras
    
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
    
    def calcular_valor_total(self) -> int:
        total = 0
        for obra in self._obras:
            total += obra.valor 
        return total
    
class Salas:
    def __init__(self, nombre : str, obras : list):
        self._nombre = nombre
        self._obras = obras

class Pantalla: 
    def __init__(self,):
        pass