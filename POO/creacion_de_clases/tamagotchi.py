from persona import *

class Tamagotchi:
    def __init__(self, nombre, color, salud, felicidad, energia):
       self.nombre = nombre
       self.color = color
       self.salud = salud
       self.felicidad = felicidad
       self.energia = energia
       
    def jugar(self):
        self.felicidad += 10
        self.salud -= 5
        print(f"{self.nombre} disfruta jugando y es más feliz pero menos saludable. ")
        return self
    
    def comer(self):
        self.felicidad += 5
        self.salud += 10
        print(f"{self.nombre} está comiendo. Ahora es más feliz y más saludable. ")
        return self
    
    def curar(self):
        self.salud += 20
        self.felicidad -= 5
        print(f"{self.nombre} está siendo curado. Ahora está más saludable pero menos feliz. ")
        return self


    
    
# Crear una instancia de Tamagotchi
mascota1 = Tamagotchi("pupo", "morado", 100, 20, 10)

# Crear instancia de persona y asignar instancia de tamagotchi
persona1= Persona("Mariel", "Gajardo", 24, mascota1)

#Darle de comer, curarlo y jugar con tamagotchi
persona1.darle_comida().curarlo().jugar_con_tamagotchi()

#Crear subclases de tamagotchi con herencia

class TamagotchiParadise(Tamagotchi):
   def __init__(self,nombre, edad, color, planeta, entorno):
      self.nombre = nombre
      self.edad = edad
      self.color = color
      self.planeta = planeta
      self.entorno = entorno

   def elegir_planeta(self):
      print(f"Tamagotchi puede elegir su {self.planeta}.")
