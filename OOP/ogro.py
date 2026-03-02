from basicosdepaython.OOP.Enemigo import *
import random
class ogro(Enemigo):
    def __init__(self,puntos_energia=20, ataques=3):
        super().__init__(tipo_enemigos='ogro'), puntos_energia=puntos_energia, ataques=ataques

def habla(self):
    print("ogro aplastar todo!!!")

    def ataque_especial_(self):
        print("ogro ataque especial")
        funciona_ataque_especial= random.random() <0.20
        if funciona_ataque_especial:
            self.ataque += 4
            print("ogro enojado y incremento su ataque por 4")
            