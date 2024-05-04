LETTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'š', 'č', 'ć', 'ď', 'ž', 'ľ', 'á', 'é', 'í', 'ó', 'ú', 'ý', 'ä', 'ô', 'ö', 'ü', 'ť', 'ŕ', 'ĺ', 'ň',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Š', 'Č', 'Ć', 'Ď', 'Ž', 'Ľ', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ý', 'Ä', 'Ô', 'Ö', 'Ü', 'Ť', 'Ŕ', 'Ĺ', 'Ň']

DIGIT = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

ASCII = ['.','-','!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '/', ';', '=', '?', '@', '[', ']', '^', '_', '{', '|', '}', '~']

RULES_SECOND_REVISION = {
    'XMLDOCUMENT': (
        ['XMLDECL'], #1
        ['ELEMENT']  #2
    ),
    'XMLDECL': ['<?xml version ="', 'VERNUMB','"?>'], #3
    'VERNUMB': ['NUMBER', '.', 'NUMBER'], #4
    'ELEMENT': ['<', 'NAME', 'ELEMENT``'], #5
    'ELEMENT`': (
        ['WORDS', 'ENDTAG'], # 6  
        ['ELEMENTS', 'ENDTAG'] #7
    ),
    'ELEMENT``': (
        ['/>'],  #8
        ['>', 'ELEMENT`'] #9
    ),
    'ENDTAG': ['</', 'NAME', '>'], #10
    'WORDS': (
        ['WORD', 'WORDS'],  #11
        ['ε'] #12
    ),
    'ELEMENTS': (
        ['ELEMENT'],  #13
        ['ε'] #14
    ),
    'NAME': (
        ['LETTER', 'NAMECHAR'], #15
        [' ', 'NAMECHAR'], #16
        [':', 'NAMECHAR'] #17
    ),
    'NAMECHAR': (
        ['LETTER', 'NAMECHAR'], #18
        ['DIGIT', 'NAMECHAR'], #19
        ['.', 'NAMECHAR'], #20
        ['-', 'NAMECHAR'], #21
        [' ', 'NAMECHAR'], #22
        [':', 'NAMECHAR'], #23
        ['ε'] #24
    ),
    'LETTER': LETTER, #25
    'NUMBER': ['DIGIT', 'NUMBER`'],  #26
    'DIGIT': DIGIT,  #27
    'WORD': ['CHAR', 'WORD`'], #28
    'WORD`': (
        ['CHAR', 'WORD`'], #29
        ['ε'] #30
    ),
    'CHAR': (
        LETTER, #31
        DIGIT, #32
        ASCII #33
    )
}

FIRST = {
    'XMLDOCUMENT': ['<?xml version ="', '<'],
    'XMLDECL': ['<?xml version ="'],
    'VERNUMB': DIGIT,
    'ELEMENT': ['<'],
    'ELEMENT`': LETTER + DIGIT + ASCII + ['ε'],
    'ELEMENT``': ['/>', '>'],
    'ENDTAG': ['</'],
    'WORDS': LETTER + DIGIT + ASCII + ['ε'],
    'ELEMENTS': ['<', 'ε'],
    'NAME': LETTER + [' ', ':'],
    'NAMECHAR': LETTER + DIGIT + ASCII + ['ε'],
    'LETTER': LETTER,
    'NUMBER': DIGIT,
    'NUMBER`': DIGIT + ['ε'],
    'DIGIT': DIGIT,
    'WORD': LETTER + DIGIT + ASCII,
    'WORD`': LETTER + DIGIT + ASCII + ['ε'],
    'CHAR': LETTER + DIGIT + ASCII
}

FOLLOW = {
    'XMLDOCUMENT': ['EOF'],
    'XMLDECL': ['<'],
    'VERNUMB': ['"?>'],
    'ELEMENT': ['EOF', '</'],
    'ELEMENT`': ['EOF', '</'],
    'ELEMENT``': ['EOF', '</'],
    'ENDTAG': ['EOF', '</'],
    'WORDS': ['</'],
    'ELEMENTS': ['</'],
    'NAME': ['/>', '>'],
    'NAMECHAR': ['/>', '>'],
    'LETTER': LETTER + DIGIT + ASCII,
    'NUMBER': ['.', '"?>'],
    'NUMBER`': ['.', '"?>'],
    'DIGIT': LETTER + DIGIT + ASCII + ['/>'] + ['>'],
    'WORD': LETTER + DIGIT + ['/>'],
    'WORD`': LETTER + DIGIT + ['</'],
    'CHAR': LETTER + DIGIT + ['</'],
}

PARSING_TABLE = {
    'XMLDOCUMENT': {
        '<?xml version="': 1
    },
    'XMLDECL': {
        '<?xml version="': 3,
        '<': 2,
    },
    'VERNUMB':{
        ', '.join(DIGIT): 4
    },
    'ELEMENT': {
        '<': 5
    },
    'ELEMENT`': {
        '<': 7,
        ', '.join(['EOF', '</']): 6
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
        '<': 13,
        '</': 14
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
        ':': 21,
        '-': 22,
        ', '.join(['/>', '>']): 23, # ! Conflict
    },
    'LETTER': {
        ', '.join(LETTER): 24
    },
    'NUMBER': {
        ', '.join(DIGIT): 25,
        ', '.join(['.', '"?>']): 26 # ! Conflict
    },
    'NUMBER`': {
        ', '.join(DIGIT): 27
    },
    'DIGIT': {
        ', '.join(DIGIT): 28
    },
    'WORD': {
        ', '.join(LETTER): 29,
        ', '.join(DIGIT): 29,
        ', '.join(ASCII): 29
    },
    'WORD`': {
        ', '.join(LETTER): 30,
        ', '.join(DIGIT): 30,
        ', '.join(ASCII): 30,
        '</': 31
    },
    'CHAR': {
        '</': 32,
        ', '.join(DIGIT): 33,
        ', '.join(ASCII): 34
    }
}

# Lexical analysis using DFA for LittleXML
def lexical_analysis(input_string):
    START_STATE = 'XMLDOCUMENT'
    current_state = START_STATE
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
        elif input_string[i] == '?':
            tokens.append('<?')
            i += 2
        elif input_string[i] == '"':
            tokens.append('"')
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


if __name__ == '__main__':
    main()


