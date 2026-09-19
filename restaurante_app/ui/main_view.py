import tkinter as tk
from tkinter import messagebox, ttk

from modelos.usuario import Usuario
from servicios.restaurante_servicio import RestauranteServicio


class MainView(ttk.Frame):
    """Panel principal con navegación, formularios y visualización de registros."""

    def __init__(self, master: tk.Misc, servicio: RestauranteServicio, usuario_actual: Usuario, on_logout) -> None:
        super().__init__(master, padding=18)
        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.on_logout = on_logout
        self.codigo_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.categoria_var = tk.StringVar()
        self.precio_var = tk.StringVar()
        self.stock_var = tk.StringVar()
        self.estado_var = tk.StringVar()
        self._crear_componentes()
        self._mostrar_inicio()

    def _crear_componentes(self) -> None:
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        encabezado = ttk.Frame(self)
        encabezado.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 14))
        encabezado.columnconfigure(0, weight=1)
        ttk.Label(encabezado, text="RESTAURANTE APP", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, sticky="w")
        ttk.Label(encabezado, text=f"Usuario: {self.usuario_actual.nombre}").grid(row=1, column=0, sticky="w", pady=(3, 0))
        ttk.Button(encabezado, text="Cerrar sesión", command=self.on_logout).grid(row=0, column=1, rowspan=2, padx=(12, 0))

        menu = ttk.LabelFrame(self, text="Navegación", padding=10)
        menu.grid(row=1, column=0, sticky="ns", padx=(0, 15))
        for texto, comando in [
            ("Inicio", self._mostrar_inicio),
            ("Productos", self._mostrar_productos),
            ("Usuarios", self._mostrar_usuarios),
            ("Ventas", self._mostrar_ventas),
        ]:
            ttk.Button(menu, text=texto, width=20, command=comando).pack(pady=5)

        self.contenido = ttk.Frame(self)
        self.contenido.grid(row=1, column=1, sticky="nsew")
        self.contenido.columnconfigure(0, weight=1)
        self.contenido.rowconfigure(1, weight=1)

    def _limpiar_contenido(self) -> None:
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def _mostrar_inicio(self) -> None:
        self._limpiar_contenido()
        ttk.Label(self.contenido, text="Resumen del sistema", font=("Segoe UI", 15, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 15))
        tarjeta = ttk.LabelFrame(self.contenido, text="Estado actual", padding=18)
        tarjeta.grid(row=1, column=0, sticky="nw")
        ttk.Label(tarjeta, text=f"Productos registrados: {self.servicio.cantidad_productos()}").grid(row=0, column=0, sticky="w", pady=5)
        ttk.Label(tarjeta, text=f"Usuarios registrados: {self.servicio.cantidad_usuarios()}").grid(row=1, column=0, sticky="w", pady=5)
        ttk.Label(tarjeta, text="Semana 14: componentes y contenedores de Tkinter").grid(row=2, column=0, sticky="w", pady=(12, 5))

    def _mostrar_productos(self) -> None:
        self._limpiar_contenido()
        self.contenido.rowconfigure(1, weight=0)
        ttk.Label(self.contenido, text="Gestión de productos", font=("Segoe UI", 15, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 10))

        formulario = ttk.LabelFrame(self.contenido, text="Datos del producto", padding=12)
        formulario.grid(row=1, column=0, sticky="ew", pady=(0, 12))
        for col in range(4):
            formulario.columnconfigure(col, weight=1)

        campos = [
            ("Código", self.codigo_var, 0, 0),
            ("Nombre", self.nombre_var, 0, 2),
            ("Categoría", self.categoria_var, 1, 0),
            ("Precio", self.precio_var, 1, 2),
            ("Stock", self.stock_var, 2, 0),
        ]
        for texto, variable, fila, col in campos:
            ttk.Label(formulario, text=texto + ":").grid(row=fila, column=col, sticky="e", padx=5, pady=5)
            ttk.Entry(formulario, textvariable=variable, width=24).grid(row=fila, column=col + 1, sticky="ew", padx=5, pady=5)

        acciones = ttk.Frame(formulario)
        acciones.grid(row=3, column=0, columnspan=4, pady=(8, 2))
        ttk.Button(acciones, text="Registrar", command=self._registrar_producto).pack(side="left", padx=4)
        ttk.Button(acciones, text="Cargar / Consultar", command=self._cargar_producto).pack(side="left", padx=4)
        ttk.Button(acciones, text="Actualizar", command=self._actualizar_producto).pack(side="left", padx=4)
        ttk.Button(acciones, text="Eliminar", command=self._eliminar_producto).pack(side="left", padx=4)
        ttk.Button(acciones, text="Limpiar", command=self._limpiar_formulario).pack(side="left", padx=4)

        ttk.Label(self.contenido, textvariable=self.estado_var).grid(row=2, column=0, sticky="w", pady=(0, 8))

        tabla_frame = ttk.LabelFrame(self.contenido, text="Productos registrados", padding=8)
        tabla_frame.grid(row=3, column=0, sticky="nsew")
        self.contenido.rowconfigure(3, weight=1)
        tabla_frame.columnconfigure(0, weight=1)
        tabla_frame.rowconfigure(0, weight=1)

        columnas = ("codigo", "nombre", "categoria", "precio", "stock")
        self.tabla_productos = ttk.Treeview(tabla_frame, columns=columnas, show="headings", height=12)
        titulos = {"codigo": "Código", "nombre": "Nombre", "categoria": "Categoría", "precio": "Precio", "stock": "Stock"}
        anchos = {"codigo": 90, "nombre": 220, "categoria": 150, "precio": 100, "stock": 90}
        for columna in columnas:
            self.tabla_productos.heading(columna, text=titulos[columna])
            self.tabla_productos.column(columna, width=anchos[columna], anchor="center")
        self.tabla_productos.column("nombre", anchor="w")
        self.tabla_productos.grid(row=0, column=0, sticky="nsew")
        scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tabla_productos.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.tabla_productos.configure(yscrollcommand=scrollbar.set)
        self._refrescar_tabla_productos()

    def _refrescar_tabla_productos(self) -> None:
        if not hasattr(self, "tabla_productos"):
            return
        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)
        for producto in self.servicio.listar_productos():
            self.tabla_productos.insert("", "end", values=(producto.codigo, producto.nombre, producto.categoria, f"${producto.precio:.2f}", producto.stock))

    def _obtener_datos_formulario(self) -> tuple[str, str, str, float, int]:
        codigo = self.codigo_var.get().strip()
        nombre = self.nombre_var.get().strip()
        categoria = self.categoria_var.get().strip()
        try:
            precio = float(self.precio_var.get().strip())
            stock = int(self.stock_var.get().strip())
        except ValueError as exc:
            raise ValueError("Precio debe ser numérico y stock debe ser un entero.") from exc
        return codigo, nombre, categoria, precio, stock

    def _registrar_producto(self) -> None:
        try:
            datos = self._obtener_datos_formulario()
            self.servicio.registrar_producto(*datos)
            self.estado_var.set("Producto registrado correctamente.")
            self._refrescar_tabla_productos()
            self._limpiar_formulario()
        except ValueError as exc:
            messagebox.showerror("No se pudo registrar", str(exc))

    def _cargar_producto(self) -> None:
        producto = self.servicio.buscar_producto(self.codigo_var.get())
        if producto is None:
            messagebox.showerror("Consulta", "No existe un producto con ese código.")
            return
        self.nombre_var.set(producto.nombre)
        self.categoria_var.set(producto.categoria)
        self.precio_var.set(str(producto.precio))
        self.stock_var.set(str(producto.stock))
        self.estado_var.set("Producto cargado correctamente.")

    def _actualizar_producto(self) -> None:
        try:
            datos = self._obtener_datos_formulario()
            self.servicio.actualizar_producto(*datos)
            self.estado_var.set("Producto actualizado correctamente.")
            self._refrescar_tabla_productos()
        except ValueError as exc:
            messagebox.showerror("No se pudo actualizar", str(exc))

    def _eliminar_producto(self) -> None:
        codigo = self.codigo_var.get().strip()
        if not codigo:
            messagebox.showerror("Eliminar", "Ingrese el código del producto.")
            return
        producto = self.servicio.buscar_producto(codigo)
        if producto is None:
            messagebox.showerror("Eliminar", "No existe un producto con ese código.")
            return
        if not messagebox.askyesno("Confirmar eliminación", f"¿Desea eliminar '{producto.nombre}'?"):
            return
        try:
            self.servicio.eliminar_producto(codigo)
            self.estado_var.set("Producto eliminado correctamente.")
            self._limpiar_formulario()
            self._refrescar_tabla_productos()
        except ValueError as exc:
            messagebox.showerror("No se pudo eliminar", str(exc))

    def _limpiar_formulario(self) -> None:
        self.codigo_var.set("")
        self.nombre_var.set("")
        self.categoria_var.set("")
        self.precio_var.set("")
        self.stock_var.set("")

    def _mostrar_usuarios(self) -> None:
        self._limpiar_contenido()
        self.contenido.rowconfigure(1, weight=1)
        ttk.Label(self.contenido, text="Usuarios registrados", font=("Segoe UI", 15, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 10))
        tabla_frame = ttk.LabelFrame(self.contenido, text="Consulta de usuarios", padding=8)
        tabla_frame.grid(row=1, column=0, sticky="nsew")
        tabla_frame.columnconfigure(0, weight=1)
        tabla_frame.rowconfigure(0, weight=1)
        columnas = ("identificacion", "nombre", "correo")
        tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings")
        for columna, titulo in {"identificacion": "Identificación", "nombre": "Nombre", "correo": "Correo"}.items():
            tabla.heading(columna, text=titulo)
            tabla.column(columna, width=220, anchor="center")
        tabla.grid(row=0, column=0, sticky="nsew")
        for usuario in self.servicio.listar_usuarios():
            tabla.insert("", "end", values=(usuario.identificacion, usuario.nombre, usuario.correo))

    def _mostrar_ventas(self) -> None:
        self._limpiar_contenido()
        ttk.Label(self.contenido, text="Ventas", font=("Segoe UI", 15, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 10))
        ttk.Label(self.contenido, text="La funcionalidad de ventas permanece pendiente para una siguiente etapa.", wraplength=650, justify="left").grid(row=1, column=0, sticky="nw")
