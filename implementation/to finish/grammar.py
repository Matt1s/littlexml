LETTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'š', 'č', 'ć', 'ď', 'ž', 'ľ', 'á', 'é', 'í', 'ó', 'ú', 'ý', 'ä', 'ô', 'ö', 'ü', 'ť', 'ŕ', 'ĺ', 'ň',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Š', 'Č', 'Ć', 'Ď', 'Ž', 'Ľ', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ý', 'Ä', 'Ô', 'Ö', 'Ü', 'Ť', 'Ŕ', 'Ĺ', 'Ň']

DIGIT = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

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
    '16: NAME ->  NAMECHAR',
    '17: NAME -> : NAMECHAR',
    '18: NAMECHAR -> LETTER NAMECHAR',
    '19: NAMECHAR -> DIGIT NAMECHAR',
    '20: NAMECHAR -> . NAMECHAR',
    '21: NAMECHAR -> - NAMECHAR',
    '22: NAMECHAR ->  NAMECHAR',
    '23: NAMECHAR -> : NAMECHAR',
    '24: NAMECHAR -> ε',
    '25: LETTER -> a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z',
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
        'a': 6,
        'b': 6,
        'c': 6,
        'd': 6,
        'e': 6,
        'f': 6,
        'g': 6,
        'h': 6,
        'i': 6,
        'j': 6,
        'k': 6,
        'l': 6,
        'm': 6,
        'n': 6,
        'o': 6,
        'p': 6,
        'q': 6,
        'r': 6,
        's': 6,
        't': 6,
        'u': 6,
        'v': 6,
        'w': 6,
        'x': 6,
        'y': 6,
        'z': 6,
        'A': 6,
        'B': 6,
        'C': 6,
        'D': 6,
        'E': 6,
        'F': 6,
        'G': 6,
        'H': 6,
        'I': 6,
        'J': 6,
        'K': 6,
        'L': 6,
        'M': 6,
        'N': 6,
        'O': 6,
        'P': 6,
        'Q': 6,
        'R': 6,
        'S': 6,
        'T': 6,
        'U': 6,
        'V': 6,
        'W': 6,
        'X': 6,
        'Y': 6,
        'Z': 6,
        '0': 6,
        '1': 6,
        '2': 6,
        '3': 6,   
        '4': 6,
        '5': 6,
        '6': 6,
        '7': 6,
        '8': 6,
        '9': 6,
        '.': 6,
        '-': 6,
        '!': 6,
        '#': 6,
        '?': 6,
    },
    'ELEMENT``': {
        '>': 9,
        '/>': 8
    },
    'ENDTAG': {
        '</': 10
    },
    'WORDS': {
        'a': 11,
        'b': 11,
        'c': 11,
        'd': 11,
        'e': 11,
        'f': 11,
        'g': 11,
        'h': 11,
        'i': 11,
        'j': 11,
        'k': 11,
        'l': 11,
        'm': 11,
        'n': 11,
        'o': 11,
        'p': 11,
        'q': 11,
        'r': 11,
        's': 11,
        't': 11,
        'u': 11,
        'v': 11,
        'w': 11,
        'x': 11,
        'y': 11,
        'z': 11,
        'A': 11,
        'B': 11,
        'C': 11,
        'D': 11,
        'E': 11,
        'F': 11,
        'G': 11,
        'H': 11,
        'I': 11,
        'J': 11,
        'K': 11,
        'L': 11,
        'M': 11,
        'N': 11,
        'O': 11,
        'P': 11,
        'Q': 11,
        'R': 11,
        'S': 11,
        'T': 11,
        'U': 11,
        'V': 11,
        'W': 11,
        'X': 11,
        'Y': 11,
        'Z': 11,
        '0': 11,
        '1': 11,
        '2': 11,
        '3': 11,   
        '4': 11,
        '5': 11,
        '6': 11,
        '7': 11,
        '8': 11,
        '9': 11,
        '.': 11,
        '-': 11,
        '!': 11,
        '#': 11,
        '?': 11,
        '</': 12
    },
    'ELEMENTS': {
        '</': 14,
        '<': 13,
    },
    'NAME': {
        'a': 15,
        'b': 15,
        'c': 15,
        'd': 15,
        'e': 15,
        'f': 15,
        'g': 15,
        'h': 15,
        'i': 15,
        'j': 15,
        'k': 15,
        'l': 15,
        'm': 15,
        'n': 15,
        'o': 15,
        'p': 15,
        'q': 15,
        'r': 15,
        's': 15,
        't': 15,
        'u': 15,
        'v': 15,
        'w': 15,
        'x': 15,
        'y': 15,
        'z': 15,
        'A': 15,
        'B': 15,
        'C': 15,
        'D': 15,
        'E': 15,
        'F': 15,
        'G': 15,
        'H': 15,
        'I': 15,
        'J': 15,
        'K': 15,
        'L': 15,
        'M': 15,
        'N': 15,
        'O': 15,
        'P': 15,
        'Q': 15,
        'R': 15,
        'S': 15,
        'T': 15,
        'U': 15,
        'V': 15,
        'W': 15,
        'X': 15,
        'Y': 15,
        'Z': 15,
        ' ': 16,
        ':': 17
    },
    'NAMECHAR': {
        'a': 18,
        'b': 18,
        'c': 18,
        'd': 18,
        'e': 18,
        'f': 18,
        'g': 18,
        'h': 18,
        'i': 18,
        'j': 18,
        'k': 18,
        'l': 18,
        'm': 18,
        'n': 18,
        'o': 18,
        'p': 18,
        'q': 18,
        'r': 18,
        's': 18,
        't': 18,
        'u': 18,
        'v': 18,
        'w': 18,
        'x': 18,
        'y': 18,
        'z': 18,
        'A': 18,
        'B': 18,
        'C': 18,
        'D': 18,
        'E': 18,
        'F': 18,
        'G': 18,
        'H': 18,
        'I': 18,
        'J': 18,
        'K': 18,
        'L': 18,
        'M': 18,
        'N': 18,
        'O': 18,
        'P': 18,
        'Q': 18,
        'R': 18,
        'S': 18,
        'T': 18,
        'U': 18,
        'V': 18,
        'W': 18,
        'X': 18,
        'Y': 18,
        'Z': 18,
        '0': 19,
        '1': 19,
        '2': 19,
        '3': 19,
        '4': 19,
        '5': 19,
        '6': 19,
        '7': 19,
        '8': 19,
        '9': 19,
        '.': 20,
        '-': 21,
        ' ': 22,
        ':': 23,
        '/>': 24,
        '>': 24,
    },
    'LETTER': {
        'a': 25,
        'b': 25,
        'c': 25,
        'd': 25,
        'e': 25,
        'f': 25,
        'g': 25,
        'h': 25,
        'i': 25,
        'j': 25,
        'k': 25,
        'l': 25,
        'm': 25,
        'n': 25,
        'o': 25,
        'p': 25,
        'q': 25,
        'r': 25,
        's': 25,
        't': 25,
        'u': 25,
        'v': 25,
        'w': 25,
        'x': 25,
        'y': 25,
        'z': 25,
        'A': 25,
        'B': 25,
        'C': 25,
        'D': 25,
        'E': 25,
        'F': 25,
        'G': 25,
        'H': 25,
        'I': 25,
        'J': 25,
        'K': 25,
        'L': 25,
        'M': 25,
        'N': 25,
        'O': 25,
        'P': 25,
        'Q': 25,
        'R': 25,
        'S': 25,
        'T': 25,
        'U': 25,
        'V': 25,
        'W': 25,
        'X': 25,
        'Y': 25,
        'Z': 25
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
        '0': 27,
        '1': 27,
        '2': 27,
        '3': 27,
        '4': 27,
        '5': 27,
        '6': 27,
        '7': 27,
        '8': 27,
        '9': 27,
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
        'a': 30,
        'b': 30,
        'c': 30,
        'd': 30,
        'e': 30,
        'f': 30,
        'g': 30,
        'h': 30,
        'i': 30,
        'j': 30,
        'k': 30,
        'l': 30,
        'm': 30,
        'n': 30,
        'o': 30,
        'p': 30,
        'q': 30,
        'r': 30,
        's': 30,
        't': 30,
        'u': 30,
        'v': 30,
        'w': 30,
        'x': 30,
        'y': 30,
        'z': 30,
        'A': 30,
        'B': 30,
        'C': 30,
        'D': 30,
        'E': 30,
        'F': 30,
        'G': 30,
        'H': 30,
        'I': 30,
        'J': 30,
        'K': 30,
        'L': 30,
        'M': 30,
        'N': 30,
        'O': 30,
        'P': 30,
        'Q': 30,
        'R': 30,
        'S': 30,
        'T': 30,
        'U': 30,
        'V': 30,
        'W': 30,
        'X': 30,
        'Y': 30,
        'Z': 30,
        '0': 30,
        '1': 30,
        '2': 30,
        '3': 30,   
        '4': 30,
        '5': 30,
        '6': 30,
        '7': 30,
        '8': 30,
        '9': 30,
        '.': 30,
        '-': 30,
        '!': 30,
        '#': 30,
        '?': 30,
    },
    'WORD`': {
        'a': 31,
        'b': 31,
        'c': 31,
        'd': 31,
        'e': 31,
        'f': 31,
        'g': 31,
        'h': 31,
        'i': 31,
        'j': 31,
        'k': 31,
        'l': 31,
        'm': 31,
        'n': 31,
        'o': 31,
        'p': 31,
        'q': 31,
        'r': 31,
        's': 31,
        't': 31,
        'u': 31,
        'v': 31,
        'w': 31,
        'x': 31,
        'y': 31,
        'z': 31,
        'A': 31,
        'B': 31,
        'C': 31,
        'D': 31,
        'E': 31,
        'F': 31,
        'G': 31,
        'H': 31,
        'I': 31,
        'J': 31,
        'K': 31,
        'L': 31,
        'M': 31,
        'N': 31,
        'O': 31,
        'P': 31,
        'Q': 31,
        'R': 31,
        'S': 31,
        'T': 31,
        'U': 31,
        'V': 31,
        'W': 31,
        'X': 31,
        'Y': 31,
        'Z': 31,
        '0': 31,
        '1': 31,
        '2': 31,
        '3': 31,   
        '4': 31,
        '5': 31,
        '6': 31,
        '7': 31,
        '8': 31,
        '9': 31,
        '.': 31,
        '-': 31,
        '!': 31,
        '#': 31,
        '?': 31,
        '</': 32
    },
    'CHAR': {
        
        'a': 33,
        'b': 33,
        'c': 33,
        'd': 33,
        'e': 33,
        'f': 33,
        'g': 33,
        'h': 33,
        'i': 33,
        'j': 33,
        'k': 33,
        'l': 33,
        'm': 33,
        'n': 33,
        'o': 33,
        'p': 33,
        'q': 33,
        'r': 33,
        's': 33,
        't': 33,
        'u': 33,
        'v': 33,
        'w': 33,
        'x': 33,
        'y': 33,
        'z': 33,
        'A': 33,
        'B': 33,
        'C': 33,
        'D': 33,
        'E': 33,
        'F': 33,
        'G': 33,
        'H': 33,
        'I': 33,
        'J': 33,
        'K': 33,
        'L': 33,
        'M': 33,
        'N': 33,
        'O': 33,
        'P': 33,
        'Q': 33,
        'R': 33,
        'S': 33,
        'T': 33,
        'U': 33,
        'V': 33,
        'W': 33,
        'X': 33,
        'Y': 33,
        'Z': 33,
        '0': 34,
        '1': 34,
        '2': 34,
        '3': 34,
        '4': 34,
        '5': 34,
        '6': 34,
        '7': 34,
        '8': 34,
        '9': 34,
        ' ': 35,
        '.': 36,
        ':': 37,
        '-': 38,
        '?': 39,
        '!': 40,
    }
}