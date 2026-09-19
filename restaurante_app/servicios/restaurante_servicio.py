from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Concentra las reglas y operaciones de negocio del restaurante."""

    def __init__(self, productos: list[Producto], usuarios: list[Usuario], archivos: ArchivoServicio | None = None) -> None:
        self._productos = list(productos)
        self._usuarios = list(usuarios)
        self._archivos = archivos

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

    def buscar_producto(self, codigo: str) -> Producto | None:
        codigo = str(codigo).strip()
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def registrar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> Producto:
        if self.buscar_producto(codigo) is not None:
            raise ValueError("Ya existe un producto con ese código.")
        producto = Producto(codigo, nombre, categoria, precio, stock)
        self._productos.append(producto)
        self._guardar_productos()
        return producto

    def actualizar_producto(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int) -> Producto:
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError("No existe un producto con ese código.")
        producto.actualizar(nombre, categoria, precio, stock)
        self._guardar_productos()
        return producto

    def eliminar_producto(self, codigo: str) -> None:
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError("No existe un producto con ese código.")
        self._productos.remove(producto)
        self._guardar_productos()

    def _guardar_productos(self) -> None:
        if self._archivos is not None:
            self._archivos.guardar_productos(self._productos)
