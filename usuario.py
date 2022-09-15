class Usuario:		# esto es lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0

    # agregando el método de depósito
    def hacer_deposito(self, amount):	# toma un argumento que es el monto del depósito
        self.balance_cuenta += amount

    # la cuenta del usuario específico aumenta en la cantidad del valor recibido
    def hacer_retiro(self, amount):
        if amount > self.balance_cuenta:
            return
        self.balance_cuenta -= amount

    # haz que este método imprima el nombre del usuario y el balance de cuenta en la terminal 
    def mostrar_balance_usuario(self):
        # Ej.: “Usuario: Guido van Rossum, Balance: $150
        print("Usuario:", self.name + ", Balance: $" + str(self.balance_cuenta))

    def transferir_dinero(self,amount, user):
        self.hacer_retiro(amount)
        user.hacer_deposito(amount)


bri = Usuario("briggitte","bri@gmail.com")
seba = Usuario("sebastian","seba@gmail.com")
fer = Usuario("fernanda","fer@gmail.com")

bri.hacer_deposito(500)
bri.hacer_deposito(1000)
bri.hacer_deposito(400)
bri.hacer_retiro(1000)
bri.mostrar_balance_usuario()

seba.hacer_deposito(1000)
seba.hacer_deposito(300)
seba.hacer_retiro(100)
seba.hacer_retiro(500)
seba.mostrar_balance_usuario()

fer.hacer_deposito(3000)
fer.hacer_retiro(500)
fer.hacer_retiro(300)
fer.hacer_retiro(800)
fer.mostrar_balance_usuario()

bri.transferir_dinero(300, fer)
bri.mostrar_balance_usuario()
fer.mostrar_balance_usuario()






# print(bri.name)
# bri.hacer_deposito(1000)
# print(bri.balance_cuenta)
# bri.hacer_deposito(500)
# print(bri.balance_cuenta)
# bri.hacer_retiro(300)
# print(bri.balance_cuenta)
# bri.mostrar_balance_usuario()