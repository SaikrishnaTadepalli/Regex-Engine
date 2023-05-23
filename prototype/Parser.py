from AST import AST, Node

class Parser:
    def __init__(self):
        self.ast = AST()
        self.tokens = []
        self.current_token = None

    def parse(self, pattern):
        self.tokens = self.tokenize(pattern)
        self.current_token = self.tokens.pop(0)
        self.ast.set_pattern(pattern)
        self.ast.set_root(self.parse_expression())
        return self.ast

    def tokenize(self, pattern):
        # Implement tokenization of the input pattern
        # Split the pattern into tokens (e.g., characters, metacharacters)
        tokens = []
        # Your tokenization logic here...
        return tokens

    def parse_expression(self):
        # Recursive parsing algorithm for expression
        node = self.parse_term()

        while self.current_token == "|":
            self.consume_token("|")
            node = Node("|", [node, self.parse_term()])

        return node

    def parse_term(self):
        # Recursive parsing algorithm for term
        node = self.parse_factor()

        while self.current_token not in [")", "|", None]:
            next_node = self.parse_factor()
            node = Node(".", [node, next_node])

        return node

    def parse_factor(self):
        # Recursive parsing algorithm for factor
        if self.current_token == "(":
            self.consume_token("(")
            node = self.parse_expression()
            self.consume_token(")")
            return node
        elif self.current_token in ["*", "+", "?"]:
            operator = self.current_token
            self.consume_token(operator)
            return Node(operator, [self.parse_factor()])
        else:
            value = self.current_token
            self.consume_token(value)
            return Node(value)

    def consume_token(self, expected_token):
        if self.current_token == expected_token:
            if len(self.tokens) > 0:
                self.current_token = self.tokens.pop(0)
            else:
                self.current_token = None
        else:
            raise Exception(f"Expected token '{expected_token}', but found '{self.current_token}'.")

# # Test the parser
# parser = Parser()
# ast = parser.parse("a(b|c)*")
# # Print the built AST
# print(ast.get_root().get_value())
