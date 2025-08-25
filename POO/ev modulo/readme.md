# Sistema de Gestión de Biblioteca

Un sistema completo de gestión de biblioteca desarrollado en Python que permite administrar libros físicos y digitales con persistencia de datos en archivo de texto.

## Características

- **Gestión completa de libros**: Agregar, eliminar, buscar y listar libros
- **Control de préstamos**: Marcar libros como prestados y gestionar devoluciones
- **Persistencia de datos**: Los datos se guardan automáticamente en `biblio.txt`
- **Herencia de clases**: Soporte para libros digitales con formato específico
- **Interfaz de usuario**: Menú interactivo por consola

## Estructura del Proyecto

```
proyecto/
│
├── main.py          # Archivo principal del sistema
├── biblio.txt       # Archivo de datos (se crea automáticamente)
└── README.md        # Este archivo
```

## Clases Principales

### Clase `Libro`
Representa un libro con los siguientes atributos:
- **Título**: Nombre del libro
- **Autor**: Autor del libro
- **Año de publicación**: Año en que se publicó
- **Estado**: "disponible" o "no disponible"

**Métodos principales:**
- Getters y setters para todos los atributos
- `__str__()`: Representación en cadena del objeto

### Clase `Biblioteca`
Gestiona la colección de libros y todas las operaciones del sistema.

**Funcionalidades:**
- Cargar y guardar datos desde/hacia archivo
- Operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
- Gestión de préstamos y devoluciones
- Búsqueda y filtrado de libros
- Estadísticas de disponibilidad

### Clase `LibroDigital` (Herencia)
Extiende la clase `Libro` añadiendo:
- **Formato**: Tipo de archivo digital (PDF, EPUB, etc.)

## Instalación y Uso

### Requisitos
- Python 3.6 o superior
- No requiere librerías externas adicionales

### Ejecución

1. **Clonar o descargar el archivo**:
   ```bash
   # Si tienes el archivo main.py
   python main.py
   ```

2. **Primera ejecución**:
   - Si no existe `biblio.txt`, se creará automáticamente
   - El sistema iniciará con una biblioteca vacía

3. **Ejecuciones posteriores**:
   - Los libros se cargarán automáticamente desde `biblio.txt`

## Menú de Opciones

```
1: Agregar un libro
2: Eliminar un libro por su título
3: Listar todos los libros disponibles
4: Buscar un libro por su título
5: Marcar un libro como prestado
6: Devolver un libro prestado
7: Salir
```

## Formato del Archivo de Datos

El archivo `biblio.txt` almacena cada libro en una línea con el formato:
```
Título,Autor,Año,Estado
```

**Ejemplo:**
```
El Quijote,Miguel de Cervantes,1605,disponible
Cien años de soledad,Gabriel García Márquez,1967,no disponible
```

## Funcionalidades Detalladas

### 1. Agregar Libro
- Solicita título, autor, año y estado
- Valida que el estado sea "disponible" o "no disponible"
- Guarda automáticamente en el archivo

### 2. Eliminar Libro
- Busca por título (no distingue mayúsculas/minúsculas)
- Elimina de la lista y actualiza el archivo

### 3. Listar Libros
- Muestra todos los libros en formato de tabla
- Incluye título, autor, año y estado

### 4. Buscar Libro
- Búsqueda por título exacto (no distingue mayúsculas/minúsculas)
- Muestra información completa del libro encontrado

### 5. Marcar como Prestado
- Cambia el estado de "disponible" a "no disponible"
- Verifica que el libro esté disponible antes del préstamo

### 6. Devolver Libro
- Cambia el estado de "no disponible" a "disponible"
- Verifica que el libro esté prestado antes de la devolución

## Gestión de Archivos

El sistema utiliza `pathlib` para el manejo robusto de rutas:

```python
# Obtiene la ruta del directorio del script
BASE_DIR = Path(__file__).resolve().parent

# Define la ruta del archivo de datos
RUTA_ARCHIVO = BASE_DIR / "biblio.txt"
```

### Persistencia Automática
- **Carga inicial**: Al iniciar el menú
- **Guardado automático**: Después de cada operación que modifica datos
- **Guardado final**: Al salir del programa

## Manejo de Errores

El sistema incluye manejo de errores para:
- Archivo no encontrado (crea biblioteca vacía)
- Errores de lectura/escritura de archivos
- Validación de estados de libros
- Búsquedas sin resultados

## Extensibilidad

### Añadir Nuevos Tipos de Libros
```python
class LibroAudio(Libro):
    def __init__(self, titulo, autor, anio_publicacion, estado, duracion):
        super().__init__(titulo, autor, anio_publicacion, estado)
        self.duracion = duracion
```

### Métodos de Estadísticas Disponibles
- `obtener_libros_por_estado(estado)`: Filtra libros por estado
- `contar_libros_disponibles()`: Cuenta libros disponibles
- `contar_libros_prestados()`: Cuenta libros prestados

## Notas Técnicas

- **Encoding**: UTF-8 para soporte de caracteres especiales
- **Separador**: Coma (,) para campos en el archivo
- **Estados válidos**: "disponible", "no disponible"
- **Búsquedas**: No distinguen mayúsculas/minúsculas

## Posibles Mejoras

- Interfaz gráfica (GUI)
- Base de datos en lugar de archivo de texto
- Validación de datos más robusta
- Sistema de usuarios y permisos
- Histórico de préstamos
- Fechas de préstamo y devolución
- Reservas de libros

## Licencia

Este proyecto es de código abierto y puede ser usado con fines educativos.
