import sys
from RegexEngine import RegexEngine

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <pattern> <text>")
        return

    pattern = sys.argv[1]
    text = sys.argv[2]

    # Initialize the regex engine
    engine = RegexEngine()

    # Run the regex engine to compile and match the pattern against the input text
    engine.run(pattern, text)

if __name__ == '__main__':
    main()
