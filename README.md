# Restaurante App — Semana 14

## Descripción

Proyecto de Programación Orientada a Objetos correspondiente a la Semana 14, centrada en **componentes y contenedores**. Esta versión evoluciona la interfaz gráfica de `restaurante_app` desarrollada en la semana anterior, manteniendo la arquitectura modular, la persistencia mediante archivos JSON y la separación de responsabilidades.

## Objetivo de la evolución

La interfaz fue reorganizada para ofrecer una experiencia más clara y ordenada. Se incorporaron contenedores para separar navegación, formularios, acciones y visualización de información. La sección de productos permite realizar operaciones sencillas desde la interfaz gráfica.

## Funcionalidades implementadas

- Inicio de sesión mediante `LoginView`.
- Validación de credenciales mediante `RestauranteServicio`.
- Panel principal mediante `MainView`.
- Navegación por Inicio, Productos, Usuarios y Ventas.
- Consulta de usuarios registrados.
- Gestión de productos mediante:
  - Registrar.
  - Cargar / Consultar por código.
  - Actualizar.
  - Eliminar.
  - Limpiar formulario.
- Tabla `Treeview` para mostrar productos.
- Barra de desplazamiento para la tabla de productos.
- Mensajes de confirmación y error mediante cuadros de diálogo.
- Persistencia de productos en `datos/productos.json`.
- Actualización de la información visual después de cada operación.

## Componentes y contenedores utilizados

La interfaz utiliza componentes de **Tkinter/ttk**, entre ellos `Frame`, `LabelFrame`, `Label`, `Entry`, `Button`, `Treeview` y `Scrollbar`.

Los contenedores permiten separar jerárquicamente la ventana principal, el encabezado, el menú de navegación, el formulario de productos, el área de acciones y la tabla de registros.

Se utilizaron principalmente los gestores de geometría `grid()` y `pack()` de acuerdo con la función de cada zona de la interfaz.

Los botones ejecutan sus acciones mediante `command=` y las reglas del negocio permanecen en `RestauranteServicio`.

## Arquitectura

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
└── main.py
```

## Separación de responsabilidades

- **Producto:** representa los datos y validaciones propias de un producto.
- **Usuario:** representa los usuarios utilizados para el acceso.
- **ArchivoServicio:** centraliza la lectura de JSON y la escritura de `productos.json`.
- **RestauranteServicio:** concentra validaciones y operaciones de negocio sobre productos y usuarios.
- **LoginView:** administra la presentación y captura de credenciales.
- **MainView:** coordina la interacción gráfica, formularios, botones y tablas.
- **main.py:** crea la ventana, carga los datos, prepara los servicios y controla el cambio de vistas.

Las vistas no manipulan directamente los archivos JSON.

## Flujo de productos

```text
MainView
   ↓
Formulario de producto
   ↓
Botón command=
   ↓
RestauranteServicio
   ↓
ArchivoServicio
   ↓
productos.json
   ↓
Actualización de la tabla
```

## Ejecución

Se requiere Python con Tkinter disponible. Desde la carpeta `restaurante_app` ejecutar:

```bash
python main.py
```

En Windows también puede utilizarse:

```powershell
py main.py
```

## Credenciales de prueba

- **Usuario:** `0922248737`
- **Contraseña:** `1234`

También se puede utilizar el correo registrado en `usuarios.json` como usuario.

## Comprobaciones sugeridas

1. Ejecutar `main.py` sin errores.
2. Iniciar sesión con las credenciales de prueba.
3. Entrar en **Usuarios** y comprobar la consulta.
4. Entrar en **Productos** y registrar un producto.
5. Cargar / consultar el producto mediante su código.
6. Modificar sus datos y utilizar **Actualizar**.
7. Utilizar **Eliminar** y confirmar la eliminación.
8. Cerrar y volver a ejecutar la aplicación para comprobar la persistencia en `productos.json`.

## Alcance de la Semana 14

La actividad se concentra en componentes, contenedores, gestores de geometría e interacción básica mediante botones. No se incorporan eventos avanzados con `bind()`, doble clic, teclado o mouse, ni edición directa de tablas o bases de datos.
