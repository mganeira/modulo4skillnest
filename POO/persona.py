class Persona:
   def __init__(self, nombre, apellido, edad, tamagotchi):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.tamagotchi = tamagotchi

   def jugar_con_tamagotchi(self):
    print(f"{self.nombre} {self.apellido} está jugando con su {self.tamagotchi}.")
    self.tamagotchi.jugar()
    return self
   
   def darle_comida(self): 
      print (f"{self.nombre} {self.apellido} le está dando de comer a su {self.tamagotchi}.")
      self.tamagotchi.comer()
      return self

   def curarlo(self):
      print(f"{self.nombre} {self.apellido} está jugando con su {self.tamagotchi.nombre}.")
      self.tamagotchi.curar()
      return self