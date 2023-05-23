class NFA:
    def __init__(self):
        self.states = set()
        self.transitions = {}
        self.initial_state = None
        self.accepting_states = set()

    def add_state(self, state):
        self.states.add(state)

    def add_transition(self, from_state, input_symbol, to_state):
        key = (from_state, input_symbol)
        if key not in self.transitions:
            self.transitions[key] = set()
        self.transitions[key].add(to_state)

    def set_initial_state(self, state):
        self.initial_state = state

    def add_accepting_state(self, state):
        self.accepting_states.add(state)

    def get_states(self):
        return self.states

    def get_transitions(self):
        return self.transitions

    def get_initial_state(self):
        return self.initial_state

    def get_accepting_states(self):
        return self.accepting_states

    def transition(self, state, input_symbol):
        key = (state, input_symbol)
        if key in self.transitions:
            return self.transitions[key]
        else:
            return None

    # Functions to manipulate and update the NFA structure
    # ...

    # Functions to perform operations on the NFA (e.g., epsilon closure, concatenation, union)
    # ...

    # Other utility functions specific to NFA management
    # ...


# -----------------------------------------------------------------------------------

# class State:
#     def __init__(self, name):
#         self.name = name

#     def get_name(self):
#         return self.name


# class NFA:
#     def __init__(self):
#         self.states = set()
#         self.transitions = {}
#         self.initial_state = None
#         self.accepting_states = set()

#     def add_state(self, state):
#         self.states.add(state)

#     def add_transition(self, from_state, input_symbol, to_states):
#         key = (from_state, input_symbol)
#         if key not in self.transitions:
#             self.transitions[key] = set()
#         self.transitions[key].update(to_states)

#     def set_initial_state(self, state):
#         self.initial_state = state

#     def add_accepting_state(self, state):
#         self.accepting_states.add(state)

#     def get_states(self):
#         return self.states

#     def get_transitions(self):
#         return self.transitions

#     def get_initial_state(self):
#         return self.initial_state

#     def get_accepting_states(self):
#         return self.accepting_states

#     def transition(self, state, input_symbol):
#         key = (state, input_symbol)
#         if key in self.transitions:
#             return self.transitions[key]
#         else:
#             return set()

#     # Functions to manipulate and update the NFA structure
#     # ...

#     # Functions to perform operations on the NFA (e.g., epsilon closure, concatenation, union)
#     # ...

#     # Other utility functions specific to NFA management
#     # ...
