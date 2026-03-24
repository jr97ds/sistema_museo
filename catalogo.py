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
    
class Sala:
    def __init__(self, nombre : str):
        self._nombre = nombre
        self._obras = []
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def obras(self):
        return self._obras
    
    def agregar_obra(self, obra) -> None:
        self._obras.append(obra)
    
    def mostrar_obras(self) -> None:
        print(f"\n Sala '{self._nombre}':")
        if self._obras:
            for obra in self._obras:
                if obra.estado == "En exhibición":
                    print(obra)
        else:
            print("No hay obras en esta sala.")
            return
       


class Pantalla: 
    def __init__(self,salas : list):
        self._salas = salas
    
    def mostrar_salas(self) -> None:
        for sala in self._salas:
            sala.mostrar_obras()