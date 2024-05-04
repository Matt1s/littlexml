LETTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'š', 'č', 'ć', 'ď', 'ž', 'ľ', 'á', 'é', 'í', 'ó', 'ú', 'ý', 'ä', 'ô', 'ö', 'ü', 'ť', 'ŕ', 'ĺ', 'ň',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Š', 'Č', 'Ć', 'Ď', 'Ž', 'Ľ', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ý', 'Ä', 'Ô', 'Ö', 'Ü', 'Ť', 'Ŕ', 'Ĺ', 'Ň']

DIGIT = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

ASCII = ['.','-','!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '/', ';', '=', '?', '@', '[', ']', '^', '_', '{', '|', '}', '~']

RULES_SECOND_REVISION = {
    'XMLDOCUMENT': (
        ['XMLDECL ELEMENT'], 
        ['ELEMENT']  
    ),
    'XMLDECL': ['<?xml version ="', 'VERNUMB','"?>'], 
    'VERNUMB': ['NUMBER', '.', 'NUMBER'], 
    'ELEMENT': ['<', 'NAME', 'ELEMENT``'], 
    'ELEMENT`': (
        ['WORDS', 'ENDTAG'], 
        ['ELEMENTS', 'ENDTAG']
    ),
    'ELEMENT``': (
        ['/>'],
        ['>', 'ELEMENT`']
    ),
    'ENDTAG': ['</', 'NAME'],
    'WORDS': (
        ['WORD'],
        ['ε']
    ),
    'ELEMENTS': (
        ['ELEMENT'], 
        ['ε']
    ),
    'NAME': (
        ['LETTER', 'NAMECHAR'],
        [' ', 'NAMECHAR'],
        [':', 'NAMECHAR']
    ),
    'NAMECHAR': (
        ['LETTER', 'NAMECHAR'],
        ['DIGIT', 'NAMECHAR'],
        ['.', 'NAMECHAR'],
        ['-', 'NAMECHAR'],
        [':', 'NAMECHAR'],
        [' ', 'NAMECHAR'],
        ['ε']
    ),
    'LETTER': LETTER,
    'NUMBER': ['DIGIT', 'NUMBER`'], 
    'NUMBER`': (
        ['DIGIT', 'NUMBER`'],
        ['ε']
    ),
    'DIGIT': DIGIT, 
    'WORD': ['CHAR', 'WORD`'],
    'WORD`': (
        ['CHAR', 'WORD`'],
        ['ε']
    ),
    'CHAR': (
        LETTER,
        DIGIT,
        ' ',
        '.',
        ':',
        '-',
        '?',
        '!'
    )
}

RULES_SEPARATED = [
    '1: XMLDOCUMENT -> XMLDECL ELEMENT',
    '2: XMLDOCUMENT -> ELEMENT',
    '3: XMLDECL -> <?xml version=" VERNUMB "?>',
    '4: VERNUMB -> NUMBER . NUMBER',
    '5: ELEMENT -> < NAME ELEMENT``',
    '6: ELEMENT` -> WORDS ENDTAG',
    '7: ELEMENT` -> ELEMENTS ENDTAG',
    '8: ELEMENT`` -> />',
    '9: ELEMENT`` -> > ELEMENT`',
    '10: ENDTAG -> </ NAME',
    '11: WORDS -> WORD',
    '12: WORDS -> ε',
    '13: ELEMENTS -> ELEMENT',
    '14: ELEMENTS -> ε',
    '15: NAME -> LETTER NAMECHAR',
    '16: NAME -> NAMECHAR',
    '17: NAME -> : NAMECHAR',
    '18: NAMECHAR -> LETTER NAMECHAR',
    '19: NAMECHAR -> DIGIT NAMECHAR',
    '20: NAMECHAR -> . NAMECHAR',
    '21: NAMECHAR -> - NAMECHAR',
    '22: NAMECHAR ->  NAMECHAR',
    '23: NAMECHAR -> : NAMECHAR',
    '24: NAMECHAR -> ε',
    '25: LETTER -> a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | š | č | ć | ď | ž | ľ | á | é | í | ó | ú | ý | ä | ô | ö | ü | ť | ŕ | ĺ | ň | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | Š | Č | Ć | Ď | Ž | Ľ | Á | É | Í | Ó | Ú | Ý | Ä | Ô | Ö | Ü | Ť | Ŕ | Ĺ | Ň',
    '26: NUMBER -> DIGIT NUMBER`',
    '27: NUMBER` -> DIGIT NUMBER`',
    '28: NUMBER` -> ε',
    '29: DIGIT -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9',
    '30: WORD -> CHAR WORD`',
    '31: WORD` -> CHAR WORD`',
    '32: WORD` -> ε',
    '33: CHAR -> LETTER',
    '34: CHAR -> DIGIT',
    '35: CHAR ->  ',
    '36: CHAR -> .',
    '37: CHAR -> :',
    '38: CHAR -> -',
    '39: CHAR -> ?',
    '40: CHAR -> !'
]

NON_TERMINALS = [
    'XMLDOCUMENT',
    'XMLDECL',
    'VERNUMB',
    'ELEMENT',
    'ELEMENT`',
    'ELEMENT``',
    'ENDTAG',
    'WORDS',
    'ELEMENTS',
    'NAME',
    'NAMECHAR',
    'LETTER',
    'NUMBER',
    'NUMBER`',
    'DIGIT',
    'WORD',
    'WORD`',
    'CHAR'
]


PARSING_TABLE = {
    'XMLDOCUMENT': {
        '<?xml version="': 1,
        '<': 2
    },
    'XMLDECL': {
        '<?xml version="': 3,
    },
    'VERNUMB':{
        '0': 4,
        '1': 4,
        '2': 4,
        '3': 4,
        '4': 4,
        '5': 4,
        '6': 4,
        '7': 4,
        '8': 4,
        '9': 4
    },
    'ELEMENT': {
        '<': 5
    },
    'ELEMENT`': {
        '<': 7,
        '</': 7,
        ', '.join(LETTER + DIGIT + ASCII): 6
    },
    'ELEMENT``': {
        '>': 9,
        '/>': 8
    },
    'ENDTAG': {
        '</': 10
    },
    'WORDS': {
        ', '.join(LETTER + DIGIT + ASCII): 11,
        '</': 12
    },
    'ELEMENTS': {
        '</': 14,
        '<': 13,
    },
    'NAME': {
        ', '.join(LETTER): 15,
        ' ': 16,
        ':': 17
    },
    'NAMECHAR': {
        ', '.join(LETTER): 18,
        ', '.join(DIGIT): 19,
        '.': 20,
        '-': 21,
        ' ': 22,
        ':': 23,
        ', '.join(['/>', '>']): 24,
    },
    'LETTER': {
        ', '.join(LETTER): 25
    },
    'NUMBER': {
        '0': 26,
        '1': 26,
        '2': 26,
        '3': 26,
        '4': 26,
        '5': 26,
        '6': 26,
        '7': 26,
        '8': 26,
        '9': 26
    },
    'NUMBER`': {
        ', '.join(DIGIT): 27,
        '"?>': 28
    },
    'DIGIT': {
        '0': 29,
        '1': 29,
        '2': 29,
        '3': 29,
        '4': 29,
        '5': 29,
        '6': 29,
        '7': 29,
        '8': 29,
        '9': 29
    },
    'WORD': {
        ', '.join(LETTER + DIGIT + ASCII): 30,
    },
    'WORD`': {
        ', '.join(LETTER + DIGIT + ASCII): 31,
        '</': 32
    },
    'CHAR': {
        ', '.join(LETTER): 33,
        ', '.join(DIGIT): 34,
        ' ': 35,
        '.': 36,
        ':': 37,
        '-': 38,
        '?': 39,
        '!': 40,
    }
}

FIRST = {
    '1: <?xml version="',
    '2: <',
    '3: <?xml version="',
    '4: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9',
    '5: <', 
    '6: a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | š | č | ć | ď | ž | ľ | á | é | í | ó | ú | ý | ä | ô | ö | ü | ť | ŕ | ĺ | ň | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | Š | Č | Ć | Ď | Ž | Ľ | Á | É | Í | Ó | Ú | Ý | Ä | Ô | Ö | Ü | Ť | Ŕ | Ĺ | Ň | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | . | - | ! | # | $ | % | & | ( | ) | * | + | , | / | ; | = | ? | @ | [ | ] | ^ | _ | { | | | } | ~',
    '7: < | </',
    '8: />',
    '9: >',
    '10: </',
    '11: a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | š | č | ć | ď | ž | ľ | á | é | í | ó | ú | ý | ä | ô | ö | ü | ť | ŕ | ĺ | ň | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | Š | Č | Ć | Ď | Ž | Ľ | Á | É | Í | Ó | Ú | Ý | Ä | Ô | Ö | Ü | Ť | Ŕ | Ĺ | Ň | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | . | - | ! | # | $ | % | & | ( | ) | * | + | , | / | ; | = | ? | @ | [ | ] | ^ | _ | { | | | } | ~',
    '12: ε',
    '13: <',
    '14: ε',
    '15: a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | š | č | ć | ď | ž | ľ | á | é | í | ó | ú | ý | ä | ô | ö | ü | ť | ŕ | ĺ | ň | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | Š | Č | Ć | Ď | Ž | Ľ | Á | É | Í | Ó | Ú | Ý | Ä | Ô | Ö | Ü | Ť | Ŕ | Ĺ | Ň',
    '16:  ',
    '17: :',
    '18: a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | š | č | ć | ď | ž | ľ | á | é | í | ó | ú | ý | ä | ô | ö | ü | ť | ŕ | ĺ | ň | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | Š | Č | Ć | Ď | Ž | Ľ | Á | É | Í | Ó | Ú | Ý | Ä | Ô | Ö | Ü | Ť | Ŕ | Ĺ | Ň',
    '19: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9',
    '20: .',
    '21: -',
    '22:  ',
    '23: :',
    '24: ε',
    '25: a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | š | č | ć | ď | ž | ľ | á | é | í | ó | ú | ý | ä | ô | ö | ü | ť | ŕ | ĺ | ň | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | Š | Č | Ć | Ď | Ž | Ľ | Á | É | Í | Ó | Ú | Ý | Ä | Ô | Ö | Ü | Ť | Ŕ | Ĺ | Ň',
    '26: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9',
    '27: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9',
    '28: ε',
    '29: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9',
    '30: a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | š | č | ć | ď | ž | ľ | á | é | í | ó | ú | ý | ä | ô | ö | ü | ť | ŕ | ĺ | ň | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | Š | Č | Ć | Ď | Ž | Ľ | Á | É | Í | Ó | Ú | Ý | Ä | Ô | Ö | Ü | Ť | Ŕ | Ĺ | Ň | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | . | - | ! | # | $ | % | & | ( | ) | * | + | , | / | ; | = | ? | @ | [ | ] | ^ | _ | { | | | } | ~',
    '31: a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | š | č | ć | ď | ž | ľ | á | é | í | ó | ú | ý | ä | ô | ö | ü | ť | ŕ | ĺ | ň | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | Š | Č | Ć | Ď | Ž | Ľ | Á | É | Í | Ó | Ú | Ý | Ä | Ô | Ö | Ü | Ť | Ŕ | Ĺ | Ň | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | . | - | ! | # | $ | % | & | ( | ) | * | + | , | / | ; | = | ? | @ | [ | ] | ^ | _ | { | | | } | ~',
    '32: ε',
    '33: a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | š | č | ć | ď | ž | ľ | á | é | í | ó | ú | ý | ä | ô | ö | ü | ť | ŕ | ĺ | ň | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | Š | Č | Ć | Ď | Ž | Ľ | Á | É | Í | Ó | Ú | Ý | Ä | Ô | Ö | Ü | Ť | Ŕ | Ĺ | Ň',
    '34: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9',
    '35:  ',
    '36: .',
    '37: :',
    '38: -',
    '39: ?',
    '40: !'
}

FOLLOW = {
    '12: </',
    '14: </',
    '24: /> | >',
    '28: "?> | .',
    '32: </',
}

def get_rules_of_non_terminal(non_terminal):
    print("GETTING RULES OF NON_TERMINAL")
    print("PARSING_TABLE[non_terminal]")
    for key in PARSING_TABLE[non_terminal].keys():
        print("key: ", key)
    for value in PARSING_TABLE[non_terminal].values():
        print("value: ", value)



# Lexical analysis using DFA for LittleXML
def lexical_analysis(input_string):
    print('\n')
    print('Lexical analysis...')
    current_token = ''
    tokens = []
    i = 0
    # Split input_string into group of terminals: NAME, WORDS
    while i < len(input_string):
        # First, checking <?xml version="
        if input_string[i] == '<':
            # Check if it is an element
            if input_string[i+1] == '/':
                tokens.append('</')
                i += 2
            elif input_string[i+1] == '?':
                tokens.append('<?xml version="')
                i += 15
            else:
                tokens.append('<')
                i += 1
        elif input_string[i] == '>':
            tokens.append('>')
            i += 1
        elif input_string[i] == '/':
            tokens.append('/>')
            i += 2
        elif input_string[i] == '"':
            if input_string[i+1] == '?':
                tokens.append('"?>')
                i += 3
        elif input_string[i] in LETTER or input_string[i] in DIGIT or input_string[i] in ASCII or input_string[i] == ' ':
            current_token = ''
            while i < len(input_string) and (input_string[i] in LETTER or input_string[i] in DIGIT or input_string[i] in ASCII or input_string[i] == ' '):
                current_token += input_string[i]
                i += 1
            tokens.append(current_token)
        else:
            i += 1

    # Join elements together, is there is < followed by letter, followed by >, join them together
    i = 0
    while i < len(tokens):
        if tokens[i] == '<'  and tokens[i+2] == '>':
            tokens[i] = '<' + tokens[i+1] + '>'
            del tokens[i+1:i+3]
        i += 1
    
    # Join elements together if there is </ followed by letter, followed by >
    i = 0
    while i < len(tokens):
        if tokens[i] == '</' and tokens[i+2] == '>':
            tokens[i] = '</' + tokens[i+1] + '>'
            del tokens[i+1:i+3]
        i += 1
    return tokens


def vernumb_automata(token):
    # Using rules of VERNUMB
    print('VERNUMB AUTOMATA')
    print('Token:', token)
    state = 0
    for i in range(len(token)):
        if state == 0:
            if token[i] in DIGIT:
                state = 1
            else:
                return False
        elif state == 1:
            if token[i] == '.':
                state = 2
            elif token[i] in DIGIT:
                state = 1
            else:
                return False
        elif state == 2:
            if token[i] in DIGIT:
                state = 3
            else:
                return False
        elif state == 3:
            if token[i] in DIGIT:
                state = 3
            else:
                return False
    if state == 3:
        return True
    else:
        return False
    
def element_automata(token):
    # Element should start with <, then there goes letters and ends with >
    print('ELEMENT AUTOMATA')
    print('Token:', token)
    state = 0
    for i in range(len(token)):
        print(i)
        print('Token[i]:', token[i])
        print('State:', state)
        if state == 0:
            if token[i] == '<':
                state = 1
            else:
                return False
        elif state == 1:
            if token[i] in LETTER:
                state = 2
            else:
                print('Failed in state 1')
                return False
        elif state == 2:
            if token[i] == '>':
                return True
            elif token[i] in LETTER:
                state = 2
            else:
                print('Failed in state 2')
                return False
        
    


def parse(tokens):
        # Create parser, which uses RULES_SEPARATED (value of PARSING_TABLE terminal keys)
        # and PARSING_TABLE (key: non-terminal, value: dictionary of terminal keys and values)
        print('\n')
        print('Parsing...')
        stack = ['$', 'XMLDOCUMENT']
        stack_nesting_elements = []
        i = 0
        while stack:
            print(f'Stack: {stack}')
            print(f'Current token: {tokens[i]}')
            if stack[-1] == '$' and tokens[i] == '$':
                print('Parsing successful')
                return True
            elif stack[-1] in NON_TERMINALS:
                print(stack[-1],': Non-terminal' )
                if stack[-1] == 'VERNUMB':
                    print('VERNUMB')
                    if vernumb_automata(tokens[i]):
                        print('Automata success')
                        stack.pop()
                        i += 1
                        continue
                    else:
                        print('Automata failed')
                        return False

                if stack[-1] == 'ELEMENT':
                    print('ELEMENT')
                    if element_automata(tokens[i]):
                        print('Automata success')
                        stack.pop()
                        stack_nesting_elements.append(tokens[i])
                        i += 1
                        continue
                    else:
                        print('Automata failed')
                        return False

                if tokens[i] in PARSING_TABLE[stack[-1]]:
                    print('Token in parsing table')
                    rule = PARSING_TABLE[stack[-1]][tokens[i]]
                    ruleIndex = rule - 1
                    print(f'Rule: {rule}')
                    stack.pop()
                    print(f'STACK: {stack}')
                    if rule == 12:
                        continue
                    print('STACK[-1]', stack[-1])
                    for symbol in RULES_SEPARATED[ruleIndex].split(' -> ')[1].split(' ')[::-1]:
                        print('Symbol:', symbol)
                        if symbol != '<?xml' and symbol != 'version="':
                            stack.append(symbol)
                        else:
                            if(stack[-1] != '<?xml version="'):
                                stack.append('<?xml version="')
                        print(f'STACK: {stack}')
                
                else:
                    print('Token not in parsing table')
                    print('Token: ', tokens[i], 'PARSING_TABLE[stack[-1]]: ', PARSING_TABLE[stack[-1]])
                    return False
            elif stack[-1] == tokens[i]:
                print('Found Terminal!')
                print(f'Popped: {stack[-1]}')
                stack.pop()
                i += 1
            else:
                print('Error')
                return False
        return False




def main():
    # Reading the input file as utf-8, splitting the input examples by the empty line
    get_rules_of_non_terminal("XMLDOCUMENT")
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
        print(lexical_analysis(example_stripped))
        print(parse(lexical_analysis(example_stripped)))


if __name__ == '__main__':
    main()


