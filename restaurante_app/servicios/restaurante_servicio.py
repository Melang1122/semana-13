from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:
    """Gestiona las operaciones de consulta y acceso de la interfaz gráfica."""

    def __init__(self, productos: list[Producto], usuarios: list[Usuario]) -> None:
        self._productos = list(productos)
        self._usuarios = list(usuarios)

    def validar_acceso(self, usuario: str, contrasena: str) -> Usuario | None:
        usuario = usuario.strip().lower()
        contrasena = contrasena.strip()

        if not usuario or not contrasena:
            return None

        for registrado in self._usuarios:
            coincide_usuario = (
                registrado.identificacion == usuario
                or registrado.correo.lower() == usuario
            )
            if coincide_usuario and registrado.contrasena == contrasena:
                return registrado
        return None

    def listar_productos(self) -> list[Producto]:
        return self._productos.copy()

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios.copy()

    def cantidad_productos(self) -> int:
        return len(self._productos)

    def cantidad_usuarios(self) -> int:
        return len(self._usuarios)
