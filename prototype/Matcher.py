class Matcher:
    def __init__(self):
        pass

    def match(self, dfa, text):
        current_state = dfa.get_initial_state()

        for char in text:
            current_state = self.transition(dfa, current_state, char)
            if current_state is None:
                return False

        return current_state in dfa.get_accepting_states()

    def transition(self, dfa, state, char):
        transition = dfa.transition(state, char)
        return transition
