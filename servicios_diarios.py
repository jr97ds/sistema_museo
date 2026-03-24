from abc import ABC, abstractmethod
from datetime import date
from catalogo import Catalogo
from usuarios import RestauradorJefe


class ServicioDiario(ABC):
    """Clase para representar los servicios diarios del museo"""

    @abstractmethod
    def ejecutar(self, catalogo):
        """Método abstracto para ejecutar el servicio diario"""
        pass

class VerificarCesionesVencidas(ServicioDiario):
    """Servicio diario para verificar cesiones vencidas y actualizar estados"""
    def ejecutar(self, catalogo):
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

class RestauracionesAutomaticas(ServicioDiario):

    def ejecutar(self, catalogo: Catalogo, restaurador_jefe: RestauradorJefe) -> None:
        hoy = date.today()
        for obra in catalogo.obras:
            if obra.estado == "En exhibición" and not obra.restauraciones:
                if (hoy - obra.fecha_entrada).days >= 5 * 365:
                    restaurador_jefe.enviar_a_restauracion(obra, "Automática")
            elif obra.estado == "En exhibición" and obra.restauraciones:
                    ultima_restauracion = obra.restauraciones[-1]
                    if (hoy - ultima_restauracion.fecha_fin).days >= 5 * 365:
                        restaurador_jefe.enviar_a_restauracion(obra, 
                                                               "Automática")