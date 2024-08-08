from Monster import *
from utils import *
import time
from name_to_animation import name_to_animation

class Battle:
    def __init__(self, ally_monster_index = 3, enemy_monster_index = 2, pepper = False, robot = None):
        self.robot = robot
        self.ally_monster = self.get_monster(ally_monster_index)
        self.enemy_monster = self.get_monster(enemy_monster_index)
        self.moves_list = Moves_List()
        self.pepper = pepper
        self.phrases = self.get_phrases(enemy_monster_index)
        
    def get_monster(self, index):
        if (index == 0 or index == "Naruto" or index == "naruto"):
            return Monster("Naruto", 100, 10, 10, 10, [5,6,7,8], "erba", "fuoco")
        elif(index == 1 or index == "Goku" or index == "goku"):
            return Monster("Goku", 100, 10, 10, 10, [1,2,3,4], "erba", "fuoco")
        elif(index == 2 or index == "Goldrake" or index == "goldrake"):
            return Monster("Goldrake", 100, 10, 10, 10, [13,14,15,16], "erba", "fuoco")
        elif(index == 3 or index == "Terminator" or index == "terminator"):
            return Monster("Terminator", 100, 10, 10, 10, [9,10,11,12], "erba", "fuoco")
        else:
            return Monster("Terminator", 100, 10, 10, 10, [9,10,11,12], "erba", "fuoco")
        
    def get_phrases(self,index):
        starting_phrase = 'HI, let s battle' 
        combat_phrases = ['I ll win!', 'you re strong!']
        win_phrase = ' I Won'
        loose_phrase = 'I lost'
            
        if (index == 0 or index == "Naruto" or index == "naruto"):
            #Naruto
            starting_phrase = 'I will become HOKAGE!!' 
            combat_phrases = ['Help me Kurama', 'I will take Sasuke back!']
            win_phrase = 'This is the power of a future HOKAGE'
            loose_phrase = 'NOOOOO, the leaf villaaaage!!'
        elif(index == 1 or index == "Goku" or index == "goku"):
            #Goku
            starting_phrase = 'This is gonna be fun' 
            combat_phrases = ['Show me your best!', 'you re strong!']
            win_phrase = ' It was a nice fight'
            loose_phrase = 'Looks like I am gonna train more!'
        elif(index == 2 or index == "Goldrake" or index == "goldrake"):
            #Goldrake
            starting_phrase = 'GOLDRAKE! COME ON!' 
            combat_phrases = ['I ll defeat you and then Vega', ' i will protect my planet!']
            win_phrase = 'I will always protect my people!'
            loose_phrase = 'Fleed.... I am.... sorry....'
        elif(index == 3 or index == "Terminator" or index == "terminator"):
            #Terminator
            starting_phrase = 'I have come from the future to terminate you' 
            combat_phrases = ['Tell me where is Sarah Connor', 'I am the peak of the future technology, surrender!']
            win_phrase = ' You cannot beat the skynet!'
            loose_phrase = 'I ll be back'
        
        return Phrases(starting_phrase = starting_phrase, 
            combat_phrases = combat_phrases,
            win_phrase = win_phrase,
            loose_phrase = loose_phrase)
        
    def start_battle(self):
        self.robot_print(self.phrases.starting_phrase)
        self.wait_move()
        
    def battle_state(self):
        state_text = self.ally_monster.name + "        " + self.enemy_monster.name + "\n"  + "      types" + "\n" + self.ally_monster.type_1 + "      " + self.enemy_monster.type_1 + "\n"  + self.ally_monster.type_2 + "      " + self.enemy_monster.type_2 + "\n" + "    life:"+ "\n" + str(self.ally_monster.PS) + "       " + str(self.ally_monster.PS) + "\n" + "actual life:"+ "\n" + str(self.ally_monster.actual_PS) + "       " + str(self.ally_monster.actual_PS) 
        return state_text
    
    def wait_move(self):
        while True:
            self.robot_print(" which move do you choose between:\n" + self.ally_monster.text_moves_list())
            move = raw_input()
            is_int = is_convertible_to_int(move)
            if is_int:
                move = int(move)
                if not 0 < int(move) < 5:
                    self.robot_print("invalid move")
                elif is_super_move(self.ally_monster.move(int(move) - 1)) and self.ally_monster.used_super:
                    self.robot_print("super already used")
                else:
                    if (is_super_move(self.ally_monster.move(int(move) - 1))):
                        self.ally_monster.used_super = True
                    selected_ally_move = Move(self.ally_monster, self.ally_monster.move(int(move) - 1), 1, True)
                    self.moves_list.add_move(selected_ally_move)
                    while True:
                        random_move = random.randint(0,3)
                        if not (is_super_move(self.enemy_monster.move(random_move))):
                            break
                        elif not (self.enemy_monster.used_super ):
                            break
                    if (is_super_move(self.enemy_monster.move(random_move))):
                        self.enemy_monster.used_super = True
                    selected_enemy_move = Move(self.enemy_monster, self.enemy_monster.move(random_move), 1, False)
                    self.moves_list.add_move(selected_enemy_move)
                    break
            else:
                self.robot_print("I do not understand")
        self.moves_list.sort_list_speed()
        self.solve_actions()
    
    def solve_actions(self):
        if (self.moves_list.len() == 0): 
            #print(self.battle_state())
            self.wait_move()
        else:
            move = self.moves_list.pop_first()
            if move.player: self.solve_player_action(move)
            else: self.solve_enemy_action(move)

    def solve_player_action(self, move):
        phrase = "You use " + move.name() + " on the opponent"
        self.robot_print(phrase)
        self.ally_robot_interaction(animation = 0)
        self.ally_monster.attack(move.selected_move, self.enemy_monster)
        self.continue_or_end()

    def solve_enemy_action(self, move):
        phrase = self.phrases.random_combat_phrase()
        if phrase != 0: self.robot_print(phrase)
        if(move.selected_move == 12):
            self.enemy_robot_interaction(animation = move.selected_move)
            self.enemy_monster.attack(move.selected_move, self.ally_monster)
            
        else:
            phrase = "the opponent strikes you with " + move.name()
            self.robot_print(phrase)
            self.enemy_robot_interaction(animation = move.selected_move)
            self.enemy_monster.attack(move.selected_move, self.ally_monster)
        self.continue_or_end()

    def check_end_battle(self):
        if (self.ally_monster.actual_PS == 0 and self.enemy_monster.actual_PS == 0):
            return 0
        elif(self.ally_monster.actual_PS == 0):
            return 1
        elif(self.enemy_monster.actual_PS == 0):
            return 2
        else:
            return 3

    def end_battle(self, result):
        if(result == 0):
            self.robot_print("Draw")
        elif(result == 1):
            self.robot_print(self.phrases.win_phrase)
        elif(result == 2):
            self.robot_print(self.phrases.loose_phrase)

    def continue_or_end(self):
        result = self.check_end_battle()
        if (result == 3):
            self.solve_actions()
        else:
            self.end_battle(result)

    def ally_robot_interaction(self, animation = 0):
        if(self.pepper):
            time.sleep(1)
            name_to_animation("damage", self)

    def enemy_robot_interaction(self,animation = 0):
        if(self.pepper):
            time.sleep(1)
            name_to_animation(animation_name(animation), self)
            
    def robot_print(self, phrase):
        if self.pepper:
            self.robot.say(phrase)
        else :
            print(phrase)

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
    
class Phrases:
    def __init__(self, starting_phrase = 'HI, let s battle', combat_phrases = ['I ll win!', 'you re stron!'], win_phrase = ' I Won', loose_phrase = 'I lost' ):
        self.starting_phrase = starting_phrase
        self.combat_phrases = combat_phrases
        self.win_phrase = win_phrase
        self.loose_phrase = loose_phrase
        self.used_phrases = []
        for i in range(len(combat_phrases)):
            self.used_phrases.append(1)
        self.phrases_counter = len(combat_phrases)

    def random_combat_phrase(self):
        if self.phrases_counter == 0: return 0
        self.phrases_counter-=1
        while True:
            random_phrase = random.randint(0,len(self.combat_phrases) - 1)
            if self.used_phrases[random_phrase] == 1:
                self.used_phrases[random_phrase] = 0
                return self.combat_phrases[random_phrase]


class Move:
    def __init__(self, monster, selected_move, speed, player):
        self.monster = monster
        self.selected_move = selected_move
        self.speed = speed
        self.player = player

    def name(self):

        return move_name(self.selected_move)
    
    def animation(self):
        
        return animation_name(self.selected_move)