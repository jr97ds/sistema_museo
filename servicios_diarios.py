from abc import ABC, abstractmethod
from datetime import date, timedelta
from catalogo import Catalogo
from usuarios import RestauradorJefe


class ServicioDiario(ABC):
    """Clase para representar los servicios diarios del museo"""

    @abstractmethod
    def ejecutar(self, catalogo):
        """Método abstracto para ejecutar el servicio diario"""
        pass


class VerificarCesiones(ServicioDiario):
    """Servicio diario para verificar cesiones vencidas y actualizar estados"""
    def ejecutar(self, catalogo):
        # Verificacion de cesiones vencidas y con cola
        hoy = date.today()
        # Finalizar cesion vencida y poner obra en exhibicion
        for obra in catalogo.obras:
            for cesion in obra.cesiones:
                if cesion.estado == "Aprobada" and cesion.fecha_fin < hoy:
                    cesion.estado = "Finalizada"
                    obra.estado = "En exhibición"
            # Aprobar cesion pendiente si obra  en exhibicion y cesion pendiente
            if obra.estado == "En exhibición":
                for cesion_pendiente in obra.cesiones:
                    if cesion_pendiente.estado == "Pendiente":
                        cesion_pendiente.estado = "Aprobada"
                        obra.estado = "En cesión"
                        cesion_pendiente.fecha_inicio = hoy
                        cesion_pendiente.fecha_fin = hoy + timedelta(
                            days=cesion_pendiente._duracion_dias
                            )
                        break


class RestauracionesAutomaticas(ServicioDiario):

    def ejecutar(self, catalogo: Catalogo, 
                 restaurador_jefe: RestauradorJefe) -> None:
        hoy = date.today()
        # Si nunca se ha restaurado y lleva 5 años en exhibicion
        for obra in catalogo.obras:
            if obra.estado == "En exhibición" and not obra.restauraciones:
                if (hoy - obra.fecha_entrada).days >= 5 * 365:
                    restaurador_jefe.enviar_a_restauracion(obra, "Automática")
            # Si se ha restaurado, pero la ultima restauracion fue hace 5 años
            elif obra.estado == "En exhibición" and obra.restauraciones:
                restauraciones_finalizadas = [
                r for r in obra.restauraciones if r.estado == "Finalizada" 
                ]
                ultima_restauracion = restauraciones_finalizadas[-1]
                if (hoy - ultima_restauracion.fecha_fin).days >= 5 * 365:
                    restaurador_jefe.enviar_a_restauracion(obra, 
                                                            "Automática")