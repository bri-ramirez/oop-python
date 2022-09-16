from cuenta_bancaria import CuentaBancaria

cuenta1 = CuentaBancaria()
cuenta2 = CuentaBancaria()

cuenta1.deposito(1000) \
    .deposito(9000) \
    .deposito(400) \
    .retiro(1000) \
    .generar_interes() \
    .mostrar_info_cuenta()

cuenta2.deposito(2000) \
    .deposito(600) \
    .retiro(500) \
    .retiro(200) \
    .retiro(600) \
    .retiro(200) \
    .generar_interes() \
    .mostrar_info_cuenta()

CuentaBancaria.imprimir_todas_las_cuentas()

