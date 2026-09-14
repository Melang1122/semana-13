import tkinter as tk
from tkinter import ttk

from servicios.restaurante_servicio import RestauranteServicio


class LoginView(ttk.Frame):
    """Pantalla de acceso simulado al sistema."""

    def __init__(self, master: tk.Misc, servicio: RestauranteServicio, on_login) -> None:
        super().__init__(master, padding=30)
        self.servicio = servicio
        self.on_login = on_login
        self.usuario_var = tk.StringVar()
        self.contrasena_var = tk.StringVar()
        self.mensaje_var = tk.StringVar()
        self._crear_componentes()

    def _crear_componentes(self) -> None:
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        ttk.Label(
            self,
            text="RESTAURANTE APP",
            font=("Segoe UI", 20, "bold"),
        ).grid(row=0, column=0, columnspan=2, pady=(20, 8))

        ttk.Label(
            self,
            text="Inicio de sesión",
            font=("Segoe UI", 12),
        ).grid(row=1, column=0, columnspan=2, pady=(0, 25))

        ttk.Label(self, text="Usuario:").grid(row=2, column=0, sticky="e", padx=8, pady=8)
        entrada_usuario = ttk.Entry(self, textvariable=self.usuario_var, width=30)
        entrada_usuario.grid(row=2, column=1, sticky="w", padx=8, pady=8)

        ttk.Label(self, text="Contraseña:").grid(row=3, column=0, sticky="e", padx=8, pady=8)
        entrada_contrasena = ttk.Entry(
            self, textvariable=self.contrasena_var, width=30, show="*"
        )
        entrada_contrasena.grid(row=3, column=1, sticky="w", padx=8, pady=8)

        ttk.Button(self, text="Ingresar", command=self._ingresar).grid(
            row=4, column=0, columnspan=2, pady=18
        )

        ttk.Label(
            self,
            textvariable=self.mensaje_var,
            foreground="red",
        ).grid(row=5, column=0, columnspan=2, pady=5)

        ttk.Label(
            self,
            text="Puede usar su identificación o correo como usuario.",
            font=("Segoe UI", 9),
        ).grid(row=6, column=0, columnspan=2, pady=(15, 0))

        entrada_usuario.focus()
        entrada_usuario.bind("<Return>", lambda _: entrada_contrasena.focus())
        entrada_contrasena.bind("<Return>", lambda _: self._ingresar())

    def _ingresar(self) -> None:
        usuario = self.usuario_var.get().strip()
        contrasena = self.contrasena_var.get().strip()

        if not usuario or not contrasena:
            self.mensaje_var.set("Complete usuario y contraseña.")
            return

        usuario_validado = self.servicio.validar_acceso(usuario, contrasena)
        if usuario_validado is None:
            self.mensaje_var.set("Usuario o contraseña incorrectos.")
            return

        self.mensaje_var.set("")
        self.on_login(usuario_validado)
