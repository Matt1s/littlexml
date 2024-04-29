LETTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

DIGIT = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

ASCII = ['!', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '/', ';', '=', '?', '@', '[', ']', '^', '_', '{', '|', '}', '~']

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