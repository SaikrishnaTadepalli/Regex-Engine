import sys
from RegexEngine import RegexEngine

'''
# def main():
#     if len(sys.argv) < 3:
#         print("Usage: python main.py <pattern> <text>")
#         return

#     pattern = sys.argv[1]
#     text = sys.argv[2]

#     engine = RegexEngine()
#     result = engine.run(pattern, text)

#     if (result):
#         print("\nYour text matched your pattern!\n")
#     else:
#         print("\nYour text didn't match your pattern!\n")

# if __name__ == '__main__':
#     main()
'''

regexEngine = RegexEngine()

def Main():
    print("\n--------------------------------------------------------")
    print("\t\tWelcome to the Regex-Engine\t\t")
    print("--------------------------------------------------------\n")

    pattern = input('Enter your (valid) Regex-Pattern: ')
    text = input('Enter the text you want to match: ')
    
    regexEngine.run(pattern, text)
    
    result = True

    if (result):
        print("\nYour text matched your pattern!\n")
    else:
        print("\nYour text didn't match your pattern!\n")
    
    print("--------------------------------------------------------\n")

Main()