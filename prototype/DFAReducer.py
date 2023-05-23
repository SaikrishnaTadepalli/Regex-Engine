from DFA import DFA

class DFAReducer:
    def __init__(self):
        pass

    def minimize_dfa(self, dfa):
        # Step 1: Split accepting and non-accepting states
        partition = [dfa.get_accepting_states(), dfa.get_states() - dfa.get_accepting_states()]

        # Step 2: Refine the partition until no further changes occur
        refined_partition = self.refine_partition(dfa, partition)

        # Step 3: Create a new reduced DFA
        reduced_dfa = DFA()

        for states in refined_partition:
            new_state = frozenset(states)

            if dfa.get_initial_state() in states:
                reduced_dfa.set_initial_state(new_state)

            reduced_dfa.add_state(new_state)

            for symbol in self.get_alphabet(dfa):
                next_state = self.get_next_state(dfa, states, symbol)
                reduced_dfa.add_transition(new_state, symbol, next_state)

                if next_state in dfa.get_accepting_states():
                    reduced_dfa.add_accepting_state(new_state)

        return reduced_dfa

    def refine_partition(self, dfa, partition):
        while True:
            new_partition = []

            for states in partition:
                split = self.split_states(dfa, states, partition)
                new_partition.extend(split)

            if new_partition == partition:
                break

            partition = new_partition

        return partition

    def split_states(self, dfa, states, partition):
        split = []

        for subgroup in partition:
            equivalent_states = []

            for state in states:
                transitions = self.get_transition_states(dfa, state)

                if transitions not in subgroup:
                    equivalent_states.append(state)

            if equivalent_states:
                split.append(equivalent_states)

        return split

    def get_transition_states(self, dfa, state):
        transitions = []

        for symbol in self.get_alphabet(dfa):
            next_state = self.get_next_state(dfa, state, symbol)
            transitions.append(next_state)

        return frozenset(transitions)

    def get_next_state(self, dfa, state, symbol):
        transition = dfa.transition(state, symbol)

        if transition is not None:
            return transition
        else:
            return None

    def get_alphabet(self, dfa):
        alphabet = set()

        for (state, symbol) in dfa.get_transitions().keys():
            if symbol is not None:
                alphabet.add(symbol)

        return alphabet
