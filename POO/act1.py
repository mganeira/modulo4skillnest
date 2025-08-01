class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupada = False
    def ocupar(self):
        self.ocupada = True
    def liberar(self):
        self.ocupada = False

class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Pedido:
    def __init__(self, mesa):
        self.mesa = mesa
        self.platos = []
    def agregar_plato(self, plato):
        self.platos.append(plato)
    def calcular_total(self):
        return sum(plato.precio for plato in self.platos)