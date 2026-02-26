from basicosdepaython.OOP.Enemigo import *
from basicosdepaython.OOP.Zombie import *
from basicosdepaython.OOP.ogro import *

zombie = Zombie(10, 1)
Ogro = ogro(20, 3)

print(f"({zombie.get_tipo_enemigo()} tiene  {zombie. puntos_energia} de energia y ataca con {zombie.ataque} )")
print(f"({Ogro.get_tipo_enemigo()} tiene {Ogro.puntos_energia} de energia y ataca con {Ogro.ataque})")
