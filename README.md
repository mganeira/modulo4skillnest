# Módulo 4 Skillnest

Material correspondiente a lo trabajado durante el módulo 4 orientado a POO en Python.

# Proyecto de Manejo de Archivos en Python

Una colección de ejercicios y sistemas desarrollados para aprender el manejo de archivos, excepciones y manipulación de datos CSV en Python.

## Contenido del Proyecto

Este repositorio contiene múltiples ejemplos y un sistema completo que demuestran diferentes aspectos del manejo de archivos en Python:

- **Sistema de Inventario CSV**: Aplicación completa de gestión de inventario
- **Sistema de Biblioteca**: Gestión de libros con programación orientada a objetos
- **Ejemplos de acceso a archivos**: Diferentes métodos para leer y escribir archivos
- **Manejo de logs**: Registro de actividades en archivos
- **Gestión de excepciones**: Manejo robusto de errores

## Archivos del Proyecto

```
proyecto/
├── inventario.py                    # Sistema principal de inventario
├── biblioteca.py                   # Sistema de gestión de biblioteca
├── ejemplos_archivos.py            # Ejemplos de acceso a archivos
├── manejo_logs.py                  # Ejemplo de escritura de logs
├── inventario.csv                  # Archivo de datos inventario (generado automáticamente)
├── biblioteca.txt                  # Archivo de datos biblioteca (generado automáticamente)
├── registro.log                    # Archivo de logs (generado automáticamente)
├── archivo1.txt                    # Archivo de ejemplo
├── files/                          # Carpeta de archivos de ejemplo
│   └── archivo1.txt
└── backups/                        # Carpeta de respaldos (generada automáticamente)
    ├── inventario_backup_*.csv
    └── biblioteca_backup_*.txt
```

## Requisitos

- Python 3.6 o superior
- Módulos estándar de Python:
  - `csv`
  - `os`
  - `datetime`
  - `pathlib`
  - `shutil`

## Instalación y Ejecución

1. Clona o descarga todos los archivos del proyecto
2. Asegúrate de tener Python instalado
3. Ejecuta cualquiera de los programas:

```bash
# Sistema principal de inventario
python inventario.py

# Sistema de gestión de biblioteca
python biblioteca.py

# Ejemplos de manejo de archivos
python ejemplos_archivos.py

# Ejemplo de logs
python manejo_logs.py
```

## Conceptos Cubiertos

### 1. Manejo de Archivos con Context Managers

```python
with open("archivo.txt", "r") as file:
    contenido = file.read()
```

**Ventajas del `with` statement:**
- Cierre automático del archivo
- Manejo seguro de recursos
- Prevención de corrupción de datos

### 2. Modos de Apertura de Archivos

- **`'r'` (read)**: Solo lectura, archivo debe existir
- **`'w'` (write)**: Escritura que sobrescribe contenido
- **`'a'` (append)**: Añade contenido al final sin borrar
- **`'r+'`**: Lectura y escritura
- **`'w+'`**: Escritura y lectura (sobrescribe)
- **`'a+'`**: Anexar y lectura

### 3. Métodos de Acceso a Archivos

#### Método 1: Usando `os.path`

```python
import os
ruta_dinamica = os.path.join('.', nombre_archivo)
with open(ruta_dinamica, 'r') as f:
    contenido = f.read()
```

#### Método 2: Usando `pathlib`

```python
from pathlib import Path
ruta_dinamica = Path('./files') / nombre_archivo
with open(ruta_dinamica, 'r') as f:
    contenido = f.read()
```

### 4. Manejo de Excepciones

```python
try:
    with open(archivo, 'r') as f:
        contenido = f.read()
except FileNotFoundError:
    print("El archivo no existe")
except PermissionError:
    print("Sin permisos para acceder al archivo")
except Exception as e:
    print(f"Error inesperado: {e}")
else:
    print("Archivo leído correctamente")
finally:
    print("Operación completada")
```

### 5. Trabajo con CSV

```python
import csv

# Escribir CSV
with open('datos.csv', 'w', newline='', encoding='utf-8') as file:
    escritor = csv.writer(file)
    escritor.writerow(['Nombre', 'Precio', 'Cantidad'])
    escritor.writerow(['Producto1', '10.50', '5'])

# Leer CSV
with open('datos.csv', 'r', encoding='utf-8') as file:
    lector = csv.reader(file)
    for fila in lector:
        print(fila)
```

### 6. Sistema de Logs

```python
with open("registro.log", "a") as file:
    file.write("2025-08-08: Nuevo acceso\n")
```

## Funcionalidades del Sistema de Inventario

### Operaciones CRUD

- **Create**: Añadir nuevos productos
- **Read**: Ver inventario completo y buscar productos específicos
- **Update**: Modificar productos existentes
- **Delete**: Eliminar productos con confirmación

### Características Avanzadas

- **Detección automática de encabezados**: El sistema identifica si un CSV tiene headers
- **Respaldos automáticos**: Copias de seguridad con timestamp
- **Validación de datos**: Verificación de formato y tipos de datos
- **Manejo de errores**: Recuperación elegante de fallos

## Sistema de Gestión de Biblioteca

### Funcionalidades Principales

El sistema de biblioteca permite:

1. **Agregar libros**: Registrar nuevos libros con título, autor, año y estado
2. **Eliminar libros**: Remover libros por título
3. **Listar libros**: Mostrar todos los libros disponibles
4. **Buscar libros**: Encontrar libros por título
5. **Gestión de préstamos**: Marcar libros como prestados
6. **Devolución**: Procesar devolución de libros prestados

### Estructura de Datos

```python
# Clase Libro con encapsulación
class Libro:
    def __init__(self, titulo, autor, anio_publicacion, estado):
        self._titulo = titulo
        self._autor = autor
        self._anio_publicacion = anio_publicacion
        self._estado = estado

# Métodos getter y setter para encapsulación
def get_titulo(self):
    return self._titulo

def set_titulo(self, value):
    self._titulo = value
```

### Operaciones con Archivos

```python
# Agregar libro usando pathlib
def agregar_libro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio_publicacion = input("Año de publicación: ")
    estado = input("Estado: ")
    
    with RUTA_ARCHIVO.open("a", encoding="utf-8") as f:
        f.write(f"{titulo},{autor},{anio_publicacion},{estado}\n")
    print("Libro registrado.")

# Eliminar libro manteniendo otros registros
def eliminar_libro():
    nombre = input("Nombre del libro a eliminar: ")
    nuevas_lineas = []
    eliminado = False
    
    with RUTA_ARCHIVO.open("r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            if len(partes) == 4 and partes[0].lower() == nombre.lower():
                eliminado = True
                continue
            nuevas_lineas.append(linea)
    
    with RUTA_ARCHIVO.open("w", encoding="utf-8") as f:
        f.writelines(nuevas_lineas)
```

## Estructura del Código

### Clase Principal: ManejoInventario

```python
class ManejoInventario:
    def __init__(self):
        self.archivo_nombre = "inventario.csv"
        self.encabezados_defecto = ["Nombre", "Precio", "Cantidad", "Talla"]
    
    def inicializar_archivo_con_encabezados(self):
        # Crea archivo con encabezados si no existe
    
    def ver_inventario(self):
        # Muestra contenido completo
    
    def reemplazar_info(self, texto):
        # Sobrescribe manteniendo encabezados
    
    def añadir_texto(self, texto):
        # Añade sin sobrescribir
    
    def editar_producto(self):
        # Modifica productos existentes
    
    def eliminar_producto(self):
        # Elimina con confirmación
    
    def buscar_producto(self, nombre):
        # Búsqueda por nombre
    
    def crear_backup(self):
        # Crea copias de seguridad
```

## Mejores Prácticas Implementadas

### Encoding UTF-8
```python
with open(archivo, 'r', encoding='utf-8') as file:
    # Maneja correctamente caracteres especiales
```

### Parámetro newline en CSV
```python
with open(archivo, 'w', newline='', encoding='utf-8') as file:
    # Evita líneas en blanco adicionales en Windows
```

### Validación de Entrada
```python
while True:
    try:
        numero = int(input("Elige una opción: "))
        return numero
    except ValueError:
        print("Por favor, ingresa un número válido.")
```

## Manejo de Errores Cubiertos

- **FileNotFoundError**: Archivo no existe
- **PermissionError**: Sin permisos de acceso
- **ValueError**: Datos con formato incorrecto
- **Exception**: Errores generales no previstos

## Ejemplos de Uso

### Crear un Nuevo Inventario

1. Ejecutar `python inventario.py`
2. Seleccionar opción 2 (Sobreescribir)
3. Ingresar datos: `Camiseta,15.99,10,L`

### Agregar un Libro a la Biblioteca

1. Ejecutar `python biblioteca.py`
2. Seleccionar opción 1 (Agregar libro)
3. Ingresar datos del libro paso a paso

### Eliminar un Libro

1. Seleccionar opción 2 (Eliminar libro)
2. Ingresar el título exacto del libro
3. El sistema lo eliminará del archivo

### Buscar un Producto

1. Seleccionar opción 6 (Buscar)
2. Ingresar nombre: `Camiseta`
3. Ver detalles del producto

### Crear Respaldo

1. Seleccionar opción 8 (Backup)
2. El archivo se guarda en `backups/` con timestamp

## Objetivos de Aprendizaje

Este proyecto está diseñado para enseñar:

- **Manipulación de archivos**: Lectura, escritura y modificación con diferentes formatos
- **Programación orientada a objetos**: Encapsulación, getters/setters y organización de código
- **Manejo de excepciones**: Código robusto y resistente a errores
- **Trabajo con CSV y TXT**: Diferentes formatos para almacenamiento de datos
- **Gestión de rutas**: Uso de `os.path` y `pathlib` para manejo moderno de archivos
- **Respaldos de datos**: Protección de información importante
- **Encapsulación**: Uso de atributos privados y métodos de acceso
- **Operaciones CRUD**: Crear, leer, actualizar y eliminar registros
- **Búsqueda y filtrado**: Algoritmos básicos de búsqueda en archivos

## Contribución

Proyecto desarrollado como parte del **Bootcamp Python Trainee de Skillnest** para aprender conceptos fundamentales de programación en Python.

## Licencia

Proyecto educativo de código abierto.
