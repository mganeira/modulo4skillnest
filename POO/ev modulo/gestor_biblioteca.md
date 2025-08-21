# Sistema de Gestión de Biblioteca

Sistema simple de gestión de libros desarrollado en Python que permite administrar una biblioteca mediante archivos de texto.

## 📚 Funcionalidades

- **Agregar libros**: Registra nuevos libros con título, autor, año de publicación y estado
- **Eliminar libros**: Remueve libros por título
- **Listar libros**: Muestra todos los libros registrados en formato tabla
- **Buscar libros**: Encuentra libros específicos por título
- **Préstamo de libros**: Marca libros como "no disponible" 
- **Devolución**: Cambia el estado a "Disponible" cuando se devuelve un libro

## 🗂️ Estructura del Código

### Clases
- **`Libro`**: Clase base con propiedades básicas (título, autor, año, estado)
- **`LibroDigital`**: Hereda de `Libro` y añade formato digital
- **`Biblioteca`**: Contiene configuración del menú y archivo

### Funciones Principales
- `agregar_libro()`: Añade nuevos libros al archivo
- `eliminar_libro()`: Elimina libros por título
- `listar_libros()`: Muestra listado completo
- `buscar_libro()`: Busca libro específico
- `marcar_libro_prestado()`: Gestiona préstamos
- `devolver_libro()`: Procesa devoluciones
- `menu()`: Interfaz principal del usuario

## 💾 Almacenamiento

Los datos se guardan en `biblioteca.txt` en formato CSV:
```
Título,Autor,Año,Estado
El Quijote,Cervantes,1605,Disponible
```

## 🚀 Uso

1. Ejecuta el archivo Python
2. Selecciona una opción del menú (1-7)
3. Sigue las instrucciones para cada operación
4. Los datos se guardan automáticamente

## 📋 Requisitos

- Python 3.x
- Biblioteca `pathlib` (incluida en Python estándar)

## ⚠️ Nota

El sistema maneja estados como "Disponible", "disponible", "No disponible", etc. de forma flexible para mayor usabilidad.
