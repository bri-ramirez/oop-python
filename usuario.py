class Usuario:		# esto es lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0

    # agregando el método de depósito
    def hacer_deposito(self, amount):	# toma un argumento que es el monto del depósito
        self.balance_cuenta += amount
        return self

    # la cuenta del usuario específico aumenta en la cantidad del valor recibido
    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
        return self

    # haz que este método imprima el nombre del usuario y el balance de cuenta en la terminal 
    def mostrar_balance_usuario(self):
        # Ej.: “Usuario: Guido van Rossum, Balance: $150
        print("Usuario:", self.name + ", Balance: $" + str(self.balance_cuenta))
        return self

    def transferir_dinero(self,amount, user):
        self.hacer_retiro(amount)
        user.hacer_deposito(amount)
        return self