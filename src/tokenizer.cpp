#include <iostream>
#include <string>
#include <vector>

using namespace std;

/*

The tokenizer implementation can handle the basic regular expression syntax, 
but it does not support more advanced features such as lookaheads, lookbehinds, 
backreferences, and atomic groups.

Lookaheads and lookbehinds are zero-width assertions that match a pattern only 
if it is followed by or preceded by another pattern, respectively. 

Backreferences allow you to match a previously matched group again within the 
same regular expression. 

Atomic groups are a way of grouping subpatterns in such a way that they cannot 
be backtracked out of.

To support these features, the tokenizer and parser would need to be modified 
to recognize and properly handle them. GET BACK TO IT LATER

*/

vector<string> tokenize(string regex) {
    vector<string> tokens;
    string token;

    // Iterate over the input string
    for (int i = 0; i < regex.size(); i++) {
        char c = regex[i];

        // Determine the current state based on the current character
        if (c == '\\') {
            // Escape sequence state
            token += c;
            i++;
            token += regex[i];
        } else if (c == '.') {
            // Any character state
            tokens.push_back(".");
        } else if (c == '|') {
            // Alternation state
            tokens.push_back("|");
        } else if (c == '*') {
            // Kleene star state
            tokens.push_back("*");
        } else if (c == '+') {
            // Kleene plus state
            tokens.push_back("+");
        } else if (c == '?') {
            // Optional state
            tokens.push_back("?");
        } else if (c == '(') {
            // Left parenthesis state
            tokens.push_back("(");
        } else if (c == ')') {
            // Right parenthesis state
            tokens.push_back(")");
        } else if (c == '[') {
            // Character class state
            token += c;
            i++;
            while (regex[i] != ']') {
                if (regex[i] == '\\') {
                    i++;
                    token += '\\';
                }
                token += regex[i];
                i++;
            }
            token += regex[i];
            tokens.push_back(token);
            token.clear();
        } else {
            // Literal state
            token += c;
        }
    }

    // Push any remaining token to the vector
    if (!token.empty()) {
        tokens.push_back(token);
    }

    return tokens;
}

int main() {
    string regex = "a*b+c(d|e)f?[ghij]";
    vector<string> tokens = tokenize(regex);
    
    for (int i = 0; i < tokens.size(); i++) {
        cout << tokens[i] << " ";
    }
    cout << endl;

    return 0;
}
