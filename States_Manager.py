from State import *

class States_Manager:
    def __init__(self, init_enviroment = True):
        self.actual_state = None
        self.states_list = []
        if init_enviroment:
            self.init_enviroment()
    
    def init_enviroment(self):
        initial_state = State("initial_state", "come va?",["bene", "male"],["initial_state", "mid"])
        self.actual_state = initial_state
        self.states_list.append(initial_state)
        state_1 = State("mid", "come va?",["bene", "male"],["mid", "finish"])
        self.states_list.append(state_1)
        state_2 = State("finish", "come va?",["bene", "male"],["finish", "exit"])
        self.states_list.append(state_2)
        self.connect_states()
    
    def connect_states(self):
        for i, state_to_connect in enumerate(self.states_list):
            for j, target_state_name in enumerate(state_to_connect.get_pointed_states_name()):
                for k, target_state in enumerate(self.states_list):
                    if (target_state_name == target_state.name()):
                        state_to_connect.connect_state(0, target_state)
                        print("------------------",target_state.name())
    def start(self):
        while True:
            print(self.actual_state.name())
            text_input = input(self.show_actual_state())
            if (text_input in self.actual_state.answers()):
                if(self.actual_state.pointed_state_name(text_input) == "exit"):
                    print("exiting")
                    break
                self.actual_state = self.actual_state.pointed_state_answer(text_input)
    
    def show_actual_state(self):
        phrase = self.actual_state.question()
        return phrase

