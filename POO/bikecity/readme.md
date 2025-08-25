# 🚴‍♂️ BIKECITY - Sistema de Reservas de Bicicletas

Sistema completo para la gestión de reservas de bicicletas urbanas con manejo robusto de excepciones y validaciones.

## 📋 Características

- **Gestión de Clientes**: Registro y administración de usuarios
- **Inventario de Bicicletas**: Control de disponibilidad y estados
- **Sistema de Reservas**: Creación, pago y seguimiento de reservas
- **Manejo de Excepciones**: Validaciones robustas y mensajes de error claros
- **Estados de Reserva**: Control completo del ciclo de vida (Pendiente → Activa → Completada)

## 🏗️ Arquitectura del Sistema

### Clases Principales

#### `Bicicleta`
Representa una bicicleta en el sistema con:
- ID único
- Modelo y precio por hora
- Estado de disponibilidad
- Estado de conservación

#### `Cliente` 
Gestiona información de usuarios:
- Datos personales (ID, nombre, teléfono, email)
- Historial de reservas

#### `Reserva`
Controla las reservas con:
- Información de cliente y bicicleta
- Duración y monto
- Fechas de reserva y límite
- Estados del proceso

#### `SistemaBikeCity`
Sistema principal que coordina:
- Inventario de bicicletas y clientes
- Procesamiento de reservas
- Validaciones y manejo de errores

### Manejo de Excepciones

El sistema implementa múltiples tipos de excepciones:

| Tipo | Uso | Ejemplo |
|------|-----|---------|
| `ValueError` | Datos inválidos | Horas negativas, IDs vacíos |
| `KeyError` | Recursos no encontrados | Cliente/bicicleta inexistente |
| `SystemError` | Reglas de negocio | Reservas duplicadas, bicicleta no disponible |
| `TypeError` | Tipos incorrectos | Objetos que no son instancias correctas |

## 🚀 Instalación y Uso

### Requisitos
- Python 3.7+
- Módulo `datetime` (incluido en Python estándar)

### Ejecución Rápida

```python
# Ejecutar el sistema completo
python bikecity.py
```

### Uso Programático

```python
from bikecity import SistemaBikeCity, Cliente, Bicicleta

# Inicializar sistema
sistema = SistemaBikeCity()

# Agregar cliente
cliente = Cliente("CLI001", "Juan Perez", "987654321")
sistema.agregar_cliente(cliente)

# Agregar bicicleta
bici = Bicicleta("B001", "Mountain Bike", 6000)
sistema.agregar_bicicleta(bici)

# Crear reserva
try:
    reserva_id = sistema.crear_reserva("CLI001", "B001", 2)
    sistema.procesar_pago(reserva_id, 12000)
    # ... usar bicicleta ...
    sistema.completar_reserva(reserva_id)
except Exception as e:
    print(f"Error: {e}")
```

## 📊 Flujo de Operación

### 1. Creación de Reserva
```python
reserva_id = sistema.crear_reserva(cliente_id, bicicleta_id, horas)
```

**Validaciones realizadas:**
- ✅ Cliente existe en el sistema
- ✅ Bicicleta existe y está disponible
- ✅ Cliente no tiene reservas activas
- ✅ Horas es un número positivo

### 2. Procesamiento de Pago
```python
sistema.procesar_pago(reserva_id, monto_pagado)
```

**Verificaciones:**
- ✅ Reserva existe y está pendiente
- ✅ Monto pagado coincide exactamente

### 3. Finalización
```python
sistema.completar_reserva(reserva_id)
```

**Acciones:**
- ✅ Libera la bicicleta
- ✅ Actualiza estado a "Completada"
- ✅ Remueve de reservas activas

## 🎯 Estados de Reserva

| Estado | Descripción | Transiciones Permitidas |
|--------|-------------|------------------------|
| **Pendiente** | Reserva creada, esperando pago | → Activa (tras pago) |
| **Activa** | Pagada y lista para usar | → Completada |
| **Completada** | Finalizada correctamente | Estado final |
| **Cancelada** | Reserva cancelada | Estado final |

## 🔧 Datos por Defecto

El sistema incluye datos de prueba:

### Clientes Pre-cargados
- CLI001: Juan Perez (987654321)
- CLI002: Maria Garcia (987654322)  
- CLI003: Carlos Lopez (987654323)

### Bicicletas Disponibles
- B001: Mountain Bike ($6,000/hora)
- B002: City Bike ($4,000/hora)
- B003: Electric Bike ($8,000/hora)

## 🛠️ Personalización

### Agregar Nuevos Tipos de Bicicleta
```python
bici_premium = Bicicleta("B004", "Premium Electric", 10000)
sistema.agregar_bicicleta(bici_premium)
```

### Extender Funcionalidad
```python
class BicicletaElectrica(Bicicleta):
    def __init__(self, id_bici, modelo, precio_hora, autonomia):
        super().__init__(id_bici, modelo, precio_hora)
        self.autonomia = autonomia
        self.bateria = 100
```

## ⚠️ Manejo de Errores Comunes

### Error: Cliente ya tiene reserva activa
```
Error de negocio: Cliente CLI001 ya tiene reserva activa
```
**Solución**: Completar o cancelar la reserva actual antes de crear una nueva.

### Error: Bicicleta no disponible
```
Error de negocio: Bicicleta B001 no disponible
```
**Solución**: Seleccionar una bicicleta diferente o esperar a que se libere.

### Error: Monto incorrecto
```
Error en pago: Monto incorrecto: esperado $12000, recibido $10000
```
**Solución**: Verificar el cálculo del monto total (horas × precio_hora).

## 📈 Monitoreo del Sistema

### Ver Estado Completo
```python
sistema.mostrar_estado()
```

Muestra:
- Lista de clientes registrados
- Inventario de bicicletas y disponibilidad
- Reservas activas con montos

### Consultar Historial de Cliente
```python
cliente = sistema.clientes["CLI001"]
print(f"Reservas históricas: {cliente.reservas_historicas}")
```

## 🤝 Contribución

Para contribuir al proyecto:

1. Mantener el patrón de manejo de excepciones
2. Documentar nuevas funcionalidades
3. Incluir validaciones apropiadas
4. Seguir la estructura de clases existente

## 📝 Licencia

Este proyecto es parte de material educativo para el aprendizaje de manejo de excepciones en Python.

---

**Desarrollado con fines educativos** - Gestión de Excepciones en Python
