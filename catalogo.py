from obras import Obra


class Catalogo:
    """Clase para representar el catálogo del museo, 
    que contiene una lista de obras."""
    def __init__(self, obras: list[Obra]):
        self._obras = obras

    @property
    def obras(self):
        return self._obras

    def mostrar_obras(self) -> None:
        for obra in self._obras:
            print(f"\n{obra}")

    def agregar_obra(self, obra: Obra) -> None:
        self._obras.append(obra)

    def buscar_obra(self, titulo: str):
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
    """Clase para representar una sala del museo, que contiene obras."""
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._obras = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def obras(self):
        return self._obras

    def agregar_obra(self, obra: Obra) -> None:
        self._obras.append(obra)

    # Muestra solo obras que están en exhibición
    def mostrar_obras(self) -> None:
        print(f"\n Sala '{self._nombre}':")
        # Hacer lista de obras en exhibición
        obras_exhibidas = [
            obra for obra in self._obras
            if obra.estado == "En exhibición"
        ]
        # Mostrar obras en exhibición o mensaje si no hay ninguna
        if obras_exhibidas:
            for obra in obras_exhibidas:
                print(obra)
        else:
            print("No hay obras en exhibición en esta sala.")


class Pantalla: 
    """Clase para representar una pantalla que 
    muestra las obras en exhibición."""
    def __init__(self,salas: list[Sala]):
        self._salas = salas
    
    def mostrar_salas(self) -> None:
        for sala in self._salas:
            sala.mostrar_obras()