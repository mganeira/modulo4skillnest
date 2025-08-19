#bikecity resumido por claude ai
"""
Sistema de Reservas BIKECITY del profe
Manejo de renta de bicicletas urbanas con manejo de excepciones
Resumida
"""

from datetime import datetime, timedelta

# EXCEPCIÓN PERSONALIZADA
class SystemError(Exception):
    """Excepción para errores específicos del sistema de reservas"""
    def __init__(self, mensaje, codigo_error=None):
        self.codigo_error = codigo_error
        super().__init__(mensaje)

# CLASES PRINCIPALES

class Bicicleta:
    def __init__(self, id_bici, modelo, precio_hora=5000):
        self.id = id_bici
        self.modelo = modelo
        self.precio_hora = precio_hora
        self.disponible = True
        self.estado = "Bueno"
        
    def __str__(self):
        estado_disp = "Disponible" if self.disponible else "No disponible"
        return f"Bicicleta {self.id} - {self.modelo} - {estado_disp}"

class Cliente:
    def __init__(self, id_cliente, nombre, telefono, email=""):
        self.id = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.reservas_historicas = []
        
    def __str__(self):
        return f"Cliente {self.id} - {self.nombre}"

class Reserva:
    def __init__(self, id_reserva, cliente_id, bicicleta_id, horas):
        self.id = id_reserva
        self.cliente_id = cliente_id
        self.bicicleta_id = bicicleta_id
        self.horas = horas
        self.fecha_reserva = datetime.now()
        self.fecha_limite = self.fecha_reserva + timedelta(hours=1)  # 1 hora para recoger
        self.estado = "Pendiente"  # Pendiente, Activa, Completada, Cancelada
        self.monto = 0

# SISTEMA PRINCIPAL
class SistemaBikeCity:
    def __init__(self):
        self.bicicletas = {}
        self.clientes = {}
        self.reservas = {}
        self.reservas_activas = {}  # cliente_id -> reserva_id
        self.contador_reservas = 1
        
    def agregar_cliente(self, cliente):
        """Agrega un cliente con validaciones"""
        try:
            if not isinstance(cliente, Cliente):
                raise TypeError("Debe ser una instancia de Cliente")
            
            if cliente.id in self.clientes:
                raise SystemError(f"Cliente {cliente.id} ya existe", "DUPLICADO")
                
            self.clientes[cliente.id] = cliente
            print(f"Cliente {cliente.nombre} agregado exitosamente")
            
        except (TypeError, SystemError) as e:
            print(f"Error: {e}")
            raise
        
    def agregar_bicicleta(self, bicicleta):
        """Agrega una bicicleta con validaciones"""
        try:
            if not isinstance(bicicleta, Bicicleta):
                raise TypeError("Debe ser una instancia de Bicicleta")
            
            if bicicleta.id in self.bicicletas:
                raise SystemError(f"Bicicleta {bicicleta.id} ya existe", "DUPLICADA")
                
            self.bicicletas[bicicleta.id] = bicicleta
            print(f"Bicicleta {bicicleta.id} agregada exitosamente")
            
        except (TypeError, SystemError) as e:
            print(f"Error: {e}")
            raise
    
    def crear_reserva(self, cliente_id, bicicleta_id, horas):
        """Crear reserva con manejo múltiple de excepciones"""
        
        try:
            # VALIDACIONES BÁSICAS (ValueError/TypeError)
            if not cliente_id or not isinstance(cliente_id, str):
                raise ValueError("ID de cliente inválido")
            
            if not isinstance(horas, (int, float)) or horas <= 0:
                raise ValueError("Horas debe ser número positivo")
            
            # VERIFICAR EXISTENCIA (KeyError)
            if cliente_id not in self.clientes:
                raise KeyError(f"Cliente {cliente_id} no existe")
            
            if bicicleta_id not in self.bicicletas:
                raise KeyError(f"Bicicleta {bicicleta_id} no existe")
            
            # VERIFICAR RESERVAS DUPLICADAS (SystemError)
            if cliente_id in self.reservas_activas:
                raise SystemError(
                    f"Cliente {cliente_id} ya tiene reserva activa", 
                    "RESERVA_DUPLICADA"
                )
            
            # VERIFICAR DISPONIBILIDAD (SystemError)
            bicicleta = self.bicicletas[bicicleta_id]
            if not bicicleta.disponible:
                raise SystemError(
                    f"Bicicleta {bicicleta_id} no disponible", 
                    "NO_DISPONIBLE"
                )
            
            # CREAR RESERVA
            reserva = Reserva(self.contador_reservas, cliente_id, bicicleta_id, horas)
            reserva.monto = horas * bicicleta.precio_hora
            
            # REGISTRAR EN SISTEMA
            self.reservas[reserva.id] = reserva
            self.reservas_activas[cliente_id] = reserva.id
            self.clientes[cliente_id].reservas_historicas.append(reserva.id)
            bicicleta.disponible = False
            self.contador_reservas += 1
            
            print(f"Reserva {reserva.id} creada - Monto: ${reserva.monto:,.0f}")
            return reserva.id
            
        except ValueError as e:
            print(f"Error de validación: {e}")
            raise
        except KeyError as e:
            print(f"Error de datos: {e}")
            raise
        except SystemError as e:
            print(f"Error de negocio: {e}")
            raise
        except Exception as e:
            print(f"Error inesperado: {e}")
            raise
        finally:
            print("Operación de reserva procesada")
    
    def procesar_pago(self, reserva_id, monto_pagado):
        """Procesar pago con validación de montos"""
        try:
            if reserva_id not in self.reservas:
                raise KeyError(f"Reserva {reserva_id} no encontrada")
            
            reserva = self.reservas[reserva_id]
            
            if reserva.estado != "Pendiente":
                raise SystemError(f"Reserva en estado {reserva.estado}, no se puede pagar", "ESTADO_INVALIDO")
            
            if monto_pagado != reserva.monto:
                raise SystemError(
                    f"Monto incorrecto: esperado ${reserva.monto}, recibido ${monto_pagado}", 
                    "MONTO_INCORRECTO"
                )
            
            reserva.estado = "Activa"
            print(f"Pago procesado - Reserva {reserva_id} activada")
            
        except (KeyError, SystemError) as e:
            print(f"Error en pago: {e}")
            raise
    
    def completar_reserva(self, reserva_id):
        """Completar reserva y liberar bicicleta"""
        try:
            reserva = self.reservas[reserva_id]
            
            if reserva.estado != "Activa":
                raise SystemError(f"Reserva debe estar activa, está: {reserva.estado}", "ESTADO_INVALIDO")
            
            # Liberar bicicleta
            self.bicicletas[reserva.bicicleta_id].disponible = True
            reserva.estado = "Completada"
            del self.reservas_activas[reserva.cliente_id]
            
            print(f"Reserva {reserva_id} completada - Bicicleta liberada")
            
        except KeyError:
            raise SystemError(f"Reserva {reserva_id} no encontrada", "NO_EXISTE")
        except SystemError as e:
            print(f"Error: {e}")
            raise
    
    def mostrar_estado(self):
        """Mostrar estado actual del sistema"""
        print("\n" + "="*40)
        print("ESTADO SISTEMA BIKECITY")
        print("="*40)
        
        print(f"\nCLIENTES ({len(self.clientes)}):")
        for cliente in self.clientes.values():
            print(f"  {cliente}")
        
        print(f"\nBICICLETAS ({len(self.bicicletas)}):")
        for bici in self.bicicletas.values():
            print(f"  {bici}")
        
        print(f"\nRESERVAS ACTIVAS ({len(self.reservas_activas)}):")
        for cliente_id, reserva_id in self.reservas_activas.items():
            reserva = self.reservas[reserva_id]
            cliente_nombre = self.clientes[cliente_id].nombre
            print(f"  Reserva {reserva.id} - {cliente_nombre} - ${reserva.monto}")

# INICIALIZACIÓN DEL SISTEMA
def inicializar_sistema():
    """Crear sistema con datos por defecto"""
    sistema = SistemaBikeCity()
    
    # Clientes por defecto
    clientes = [
        Cliente("CLI001", "Juan Perez", "987654321"),
        Cliente("CLI002", "Maria Garcia", "987654322"),
        Cliente("CLI003", "Carlos Lopez", "987654323")
    ]
    
    for cliente in clientes:
        try:
            sistema.agregar_cliente(cliente)
        except Exception:
            pass
    
    # Bicicletas por defecto
    bicicletas = [
        Bicicleta("B001", "Mountain Bike", 6000),
        Bicicleta("B002", "City Bike", 4000),
        Bicicleta("B003", "Electric Bike", 8000)
    ]
    
    for bici in bicicletas:
        try:
            sistema.agregar_bicicleta(bici)
        except Exception:
            pass
    
    return sistema

# FUNCIÓN PRINCIPAL SIMPLIFICADA
def main():
    """Ejemplo de uso del sistema"""
    print("SISTEMA BIKECITY")
    print("="*30)
    
    sistema = inicializar_sistema()
    sistema.mostrar_estado()
    
    # Ejemplo de uso
    try:
        print("\n--- CREANDO RESERVA ---")
        reserva_id = sistema.crear_reserva("CLI001", "B001", 2)
        
        print("\n--- PROCESANDO PAGO ---")
        sistema.procesar_pago(reserva_id, 12000)
        
        print("\n--- ESTADO DESPUÉS DEL PAGO ---")
        sistema.mostrar_estado()
        
        print("\n--- COMPLETANDO RESERVA ---")
        sistema.completar_reserva(reserva_id)
        
        print("\n--- ESTADO FINAL ---")
        sistema.mostrar_estado()
        
    except Exception as e:
        print(f"Error en demo: {e}")

if __name__ == "__main__":
    main()