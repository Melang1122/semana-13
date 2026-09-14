import json
from pathlib import Path
from typing import Any, Callable, TypeVar

from modelos.producto import Producto
from modelos.usuario import Usuario

T = TypeVar("T")


class ArchivoServicio:
    """Centraliza la lectura de los archivos JSON usados por la aplicación."""

    def __init__(self, directorio_datos: str | Path) -> None:
        self.directorio_datos = Path(directorio_datos)
        self.ruta_productos = self.directorio_datos / "productos.json"
        self.ruta_usuarios = self.directorio_datos / "usuarios.json"

    def _cargar(
        self,
        ruta: Path,
        constructor: Callable[[dict[str, Any]], T],
    ) -> list[T]:
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                registros = json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError, PermissionError):
            return []

        if not isinstance(registros, list):
            return []

        objetos: list[T] = []
        for registro in registros:
            if not isinstance(registro, dict):
                continue
            try:
                objetos.append(constructor(registro))
            except (KeyError, ValueError, TypeError):
                continue
        return objetos

    def cargar_productos(self) -> list[Producto]:
        return self._cargar(
            self.ruta_productos,
            lambda r: Producto(
                r["codigo"], r["nombre"], r["categoria"], r["precio"], r["stock"]
            ),
        )

    def cargar_usuarios(self) -> list[Usuario]:
        return self._cargar(
            self.ruta_usuarios,
            lambda r: Usuario(
                r["identificacion"], r["nombre"], r["correo"], r["contrasena"]
            ),
        )
