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
        self.used_super = False
    
    def attack(self, attack, attacked_monster):
        damage = 0
        print(attack)
        if   attack == 1:
            #Rasengan
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 2:
            # Spirit Ball
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 3:
            # drago distorsione
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 4:
            # roccia fonda
            power = 60
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 5:
            #coleo trapano
            power = 15
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 6:
            # gatgraffio
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 7:
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 8:
            power = 60
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 9:
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 10:
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 11:
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 12:
            power = 60
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 13:
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 14:
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 15:
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 16:
            power = 60
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 17:
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 18:
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 19:
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 20:
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 21:
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        elif attack == 22:
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        else:
            power = 25
            damage = int(power*(self.ATK/attacked_monster.DEF)*random.uniform(0.85, 1))
        print(damage)
        attacked_monster.actual_PS = max(0, attacked_monster.actual_PS - damage)

    def text_moves_list(self):
        text = " "
        for i, move in enumerate(self.moveset):
            text+= str(i+ 1) + ")" + move_name(move) + " "
        return text
    
    def move(self, index):
        return self.moveset[index]