from AST import AST
from NFA import NFA

class Compiler:
    def __init__(self):
        self.nfa = NFA()

    def compile(self, ast):
        self.nfa = NFA()
        self._process_node(ast.get_root())

    def _process_node(self, node):
        node_type = node.get_value()
        
        if node_type == "Concatenation":
            self._process_concatenation(node)
        elif node_type == "Alternation":
            self._process_alternation(node)
        elif node_type == "Character":
            self._process_character(node)
        elif node_type == "Repetition":
            self._process_repetition(node)
        # Handle other node types as needed
        
    def _process_concatenation(self, node):
        children = node.get_children()
        if len(children) == 2:
            self._process_node(children[0])
            self._process_node(children[1])
            
            last_accepting_states = self._get_accepting_states(children[0])
            initial_states = self._get_initial_states(children[1])
            
            for state in last_accepting_states:
                self.nfa.add_transition(state, "", initial_states)
            
            self._set_initial_and_accepting_states(
                self._get_initial_states(children[0]), self._get_accepting_states(children[1])
            )
            
        # Handle invalid AST structure for concatenation if needed
    
    def _process_alternation(self, node):
        children = node.get_children()
        if len(children) == 2:
            self._process_node(children[0])
            self._process_node(children[1])
            
            initial_state = NFA.State()
            accepting_state = NFA.State()
            
            self.nfa.add_state(initial_state)
            self.nfa.add_state(accepting_state)
            
            self.nfa.add_transition(initial_state, "", self._get_initial_states(children[0]))
            self.nfa.add_transition(initial_state, "", self._get_initial_states(children[1]))
            
            self._set_initial_and_accepting_states(initial_state, accepting_state)
            
            self.nfa.add_transition(self._get_accepting_states(children[0]), "", accepting_state)
            self.nfa.add_transition(self._get_accepting_states(children[1]), "", accepting_state)
            
        # Handle invalid AST structure for alternation if needed
    
    def _process_character(self, node):
        character = node.get_value()
        
        initial_state = NFA.State()
        accepting_state = NFA.State()
        
        self.nfa.add_state(initial_state)
        self.nfa.add_state(accepting_state)
        self.nfa.add_transition(initial_state, character, accepting_state)
        
        self._set_initial_and_accepting_states(initial_state, accepting_state)
    
    def _process_repetition(self, node):
        child = node.get_children()[0]
        self._process_node(child)
        
        initial_state = NFA.State()
        accepting_state = NFA.State()
        
        self.nfa.add_state(initial_state)
        self.nfa.add_state(accepting_state)
        
        self.nfa.add_transition(initial_state, "", self._get_initial_states(child))
        self.nfa.add_transition(self._get_accepting_states(child), "", accepting_state)
        self.nfa.add_transition(self._get_accepting_states(child), "", self._get_initial_states(child))
        self.nfa.add_transition(initial_state, "", accepting_state)
        
        self._set_initial_and_accepting_states(initial_state, accepting_state)
    
    def _get_initial_states(self, node):
        if isinstance(node, AST.Node):
            return node.get_data("initial_states")
        return set()
    
    def _get_accepting_states(self, node):
        if isinstance(node, AST.Node):
            return node.get_data("accepting_states")
        return set()
    
    def _set_initial_and_accepting_states(self, initial_state, accepting_state):
        self.nfa.set_initial_state(initial_state)
        self.nfa.add_accepting_state(accepting_state)
    
