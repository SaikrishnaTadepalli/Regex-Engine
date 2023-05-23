from DFA import DFA
from collections import deque


class NFAToDFAConverter:
    def __init__(self):
        pass

    def convert_nfa_to_dfa(self, nfa):
        dfa = DFA()
        initial_state = self.epsilon_closure(nfa, {nfa.get_initial_state()})
        dfa.add_state(initial_state)
        dfa.set_initial_state(initial_state)

        unmarked_states = deque([initial_state])
        marked_states = set()

        while unmarked_states:
            current_state = unmarked_states.popleft()
            marked_states.add(current_state)

            for symbol in self.get_alphabet(nfa):
                next_state = self.epsilon_closure(nfa, self.move(nfa, current_state, symbol))

                if next_state not in marked_states:
                    unmarked_states.append(next_state)
                    marked_states.add(next_state)

                dfa.add_transition(current_state, symbol, next_state)

                if next_state.intersection(nfa.get_accepting_states()):
                    dfa.add_accepting_state(next_state)

        return dfa

    def epsilon_closure(self, nfa, states):
        closure = set(states)
        stack = list(states)

        while stack:
            current_state = stack.pop()
            epsilon_transitions = nfa.transition(current_state, None)

            if epsilon_transitions:
                for state in epsilon_transitions:
                    if state not in closure:
                        closure.add(state)
                        stack.append(state)

        return frozenset(closure)

    def move(self, nfa, states, symbol):
        result = set()

        for state in states:
            transitions = nfa.transition(state, symbol)

            if transitions:
                result.update(transitions)

        return result

    def get_alphabet(self, nfa):
        alphabet = set()

        for (state, symbol) in nfa.get_transitions().keys():
            if symbol is not None:
                alphabet.add(symbol)

        return alphabet
