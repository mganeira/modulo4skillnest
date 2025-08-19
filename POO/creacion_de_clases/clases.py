class Auto:
    #metodo constructor
    def __init__(self, marca, modelo, color): 
        self.marca = marca
        self.modelo = modelo
        self.color = color
    #metodos
    def acelerar(self):
        print(f"{self.marca} {self.modelo} está acelerando.")
        if(self.marca == "Toyota"):
            print("Bruuuuuum!")
        elif(self.marca == "Audi"):
            print("Niuuuuuuuum!")
    def frenar(self):
        print(f"{self.marca} {self.modelo} está frenando.")
    def encender_luces(self):
        print(f"Luces de {self.marca} {self.modelo} encendidas.")
mi_auto_1 = Auto("Toyota","Corolla","Gris")
mi_auto_2 = Auto("Audi","R8","Negro")
print(type(mi_auto_1)) #Inspeccionando clase
mi_auto_1.acelerar() #Llamando al método acelerar
print("Es de color:",mi_auto_1.color) #Accediendo a un atributo
print("-"*20)
mi_auto_2.acelerar()
mi_auto_2.encender_luces()



class Celular:
    #metodo constructor
    def __init__(self, marca, modelo, color): 
        self.marca = marca
        self.modelo = modelo
        self.color = color
    #metodos
    def sacar_foto(self):
        print(f"{self.marca} {self.modelo} está sacando una foto.")
        print("Click!. Se ha sacado una foto")
    
    def cargarse(self):
        print("Enchufa el cargador para que se cargue.")
        print("Carga rápida activada.")
        print(f"{self.marca} {self.modelo} está cargándose.")

    def llamar(self, numero):
        print(f"Llamando al {numero} desde {self.marca}.")

    def enviar_mensaje(self, numero, mensaje):
        print(f"Enviando mensaje a {numero}: {mensaje}")
    def tomar_foto(self, capacidad_almacenamiento):
        if capacidad_almacenamiento > 0:
            print(f"Tomando foto con {self.marca}.")
        else:
            print(f"No hay suficiente espacio en {self.marca} para tomar la foto.")
    def programar_alarma(self,hora):
        print(f"Alarma programada en {self.marca}. Hora: {hora}")
    def desbloquear(self,huella):
        if huella:
            print(f"{self.marca} desbloqueado con huella.")
        else:
            print(f"{self.marca} no se pudo desbloquear. Huella no reconocida.")


iphone =Celular("Apple", "Iphone13", "Azul")

iphone.sacar_foto()
iphone.cargarse()

zflip =Celular("Samsung", "Z Flip", "Verde agua")

zflip.sacar_foto()
