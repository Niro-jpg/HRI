class State:
    def __init__(self, state_name, state_question, state_answers, pointed_states_names):
        self.state_name = state_name
        self.state_question = state_question
        self.state_answers = state_answers
        self.pointed_states_names = pointed_states_names 
        self.pointed_states = []
        
    def name(self):
        return self.state_name

    def answer_name(self, index):
        return self.answer[index]

    def connect_state(self, index, state):
        self.pointed_states.append(state)

    def get_pointed_states_name(self):
        return self.pointed_states_names

    def question(self):
        return self.state_question

    def answers(self):
        return self.state_answers

    def pointed_state_answer(self, answer):
        index = self.state_answers.index(answer)
        return self.pointed_states[index]

    def pointed_state_name(self, answer):
        index = self.state_answers.index(answer)
        return self.pointed_states_names[index]