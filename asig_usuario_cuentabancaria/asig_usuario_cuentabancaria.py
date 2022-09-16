from cuenta_bancaria import CuentaBancaria
from usuario import Usuario

cuentaBancaria = CuentaBancaria(2000, 0.2)
bri = Usuario("Briggitte", "bri@gmail.com", cuentaBancaria)

bri.hacer_deposito(1000).mostrar_balance_usuario()

cuentaBancaria2 = CuentaBancaria()

bri.crear_nueva_cuenta(cuentaBancaria2)\
    .hacer_deposito(5000, 1)\
    .mostrar_balance_usuario(1)