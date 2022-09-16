from usuario import Usuario

bri = Usuario("briggitte","bri@gmail.com")
seba = Usuario("sebastian","seba@gmail.com")
fer = Usuario("fernanda","fer@gmail.com")

bri.hacer_deposito(500).hacer_deposito(1000).hacer_deposito(400).hacer_retiro(1000).mostrar_balance_usuario()

seba.hacer_deposito(1000).hacer_deposito(300).hacer_retiro(100).hacer_retiro(500).mostrar_balance_usuario()

fer.hacer_deposito(3000).hacer_retiro(500).hacer_retiro(300).hacer_retiro(800).mostrar_balance_usuario()

bri.transferir_dinero(300, fer).mostrar_balance_usuario()
fer.mostrar_balance_usuario()
