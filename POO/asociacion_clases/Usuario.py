from Tarjeta import *

class Usuario:


   def __init__(self, nombre, apellido, email):

       self.nombre = nombre

       self.apellido = apellido

       self.email = email

       self.tarjeta = TarjetaCredito(0, 20000, 0.015) #Agregamos esta línea