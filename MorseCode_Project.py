


morse_code_dict = {

    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '       '

}




def morse_code_converter():
    string = input('Enter Text:' )
    upper_string = string.upper()
    morse_code_full = ''
    for i in upper_string:
        morse_code_element = morse_code_dict[i]
        morse_code_full = morse_code_full + morse_code_element + '   '
    print(f'{string} in morse code = {morse_code_full}')
    return morse_code_full





morse_code_converter()






