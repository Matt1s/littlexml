
from grammar import *
def find_longest_non_terminal(non_terminal):
    longest = ""
    for key in PARSING_TABLE[non_terminal]:
        if key == 'ε':
            continue
        if len(key) > len(longest):
            longest = key
    return longest

def parse(input):
    print('\n')
    print('Parsing...')
    stack = ['$']
    STARTING_NON_TERMINAL = 'XMLDOCUMENT'
    stack.append(STARTING_NON_TERMINAL)
    i = 0
    while i < len(input):
        print(f'Index: {i}')
        print(f'Input: {input[i]}{input[i+1]}{input[i+2]}')
        if not stack:
            return 'Error'
        print(f'Stack: {stack}')
        current = stack.pop()
        print(f'Current: {current}')
        if current in NON_TERMINALS:
            longest_non_terminal = find_longest_non_terminal(current)
            if longest_non_terminal and longest_non_terminal in PARSING_TABLE[current]:
                rule = PARSING_TABLE[current][longest_non_terminal]
                print(f'Rule HERE: {rule}')
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
                    if input[i] in LETTER or input[i] == '.' or input[i] == '-' or input[i] == '_':
                        rule = input[i]
                        stack.append(rule)
                        print(f'Pushed rule NAMECHAR: {rule}')
                    else:
                        print('Error because of namechar', input[i])
                else:
                    rule = RULES_SEPARATED[rule - 1].split(' -> ')[1].split(' ')
                    # if there are rules <?xml, version=", beside each other in rule, merge them
                    rule.reverse()
                    for r in rule:
                        if r == "<?xml":
                            r = '<?xml version="'
                            stack.remove('version="')
                            print(f'Popped version=" as it is part of the rule <?xml version="')
                        stack.append(r)
                        print(f'Pushed rule not DIGIT or LETTER: {r}')
            elif '$' in PARSING_TABLE[current]:
                rule = PARSING_TABLE[current]['$']
                print(f'Rule 3: {rule}')
                if isinstance(rule, int):
                    rule = RULES_SEPARATED[rule - 1].split(' -> ')[1].split(' ')
                    rule.reverse()
                    for r in rule:
                        stack.append(r)
                        print(f'Pushed rule 4: {r}')
                elif rule == 'ε':
                    pass
                else:
                    stack.append(rule)
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


