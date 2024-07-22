from Monster import *
from utils import *
import time

class Battle:
    def __init__(self,ally_monster = None, enemy_monster = None, pepper = False, robot = None):
        self.robot = robot
        if (ally_monster == None):
            self.ally_monster = Monster("andre", 100, 10, 10, 10, [1,2,5,4], "erba", "fuoco")
        else:
            self.ally_monster = ally_monster
        if (ally_monster == None):
            self.enemy_monster = Monster("lucas", 100, 10, 10, 10, [1,2,3,4], "acqua", "acciaio")
        else:
            self.enemy_monster = enemy_monster   
        self.moves_list = Moves_List()
        self.pepper = pepper
        
    def start_battle(self):
        self.wait_move()
        
    def battle_state(self):
        state_text = self.ally_monster.name + "        " + self.enemy_monster.name + "\n"  + "      types" + "\n" + self.ally_monster.type_1 + "      " + self.enemy_monster.type_1 + "\n"  + self.ally_monster.type_2 + "      " + self.enemy_monster.type_2 + "\n" + "    life:"+ "\n" + str(self.ally_monster.PS) + "       " + str(self.ally_monster.PS) + "\n" + "actual life:"+ "\n" + str(self.ally_monster.actual_PS) + "       " + str(self.ally_monster.actual_PS) 
        return state_text
    
    def wait_move(self):
        while True:
            move = input(" which move do you choose between:\br" + self.ally_monster.text_moves_list())
            if not isinstance(move, int):
                print("non ho capito")
            elif not 0 < int(move) < 5:
                print("mossa non valida")
            else:
                selected_ally_move = Move(self.ally_monster, int(move), 1, True)
                self.moves_list.add_move(selected_ally_move)
                random_move = random.randint(1,4)
                selected_enemy_move = Move(self.enemy_monster, random_move, 1, False)
                self.moves_list.add_move(selected_enemy_move)
                break
        self.moves_list.sort_list_speed()
        self.solve_actions()
    
    def solve_actions(self):
        if (self.moves_list.len() == 0): 
            print(self.battle_state())
            self.wait_move()
        else:
            move = self.moves_list.pop_first()
            if move.player: self.solve_player_action(move)
            else: self.solve_enemy_action(move)

    def solve_player_action(self, move):
        phrase = "usi " + move.name() + " contro il nemico"
        self.ally_robot_interaction(phrase)
        miao = raw_input(phrase)
        self.ally_monster.attack(move.selected_move, self.enemy_monster)
        self.continue_or_end()

    def solve_enemy_action(self, move):
        phrase = "il nemico ti attacca con " + move.name()
        self.enemy_robot_interaction(phrase)
        miao = raw_input(phrase)
        self.enemy_monster.attack(move.selected_move, self.ally_monster)
        self.continue_or_end()

    def check_end_battle(self):
        if (self.ally_monster.PS == 0 and self.enemy_monster.PS == 0):
            return 0
        elif(self.ally_monster.PS == 0):
            return 1
        elif(self.enemy_monster.PS == 0):
            return 2
        else:
            return 3

    def end_battle(self, result):
        if(result == 0):
            print("pareggio")
        elif(result == 1):
            print("Vittoria!")
        elif(result == 2):
            print("Sconfitta...")

    def continue_or_end(self):
        result = self.check_end_battle()
        if (result == 3):
            self.solve_actions()
        else:
            self.end_battle(result)

    def end_battle(self, result):
        print("battaglia finita!")

    def ally_robot_interaction(self, phrase):
        if(self.pepper):
            print("pepper")
            time.sleep(1)
            self.robot.say('Character 1')

    def enemy_robot_interaction(self,phrase):
        if(self.pepper):
            print("pepper")
            time.sleep(1)
            self.robot.say('Character 1')

class Moves_List:
    def __init__(self):
        self.list = []

    def sort_list_speed(self):
        if len(self.list) <=1: return
        self.list = sorted(self.list, key=lambda x: x.speed)

    def add_move(self, move):
        self.list.append(move)
    def len(self):
        return len(self.list)
    def pop_first(self):
        return self.list.pop(0)


class Move:
    def __init__(self, monster, selected_move, speed, player):
        self.monster = monster
        self.selected_move = selected_move
        self.speed = speed
        self.player = player

    def name(self):

        attack = self.selected_move    
        name = "raggio"
        if   attack == 1:
            name = "raggio cometa"
        elif attack == 2:
            # fuoco fatuo
            name = "fuoco fatuo"
        elif attack == 3:
            # drago distorsione
            name = "drago distorsione"
        elif attack == 4:
            # roccia fonda
            name = "roccia fonda"
        elif attack == 5:
            #coleo trapano
            name = "coleo trapano"
        elif attack == 6:
            # gatgraffio
            name = "gatto graffio"
        else:
            name = "testata"
        
        return name