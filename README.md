# Restaurante App — Semana 13

## Descripción

Proyecto de Programación Orientada a Objetos correspondiente a la Semana 13. Esta versión inicia la transición de `restaurante_app` desde una aplicación de consola hacia una interfaz gráfica de usuario desarrollada con **Tkinter**.

La aplicación utiliza una estructura separada por responsabilidades: modelos, servicios, datos JSON, vistas gráficas y un archivo `main.py` que prepara las dependencias y mantiene una sola ventana principal.

## Funcionalidades implementadas

- Pantalla de acceso mediante `LoginView`.
- Validación visual de campos vacíos.
- Validación de credenciales mediante `RestauranteServicio`.
- Acceso con identificación o correo electrónico.
- Panel principal mediante `MainView`.
- Visualización de productos cargados desde `productos.json`.
- Visualización de usuarios cargados desde `usuarios.json`.
- Resumen de cantidad de productos y usuarios.
- Opción **Ventas** identificada como funcionalidad pendiente.
- Cierre de sesión y retorno al login dentro de la misma ventana.

## Estructura

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

## Responsabilidad de los componentes

- **Producto:** representa cada producto del restaurante y valida sus datos.
- **Usuario:** representa a los usuarios utilizados para la simulación de acceso.
- **ArchivoServicio:** lee los archivos JSON y construye los objetos correspondientes.
- **RestauranteServicio:** concentra las operaciones de acceso y consulta de productos y usuarios.
- **LoginView:** presenta los campos de usuario, contraseña, mensajes de validación y botón de ingreso.
- **MainView:** presenta el panel principal, los productos, los usuarios y la opción futura de ventas.
- **main.py:** crea una única instancia de `Tk()`, prepara los servicios y controla el cambio entre las vistas.

## Flujo de la aplicación

```text
Inicio
  ↓
main.py crea Tkinter y carga los datos
  ↓
LoginView
  ↓
Usuario + contraseña
  ↓
RestauranteServicio valida el acceso
  ↓
MainView
  ↓
Productos | Usuarios | Ventas (pendiente)
  ↓
Cerrar sesión
  ↓
LoginView
```

## Credenciales de prueba

Para comprobar el funcionamiento se puede utilizar:

- **Usuario:** `0922248737`
- **Contraseña:** `1234`

También se puede utilizar el correo registrado en `usuarios.json` como usuario.

> El acceso es una simulación pedagógica y no representa un mecanismo real de autenticación segura.

## Ejecución

Se requiere Python con Tkinter disponible. Desde la carpeta `restaurante_app` ejecute:

```bash
python main.py
```

En Windows también puede utilizar:

```powershell
py main.py
```

## Comprobaciones realizadas

1. Los archivos Python compilan correctamente.
2. Los productos se cargan desde `productos.json`.
3. Los usuarios se cargan desde `usuarios.json`.
4. Las credenciales válidas permiten el acceso mediante `RestauranteServicio`.
5. Credenciales incorrectas son rechazadas.
6. Las vistas reciben la información desde el servicio y no leen directamente los archivos JSON.
7. La aplicación mantiene una sola ventana principal y un solo `mainloop()`.

## Funcionalidades pendientes

Las ventas completas, formularios CRUD y otras funciones de la aplicación de consola anterior no se incorporan todavía en esta etapa, ya que serán desarrolladas progresivamente en las siguientes semanas.
