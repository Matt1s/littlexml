
from grammar import *
def find_longest_non_terminal(non_terminal, remaining_input):
    longest = ""
    for key in PARSING_TABLE[non_terminal]:
        for i in range(len(key), 0, -1):
            if key[:i] == remaining_input[:i]:
                if len(key[:i]) > len(longest):
                    longest = key[:i]
    print(f'Longest: {longest}', 'Non-terminal:', non_terminal)
    if(longest == ''):
        # Return epsilon if no match is found
        print('No match found for non-terminal:', non_terminal)
        return 'ε'
    return longest

def parse(input):
    print('\n')
    print('Parsing...')
    stack = ['$']
    STARTING_NON_TERMINAL = 'XMLDOCUMENT'
    stack.append(STARTING_NON_TERMINAL)
    i = 0
    while i < len(input):
        if input[i] == ' ':
            i+=1
            continue
        try:
            print(f'Input: {input[i]}{input[i+1]}{input[i+2]}{input[i+3]}{input[i+4]}{input[i+5]}')
        except:
            pass
        if not stack:
            return 'Error'
        print(f'Stack: {stack}')
        current = stack.pop()
        print(f'Current: {current}')
        if current in NON_TERMINALS:
            longest_non_terminal = find_longest_non_terminal(current, input[i:])
            if (current == "ENDTAG" and longest_non_terminal == 'ε'):
                stack.append('ELEMENT``')
                current = 'ELEMENT``'
            if longest_non_terminal and longest_non_terminal in PARSING_TABLE[current]:
                if(current != 'NAMECHAR'):
                    rule = PARSING_TABLE[current][longest_non_terminal]
                    print(f'Rule: {rule}')
                if current == 'DIGIT':
                    # Treat the digit as a terminal because it is a single character because '29: DIGIT -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9',
                    if input[i] in DIGIT:
                        rule = input[i]
                        stack.append(rule)
                        print(f'Pushed rule DIGIT: {rule}')
                    else:
                        print('Error because of digit', input[i])
                elif current == 'LETTER':
                    # Treat the letter as a terminal because it is a single character because '25: LETTER -> a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z',
                    if input[i] in LETTER:
                        rule = input[i]
                        stack.append(rule)
                        print(f'Pushed rule LETTER: {rule}')
                    else:
                        print('Error because of letter', input[i])
                elif current == 'NAMECHAR':
                    # Treat the namechar as a terminal because it is a single character because '26: NAMECHAR -> LETTER | DIGIT | . | - | _',
                    if input[i] in LETTER or input[i] == '.' or input[i] == '-' or input[i] == '_' or input[i] in DIGIT or input[i] == ' ':
                        rule = input[i]
                        stack.append('NAMECHAR')
                        stack.append(rule)
                        print(f'Pushed rule NAMECHAR: {rule}')
                    else:
                        print('Error because of namechar', input[i])
                else:
                    rule = RULES_SEPARATED[rule - 1].split(' -> ')[1].split(' ')
                    print("Split rule: ", rule)
                    # if there are rules <?xml, version=", beside each other in rule, merge them
                    rule.reverse()
                    for r in rule:
                        if r == "<?xml":
                            r = '<?xml version="'
                            stack.remove('version="')
                            print(f'Popped version=" as it is part of the rule <?xml version="')
                        stack.append(r)
                        print(f'Pushed rule not DIGIT or LETTER: {r}')
            elif longest_non_terminal == 'ε':
                print('Pushed ε')
                stack.append('ε')
            else:
                return 'Error because of non-terminal'
        elif current == input[i]:
            print('Matched terminal')
            i+=len(current)
        else:
            print('Terminal found in non-terminal rules')
            # i+= length of the current terminal, also pop it from stack
            if(current != 'ε' ):
                i+=len(current)

    if not stack:
        return 'Success'
    return 'Error because of stack'

def main():
    # Reading the input file as utf-8, splitting the input examples by the empty line
    with open('input.txt', 'r', encoding='utf-8') as file:
        examples = file.read().split('\n\n')
        #for example in examples:
        example = examples[0]
        #print(f'Example\n: {example}')
        # Strip end of line characters as well as empty characters on the start of all lines
        example_lines = example.split('\n')
        example_stripped = []
        for line in example_lines:
            line_stripped = line.strip().replace('\n', '')
            print(line_stripped)
            if line_stripped:
                example_stripped.append(line_stripped)
        example_stripped = ''.join(example_stripped)
        print(f'Example: {example_stripped}')
        print('Parsing...')
        print(parse(example_stripped))


if __name__ == '__main__':
    main()


