from typing import Optional
from usuarios import Empleado

class Auth:
    """Clase para manejar la autenticación de 
    empleados en el sistema del museo"""
    def __init__(self, empleados):
        self._empleados = empleados
        self._empleado_actual: Optional[Empleado] = None

    @property
    def is_login(self) -> bool:
        return self._empleado_actual is not None
    
    @property
    def empleado_actual(self) -> Optional[Empleado]:
        return self._empleado_actual
    
    def login(self, usuario: str, contraseña: str) -> bool:
        """Verifica las credenciales del empleado y 
        establece el empleado actual si son correctas"""
        for empleado in self._empleados:
            if empleado.verificar_credenciales(usuario, contraseña):
                self._empleado_actual = empleado
                return True
        return False 

    def cerrar_sesion(self) -> None:
        """Cierra la sesión del empleado actual"""
        self._empleado_actual = None