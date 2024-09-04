class FSM:
    def __init__(self, states, alphabet, initial_state, final_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
        self.current_state = initial_state

    def transition(self, input_symbol):
        if input_symbol not in self.alphabet:
            raise ValueError(f"Invalid input symbol: {input_symbol}")
        self.current_state = self.transitions[self.current_state][input_symbol]

    def run(self, input_string):
        self.current_state = self.initial_state
        for symbol in input_string:
            self.transition(symbol)
        return self.current_state

    def is_accepted(self):
        return self.current_state in self.final_states

