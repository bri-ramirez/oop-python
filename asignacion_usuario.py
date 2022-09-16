from usuario import Usuario


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