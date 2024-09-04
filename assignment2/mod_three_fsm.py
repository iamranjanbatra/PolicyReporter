from .fsm import FSM    
class ModThreeFSM:
    def __init__(self):
        states = ['S0', 'S1', 'S2']
        alphabet = ['0', '1']
        initial_state = 'S0'
        final_states = ['S0', 'S1', 'S2']
        transitions = {
            'S0': {'0': 'S0', '1': 'S1'},
            'S1': {'0': 'S2', '1': 'S0'},
            'S2': {'0': 'S1', '1': 'S2'}
        }
        self.fsm = FSM(states, alphabet, initial_state, final_states, transitions)

    def compute_remainder(self, binary_string):
        final_state = self.fsm.run(binary_string)
        return {'S0': 0, 'S1': 1, 'S2': 2}[final_state]
    