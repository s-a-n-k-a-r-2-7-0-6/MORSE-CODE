morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

def text_to_morse(text):
    morse = ''
    for i in text:
        if i != ' ':
            morse += morse_code[i.upper()] + ' '
        else:
            morse += ' '
    return morse

def morse_to_text(morse):
    text = ''
    morse += ' '
    d = ''
    for char in morse:
        if (char != ' '):
            i = 0
            d += char
        else:
            i += 1
            if i == 2:
                text += ' '
            else:
                text += list(morse_code.keys())[list(morse_code.values()).index(d)]
                d = ''
    return text
print(text_to_morse('ths'))
print(morse_to_text('-.. . . .--. '))