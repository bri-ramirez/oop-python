class Usuario:

    mis_cuentas = []

    def __init__(self, name, email, cuenta):
        self.name = name
        self.email = email
        # self.cuenta = cuenta # es una instancia de cuenta bancaria

        self.mis_cuentas.append(cuenta)

    # agregando el método de depósito
    def hacer_deposito(self, amount, num_cuenta = 0):	# toma un argumento que es el monto del depósito
        self.mis_cuentas[num_cuenta].deposito(amount)
        # self.cuenta.deposito(amount)
        return self

    # la cuenta del usuario específico aumenta en la cantidad del valor recibido
    def hacer_retiro(self, amount, num_cuenta = 0):
        self.mis_cuentas[num_cuenta].retiro(amount)
        # self.cuenta.retiro(amount)
        return self

    # haz que este método imprima el nombre del usuario y el balance de cuenta en la terminal 
    def mostrar_balance_usuario(self, num_cuenta = 0):
        print(f"Usuario: {self.name}, Balance: ${self.mis_cuentas[num_cuenta].balance}")
        # print(f"Usuario: {self.name}, Balance: ${self.cuenta.balance}")
        return self

    def crear_nueva_cuenta(self, cuenta_nueva):
        self.mis_cuentas.append(cuenta_nueva)
        return self