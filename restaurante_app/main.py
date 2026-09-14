import tkinter as tk
from pathlib import Path

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

RUTA_DATOS = Path(__file__).resolve().parent / "datos"


class RestauranteApp:
    """Controla una única ventana y el cambio entre LoginView y MainView."""

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Restaurante App - Semana 13")
        self.root.geometry("900x560")
        self.root.minsize(800, 500)

        archivos = ArchivoServicio(RUTA_DATOS)
        productos = archivos.cargar_productos()
        usuarios = archivos.cargar_usuarios()
        self.servicio = RestauranteServicio(productos, usuarios)

        self.vista_actual = None
        self.mostrar_login()

    def _cambiar_vista(self, nueva_vista) -> None:
        if self.vista_actual is not None:
            self.vista_actual.destroy()
        self.vista_actual = nueva_vista
        self.vista_actual.pack(fill="both", expand=True)

    def mostrar_login(self) -> None:
        vista = LoginView(self.root, self.servicio, self.mostrar_principal)
        self._cambiar_vista(vista)

    def mostrar_principal(self, usuario) -> None:
        vista = MainView(self.root, self.servicio, usuario, self.mostrar_login)
        self._cambiar_vista(vista)

    def ejecutar(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    RestauranteApp().ejecutar()
