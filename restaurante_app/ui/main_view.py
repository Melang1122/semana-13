import tkinter as tk
from tkinter import ttk

from modelos.usuario import Usuario
from servicios.restaurante_servicio import RestauranteServicio


class MainView(ttk.Frame):
    """Panel principal desde el cual se consultan usuarios y productos."""

    def __init__(
        self,
        master: tk.Misc,
        servicio: RestauranteServicio,
        usuario_actual: Usuario,
        on_logout,
    ) -> None:
        super().__init__(master, padding=20)
        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.on_logout = on_logout
        self._crear_componentes()
        self._mostrar_inicio()

    def _crear_componentes(self) -> None:
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        encabezado = ttk.Frame(self)
        encabezado.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 15))
        encabezado.columnconfigure(0, weight=1)

        ttk.Label(
            encabezado,
            text="Panel principal - Restaurante App",
            font=("Segoe UI", 17, "bold"),
        ).grid(row=0, column=0, sticky="w")

        ttk.Label(
            encabezado,
            text=f"Bienvenido: {self.usuario_actual.nombre}",
        ).grid(row=1, column=0, sticky="w", pady=(4, 0))

        ttk.Button(encabezado, text="Cerrar sesión", command=self.on_logout).grid(
            row=0, column=1, rowspan=2, padx=(15, 0)
        )

        menu = ttk.LabelFrame(self, text="Opciones", padding=10)
        menu.grid(row=1, column=0, sticky="ns", padx=(0, 15))

        ttk.Button(menu, text="Inicio", width=20, command=self._mostrar_inicio).pack(pady=5)
        ttk.Button(menu, text="Productos", width=20, command=self._mostrar_productos).pack(pady=5)
        ttk.Button(menu, text="Usuarios", width=20, command=self._mostrar_usuarios).pack(pady=5)
        ttk.Button(menu, text="Ventas (pendiente)", width=20, command=self._mostrar_ventas).pack(pady=5)

        self.contenido = ttk.Frame(self)
        self.contenido.grid(row=1, column=1, sticky="nsew")
        self.contenido.columnconfigure(0, weight=1)
        self.contenido.rowconfigure(1, weight=1)

    def _limpiar_contenido(self) -> None:
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def _mostrar_inicio(self) -> None:
        self._limpiar_contenido()
        ttk.Label(
            self.contenido,
            text="Resumen del sistema",
            font=("Segoe UI", 15, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 15))

        resumen = (
            f"Productos registrados: {self.servicio.cantidad_productos()}\n"
            f"Usuarios registrados: {self.servicio.cantidad_usuarios()}\n\n"
            "Ventas: funcionalidad pendiente para una siguiente etapa."
        )
        ttk.Label(self.contenido, text=resumen, justify="left").grid(
            row=1, column=0, sticky="nw"
        )

    def _mostrar_productos(self) -> None:
        self._limpiar_contenido()
        ttk.Label(
            self.contenido,
            text="Productos registrados",
            font=("Segoe UI", 15, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 10))

        columnas = ("codigo", "nombre", "categoria", "precio", "stock")
        tabla = ttk.Treeview(self.contenido, columns=columnas, show="headings", height=15)
        titulos = {
            "codigo": "Código",
            "nombre": "Nombre",
            "categoria": "Categoría",
            "precio": "Precio",
            "stock": "Stock",
        }
        for columna in columnas:
            tabla.heading(columna, text=titulos[columna])
            tabla.column(columna, width=120, anchor="center")

        tabla.column("nombre", width=190, anchor="w")
        tabla.grid(row=1, column=0, sticky="nsew")

        for producto in self.servicio.listar_productos():
            tabla.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    f"${producto.precio:.2f}",
                    producto.stock,
                ),
            )

    def _mostrar_usuarios(self) -> None:
        self._limpiar_contenido()
        ttk.Label(
            self.contenido,
            text="Usuarios registrados",
            font=("Segoe UI", 15, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 10))

        columnas = ("identificacion", "nombre", "correo")
        tabla = ttk.Treeview(self.contenido, columns=columnas, show="headings", height=15)
        titulos = {
            "identificacion": "Identificación",
            "nombre": "Nombre",
            "correo": "Correo",
        }
        for columna in columnas:
            tabla.heading(columna, text=titulos[columna])
            tabla.column(columna, width=190, anchor="center")
        tabla.column("nombre", width=220, anchor="w")
        tabla.column("correo", width=260, anchor="w")
        tabla.grid(row=1, column=0, sticky="nsew")

        for usuario in self.servicio.listar_usuarios():
            tabla.insert(
                "",
                "end",
                values=(usuario.identificacion, usuario.nombre, usuario.correo),
            )

    def _mostrar_ventas(self) -> None:
        self._limpiar_contenido()
        ttk.Label(
            self.contenido,
            text="Ventas",
            font=("Segoe UI", 15, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 10))
        ttk.Label(
            self.contenido,
            text=(
                "Esta funcionalidad se encuentra pendiente y será incorporada "
                "en las siguientes etapas del proyecto."
            ),
            wraplength=550,
            justify="left",
        ).grid(row=1, column=0, sticky="nw")
