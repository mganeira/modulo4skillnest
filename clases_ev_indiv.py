class Tarjeta_de_Credito:
    todas_las_tarjetas = []
    def __init__(self, limite_credito= 100000, intereses= 0.0, saldo_pagar= 0):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        print("Tarjeta creada exitosamente.")

        #METODOS DE INSTANCIA
    def compra(self, monto):
        if self.saldo_pagar + monto > self.limite_credito:
             print("No puedes exceder el límite del crédito.")
        else:
             self.saldo_pagar += monto
        return self
    def pago(self, monto):
        self.saldo_pagar -= monto
        print(f"Has pagado {monto}, ahora debes {self.saldo_pagar}.")
        return self
    def mostrar_info_tarjeta(self):
        print("\nMostrando informacion de tarjeta de Credito")
        print("=" * 20)
        print(f"Saldo a pagar: ${self.saldo_pagar}")
        print(f"Limite de credito: ${self.limite_credito}")
        print(f"Intereses: {self.intereses*100}%")
        print("=" * 20)
    def cobrar_intereses(self):
            self.saldo_pagar += self.intereses * self.saldo_pagar
            print(f"Se han cobrado tus intereses. Se han sumado {self.saldo_pagar} ")
            return self
#METODO DE CLASE
    @classmethod
    def info_todas_tarjetas(cls):
        total_saldos = 0
        for tarjeta in cls.todas_las_tarjetas:
            print(id)
            print(tarjeta)
            print(tarjeta.saldo_pagar())
            print(tarjeta.limite_credito())
            print(tarjeta.interes())

    


santander = Tarjeta_de_Credito()
bci = Tarjeta_de_Credito(200000, 0.2)
lider = Tarjeta_de_Credito(150000, 0.9)
bci.mostrar_info_tarjeta()
bci.compra(100000)
bci.mostrar_info_tarjeta()
santander.compra(15000).compra(30000).pago(20000).cobrar_intereses().mostrar_info_tarjeta()
bci.compra(50000).compra(10000).pago(40000).compra(30000).cobrar_intereses().mostrar_info_tarjeta()
lider.compra(60000).compra(20000).compra(20000).compra(20000).compra(50000).mostrar_info_tarjeta()
print(Tarjeta_de_Credito.info_todas_tarjetas())