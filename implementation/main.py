
LETTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'š', 'č', 'ć', 'ď', 'ž', 'ľ', 'á', 'é', 'í', 'ó', 'ú', 'ý', 'ä', 'ô', 'ö', 'ü', 'ť', 'ŕ', 'ĺ', 'ň',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Š', 'Č', 'Ć', 'Ď', 'Ž', 'Ľ', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ý', 'Ä', 'Ô', 'Ö', 'Ü', 'Ť', 'Ŕ', 'Ĺ', 'Ň']

DIGIT = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

ASCII = ['.','-','!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '/', ';', '=', '?', '@', '[', ']', '^', '_', '{', '|', '}', '~']

NONTERMINALS = ['XMLDOCUMENT', 'XMLDECL', 'VERNUMB','ELEMENT', 'ELEMENT`','ELEMENT``', 'ENDTAG',
                'WORDS', 'ELEMENTS', 'NAME', 'NAMECHAR', 'LETTER', 'NUMBER', 'DIGIT', 'WORD', 'WORD`','CHAR']

TERMINALS = ['<?xml version ="', '"?>', '.', '<', '>', '/>', '</', ' ', ':', '-'] + LETTER + DIGIT + ASCII

q0 = 'XMLDOCUMENT'

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

def get_next_state(current_state, terminal):
    print('Getting next from from parsing table...')
    print(f'Current state: {current_state}, Terminal: {terminal}')
    for key in PARSING_TABLE.get(current_state):
        if terminal in key:
            return PARSING_TABLE.get(current_state).get(key)
    return None

def tokenize(input_string):
    # Following the PARSING_TABLE, we can tokenize the example
    tokens = []
    START_STATE = 'XMLDOCUMENT'
    CURRENT_STATE = START_STATE
    RULE_USED = None
    # Split the example by the rule used in current state
    while input_string:
        for terminal in TERMINALS:
            print(terminal)
            for key in PARSING_TABLE.get(CURRENT_STATE):
                if terminal in key:
                    print(f'Key: {key}, Value: {PARSING_TABLE.get(CURRENT_STATE).get(key)}')
                    tokens.append(terminal)
                    input_string = input_string[len(key):]
                    RULE_USED = PARSING_TABLE.get(CURRENT_STATE).get(key)
                    print(RULE_USED)
                    # Going to next rule from RULES_SECOND_REVISION, based on next terminal in the input_string
                    NEXT_TERMINAL = input_string[0]
                    CURRENT_STATE = get_next_state(CURRENT_STATE, NEXT_TERMINAL)
                    print(f'Current state: {CURRENT_STATE}')
    return tokens


NDA = {
    'XMLDOCUMENT':{
        '<?xml version="': 'XMLDECL',
        '<': 'ELEMENT'
    },
    'XMLDECL':{
        'DIGIT': 'VERNUMB',
    },
    'VERNUMB':{
        '.': 'VERNUMB`',
    },
    'VERNUMB`':{
        'DIGIT': 'VERNUMB``',
    },
    'VERNUMB``':{
        '"?>': 'ELEMENT'
    },
    'ELEMENT':{
        '<': 'NAME'
    },
    'NAME':{
        'LETTER': 'NAMECHAR'
    },
    'NAMECHAR':{
        'LETTER': 'NAMECHAR',
        'DIGIT': 'NAMECHAR',
        'ASCII': 'NAMECHAR',
        '>': 'ELEMENT`',
        '/>': 'ELEMENT``',
    },
    'ELEMENT``':{
        'EOF': 'FINAL',
    },
    'ELEMENT`':{
        'LETTER': 'WORDS',
        'DIGIT': 'WORDS',
        'ASCII': 'WORDS',
        '</': 'NAME',
        '<': 'NAME',
    },
    'WORDS':{
        'LETTER': 'CHAR',
        'DIGIT': 'CHAR',
        'ASCII': 'CHAR',
        '</': 'NAME',
    },
    'CHAR':{
        'LETTER': 'CHAR',
        'DIGIT': 'CHAR',
        'ASCII': 'CHAR',
        '</': 'NAME',
    }
}


def check_string(example):

    # Tokenize the example
    # tokens = tokenize(example)
    # print(tokens)
    # Parse the tokens
    #return parse(tokens)
    # Use the NDA to check if the example is valid
    STARTING_STATE = 'XMLDOCUMENT'
    current_state = STARTING_STATE
    # loop through NDA current_state and find the longest match
    print('Looping through NDA...')
    i = 0
    while True:
        key = example[i]
        current_non_terminal = None
        if(key == ' '):
            print('Skipping space')
            i += 1
            key = example[i]
        for key in NDA.get(current_state):
            # Possible keys in the current state:
            print("Possible non-terminals:", NDA.get(current_state).keys())
            print(f'Current key: {key}')
            if key == 'DIGIT':
                if example[i] in DIGIT:
                    key = example[i]
                    print('Found digit:', key)
                    current_non_terminal = 'DIGIT'
            if key == 'LETTER':
                if example[i] in LETTER:
                    key = example[i]
                    print('Found letter:', key)
                    current_non_terminal = 'LETTER'
            if key == 'ASCII':
                if example[i] in ASCII:
                    key = example[i]
                    print('Found ASCII:', key)
                    current_non_terminal = 'ASCII'

            try:
                print(example[i], example[i+1], example[i+2])
            except:
                print('End of example')
            if(example[i] == ' '):
                # Skip until next non-space character
                i += 1
                print('Skipping space')
            if key in example[i:]:
                print('CHANGING STATE!')
                # Update the current state to the value of the key
                if current_non_terminal:
                    current_state = NDA.get(current_state).get(current_non_terminal)
                else:
                    current_state = NDA.get(current_state).get(key)
                i += len(key)
                print('Current i', i)
                print(f'Found key: {key}')
                try:
                    print('Next symbol:', example[i])
                except:
                    print('End of example')
                    
                print(f'Next state: {current_state}')
                # If the current state is FINAL, the example is valid
                current_non_terminal = None
                if current_state == 'FINAL':
                    return True
                break
                
    return True


def main():
    # Reading the input file as utf-8, splitting the input examples by the empty line
    with open('input.txt', 'r', encoding='utf-8') as file:
        examples = file.read().split('\n\n')
        #for example in examples:
        example = examples[2]
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
        if check_string(example_stripped):
            print('The example is valid')
        else:
            print('The example is invalid')
        print('------------------------------------')


if __name__ == '__main__':
    main()

