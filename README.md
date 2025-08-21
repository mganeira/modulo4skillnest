# Módulo 4 Skillnest - Programación Orientada a Objetos

Material correspondiente al módulo 4 del **Bootcamp Python Trainee de Skillnest**, orientado a Programación Orientada a Objetos (POO) y manejo avanzado de archivos en Python.

## 🎯 Objetivo del Módulo

Este repositorio contiene una colección completa de ejercicios, proyectos y sistemas desarrollados para dominar los conceptos fundamentales de la Programación Orientada a Objetos, manejo de archivos, excepciones y manipulación de datos CSV en Python.

## 📁 Estructura del Repositorio

```
Módulo-4-Skillnest/
├── 📂 POO/                          # Conceptos fundamentales de POO
├── 📂 creacion_de_clases/           # Fundamentos de clases y objetos
├── 📂 pilares_poo/                  # Encapsulación, Herencia, Polimorfismo
├── 📂 metodos/                      # Métodos especiales y avanzados
├── 📂 asociacion_clases/            # Relaciones entre clases
├── 📂 manejo_de_archivos/           # Manipulación de archivos y CSV
├── 📂 excepciones/                  # Gestión de errores y excepciones
├── 📂 bikecity/                     # Proyecto sistema de bicicletas
├── 📂 ev_grupal_6_inventario/       # Sistema de inventario (Evaluación grupal)
├── 📂 ev_modulo/                    # Evaluación final del módulo
└── 📄 README.md                     # Documentación principal
```

## 🚀 Proyectos Principales

### 1. Sistema de Inventario (Evaluación Grupal 6)
**Ubicación:** `ev_grupal_6_inventario/`

Sistema completo de gestión de inventario con funcionalidades CRUD:
- Gestión de productos con CSV
- Respaldos automáticos
- Búsqueda y filtrado
- Validación robusta de datos

### 2. BikeCity - Sistema de Bicicletas
**Ubicación:** `bikecity/`

Aplicación de gestión de sistema de bicicletas urbanas:
- Programación orientada a objetos avanzada
- Gestión de usuarios y bicicletas
- Sistema de alquiler y devolución

### 3. Sistema de Biblioteca
**Ubicación:** `manejo_de_archivos/`

Gestión completa de biblioteca con:
- CRUD de libros
- Sistema de préstamos
- Persistencia en archivos TXT

## 📚 Conceptos Cubiertos por Carpeta

### 🎯 POO - Programación Orientada a Objetos
Conceptos fundamentales de la programación orientada a objetos en Python.

### 🏗️ creacion_de_clases
- Definición de clases y objetos
- Constructores (`__init__`)
- Atributos de instancia y clase
- Métodos básicos

```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def mostrar_info(self):
        return f"{self.nombre}: ${self.precio}"
```

### 🛡️ pilares_poo
Los cuatro pilares fundamentales de la POO:

#### **Encapsulación**
```python
class CuentaBanco:
    def __init__(self):
        self.__saldo = 0  # Atributo privado
    
    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
```

#### **Herencia**
```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"
```

#### **Polimorfismo**
```python
def procesar_animal(animal):
    return animal.hacer_sonido()  # Funciona con cualquier subclase
```

#### **Abstracción**
```python
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass
```

### ⚙️ metodos
Métodos especiales y avanzados:
- Métodos mágicos (`__str__`, `__repr__`, `__len__`)
- Métodos de clase (`@classmethod`)
- Métodos estáticos (`@staticmethod`)
- Propiedades (`@property`)

```python
class Libro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
    
    def __str__(self):
        return f"Libro: {self.titulo}"
    
    def __len__(self):
        return self.paginas
    
    @property
    def es_largo(self):
        return self.paginas > 300
```

### 🔗 asociacion_clases
Relaciones entre clases:
- **Composición**: "tiene un"
- **Agregación**: "usa un"
- **Asociación**: relaciones entre objetos

```python
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Coche:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor  # Composición
```

### 📁 manejo_de_archivos
Manipulación avanzada de archivos:

#### **Context Managers**
```python
with open("archivo.txt", "r", encoding="utf-8") as file:
    contenido = file.read()
```

#### **Trabajo con CSV**
```python
import csv

with open('datos.csv', 'w', newline='', encoding='utf-8') as file:
    escritor = csv.writer(file)
    escritor.writerow(['Nombre', 'Precio', 'Cantidad'])
```

#### **Gestión de Rutas**
```python
from pathlib import Path

ruta = Path("./archivos") / "documento.txt"
with ruta.open("r") as archivo:
    contenido = archivo.read()
```

### ⚠️ excepciones
Manejo robusto de errores:

```python
try:
    with open(archivo, 'r') as f:
        contenido = f.read()
except FileNotFoundError:
    print("El archivo no existe")
except PermissionError:
    print("Sin permisos de acceso")
except Exception as e:
    print(f"Error inesperado: {e}")
else:
    print("Operación exitosa")
finally:
    print("Limpieza completada")
```

## 🛠️ Requisitos Técnicos

- **Python 3.6 o superior**
- **Módulos estándar requeridos:**
  - `csv` - Manipulación de archivos CSV
  - `os` - Operaciones del sistema operativo
  - `datetime` - Manejo de fechas y tiempo
  - `pathlib` - Manejo moderno de rutas
  - `shutil` - Utilidades de archivos
  - `abc` - Clases abstractas

## 🚀 Instalación y Ejecución

1. **Clonar el repositorio:**
```bash
git clone https://github.com/tu-usuario/modulo-4-skillnest.git
cd modulo-4-skillnest
```

2. **Verificar instalación de Python:**
```bash
python --version
```

3. **Ejecutar proyectos específicos:**
```bash
# Sistema de inventario
cd ev_grupal_6_inventario
python inventario.py

# Sistema BikeCity
cd bikecity
python main.py

# Ejemplos de POO
cd POO
python ejemplo_clases.py
```

## 📖 Guía de Estudio Recomendada

### **Nivel Principiante**
1. `creacion_de_clases/` - Fundamentos básicos
2. `POO/` - Conceptos introductorios
3. `metodos/` - Métodos básicos

### **Nivel Intermedio**
4. `pilares_poo/` - Encapsulación y herencia
5. `excepciones/` - Manejo de errores
6. `manejo_de_archivos/` - Persistencia de datos
7. `asociacion_clases/` - Relaciones complejas
8. `bikecity/` - Proyecto integrador
9. `ev_grupal_6_inventario/` - Sistema completo

## 🎯 Competencias Desarrolladas

### **Programación Orientada a Objetos**
- ✅ Diseño e implementación de clases
- ✅ Aplicación de los pilares de la POO
- ✅ Relaciones entre objetos
- ✅ Patrones de diseño básicos

### **Manejo de Archivos**
- ✅ Lectura y escritura de archivos
- ✅ Manipulación de CSV y TXT
- ✅ Context managers y buenas prácticas
- ✅ Gestión de rutas con pathlib

### **Gestión de Errores**
- ✅ Captura y manejo de excepciones
- ✅ Validación de datos de entrada
- ✅ Recuperación elegante de errores
- ✅ Logging y debugging

### **Desarrollo de Aplicaciones**
- ✅ Arquitectura de software básica
- ✅ Operaciones CRUD completas
- ✅ Interfaces de usuario por consola
- ✅ Persistencia y respaldos de datos

## 📋 Evaluaciones Incluidas

### **Evaluación Grupal 6 - Sistema de Inventario**
- Implementación completa de CRUD
- Manejo avanzado de archivos CSV
- Validación robusta de datos
- Sistema de respaldos automáticos

### **Evaluación Final del Módulo**
- Aplicación integral de todos los conceptos
- Demostración de dominio de POO
- Implementación de mejores prácticas

## 🔧 Funcionalidades Destacadas

### **Sistema de Inventario**
- ✨ Detección automática de encabezados CSV
- 🔄 Respaldos automáticos con timestamp
- 🔍 Búsqueda y filtrado avanzado
- ✏️ Edición in-place de productos
- 🛡️ Validación completa de datos

### **Sistema BikeCity**
- 🚲 Gestión completa de flota de bicicletas
- 👤 Sistema de usuarios y membresías
- 📍 Gestión de estaciones y ubicaciones
- 📊 Reportes y estadísticas de uso

## 💡 Mejores Prácticas Implementadas

### **Código Limpio**
```python
# Nombres descriptivos
class GestorInventario:
    def agregar_producto(self, producto):
        pass

# Documentación clara
def buscar_por_nombre(self, nombre: str) -> list:
    """Busca productos por nombre parcial o completo."""
    pass
```

### **Manejo Seguro de Archivos**
```python
# Encoding explícito
with open(archivo, 'r', encoding='utf-8') as file:
    contenido = file.read()

# Validación antes de operaciones
if archivo_path.exists():
    # Procesar archivo
```

### **Encapsulación Apropiada**
```python
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre      # Protegido
        self.__id = self._generar_id()  # Privado
    
    @property
    def nombre(self):
        return self._nombre
```

## 📈 Progresión del Aprendizaje

```
Semana 1: Fundamentos de POO → creacion_de_clases/
Semana 2: Pilares de POO → pilares_poo/
Semana 3: Métodos Avanzados → metodos/
Semana 4: Manejo de Archivos → manejo_de_archivos/
Semana 5: Excepciones → excepciones/
Semana 6: Asociaciones → asociacion_clases/
Semana 7: Proyecto BikeCity → bikecity/
Semana 8: Evaluación Final → ev_grupal_6_inventario/
```

## 🤝 Contribución

Este proyecto ha sido desarrollado como parte del **Bootcamp Python Trainee de Skillnest**. Las contribuciones y mejoras son bienvenidas:

1. Fork del proyecto
2. Crear rama para nueva funcionalidad
3. Commit de cambios
4. Push a la rama
5. Abrir Pull Request

## 📝 Licencia

Proyecto educativo de código abierto desarrollado para fines de aprendizaje.

---

## 🎓 Sobre Skillnest

Este material forma parte del programa educativo de **Skillnest**, enfocado en formar desarrolladores Python con sólidas bases en programación orientada a objetos y mejores prácticas de desarrollo de software.

**¡Feliz aprendizaje! 🐍✨**
