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
    '22: NAMECHAR -> : NAMECHAR',
    '23: NAMECHAR -> NAMECHAR',
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
        ', '.join(DIGIT): 4
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
        ', '.join(DIGIT): 26,
    },
    'NUMBER`': {
        ', '.join(DIGIT): 27,
        '"?>': 28
    },
    'DIGIT': {
        ', '.join(DIGIT): 29
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

# Lexical analysis using DFA for LittleXML
def lexical_analysis(input_string):
    print('\n')
    print('Lexical analysis...')
    START_STATE = 'XMLDOCUMENT'
    current_state = START_STATE
    current_token = ''
    tokens = []
    i = 0
    # Split input_string into group of terminals: NAME, WORDS
    while i < len(input_string):
        # First, checking <?xml version="
        if input_string[i:i+15] == '<?xml version="':
            tokens.append('<?xml version="')
            i += 15
        elif input_string[i] == '<':
            # Check if it is an element
            if input_string[i+1] == '/':
                tokens.append('</')
                i += 2
            elif input_string[i+1] == '?':
                tokens.append('<?')
                i += 2
            else:
                tokens.append('<')
                i += 1
        elif input_string[i:i+2] == '/>':
            tokens.append('/>')
            i += 2
        elif input_string[i:i+2] == '?>':
            tokens.append('?>')
            i += 2
        elif input_string[i] == '>':
            tokens.append('>')
            i += 1
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

def parse(tokens):
        print('\n')
        print('Parsing...')
        stack = ['XMLDOCUMENT']  # Start with the root element
        i = 0
        state = stack[-1]
        print('PARSING TABLE STATE TOP OF STACK')
        print(PARSING_TABLE[state])
        while i < len(tokens):
            print(f'Current token: {tokens[i]}')
            # Put token on the stack
            stack.append(tokens[i])
            print(f'Stack: {stack}')
            # Get the top of the stack
            state = stack[-1]
            print(f'State: {state}')
            # Get the top of the stack
            top_of_stack = stack[-1]
            print(f'Top of stack: {top_of_stack}')
            # Get the top of the stack
            print(f'Parsing table state: {PARSING_TABLE[state]}')
            # Check if the top of the stack is in the parsing table
            if top_of_stack in PARSING_TABLE[state]:
                # Get the rule number
                rule_number = PARSING_TABLE[state][top_of_stack]
                print(f'Rule number: {rule_number}')
                # Get the rule
                rule = RULES_SECOND_REVISION[rule_number]
                print(f'Rule: {rule}')
                # Pop the stack
                stack.pop()
                print(f'Stack: {stack}')
                # Pop the stack
                stack.pop()
                print(f'Stack: {stack}')
                # Push the rule on the stack
                stack += rule
                print(f'Stack: {stack}')
            else:
                print('Error')
                break




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
        print(lexical_analysis(example_stripped))
        print(parse(lexical_analysis(example_stripped)))


if __name__ == '__main__':
    main()


