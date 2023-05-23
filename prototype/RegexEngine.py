from Parser import Parser
from Compiler import Compiler
from NFAToDFAConverter import NFAToDFAConverter
from DFAReducer import DFAReducer
from Matcher import Matcher

class RegexEngine:
    def __init__(self):
        self.parser = Parser()
        self.compiler = Compiler()
        self.converter = NFAToDFAConverter()
        self.reducer = DFAReducer()
        self.matcher = Matcher()

    def run(self, pattern, text):
        # Parsing
        ast = self.parser.parse(pattern)

        # Compiling
        nfa = self.compiler.compile(ast)

        # Converting
        dfa = self.converter.convert(nfa)

        # Reducing
        reduced_dfa = self.reducer.reduce(dfa)

        # Matching
        is_match = self.matcher.match(reduced_dfa, text)

        if is_match:
            groups = self.matcher.get_groups()
            print("Match found!")
            print("Groups:", groups)
        else:
            print("No match found.")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: python RegexEngine.py <pattern> <text>")
    else:
        pattern = sys.argv[1]
        text = sys.argv[2]

        engine = RegexEngine()
        engine.run(pattern, text)
