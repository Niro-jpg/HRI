import random
from utils import *

class Monster:
    def __init__(self, name, PS, ATK, DEF, SPE, moveset, type_1, type_2):
        self.name = name
        self.PS = PS
        self.actual_PS = PS
        self.ATK = ATK
        self.DEF = DEF
        self.SPE = SPE
        self.moveset = moveset
        self.type_1 = type_1
        self.type_2 = type_2
    
    def attack(self, attack, attacked_monster):
        damage = 0
        if   attack == 1:
            #Rasengan
            power = 60
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 2:
            # Spirit Ball
            power = 30
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 3:
            # drago distorsione
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 4:
            # roccia fonda
            power = 40
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 5:
            #coleo trapano
            power = 15
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 6:
            # gatgraffio
            print("Hai selezionato il caso 2.")
        elif attack == 7:
            print("Hai selezionato il caso 3.")
        elif attack == 8:
            print("Hai selezionato il caso 2.")
        elif attack == 9:
            print("Hai selezionato il caso 3.")
        elif attack == 10:
            print("Hai selezionato il caso 2.")
        else:
            print("Caso non valido.")
        attacked_monster.actual_PS = max(0, attacked_monster.actual_PS - damage)

    def text_moves_list(self):
        text = " "
        for i, move in enumerate(self.moveset):
            text+= str(i+ 1) + ")" + move_name(move) + " "
        return text