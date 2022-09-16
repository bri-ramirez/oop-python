class CuentaBancaria:
    todas_las_cuentas = []

    def __init__(self,  balance = 0, tasa_interes = 0.01): 
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        self.balance -= amount
        return self
    
    def mostrar_info_cuenta(self):
        print(self.balance)
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interes
        return self

    @classmethod
    def imprimir_todas_las_cuentas(cls):
        for cuenta in cls.todas_las_cuentas:
            print(f"balance de cuenta: {cuenta.balance}")
            # imprime la instancia como un diccionario
            # print(cuenta.__dict__)


