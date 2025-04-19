import re

MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }



###3rd attempt without for:
def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):
    """Convert an input text file to an output Morse code file.

    Notes
    -----
    This function assumes the existence of a MORSE_CODE dictionary, containing a
    mapping between English letters and their corresponding Morse code.

    Parameters
    ----------
    input_file : str
        Path to file containing the text file to convert.
    output_file : str
        Name of output file containing the translated Morse code. Please don't change
        it since it's also hard-coded in the tests file.
    """
    try:
        with open(input_file, "r") as input:
            content = input.read().upper()
    except FileNotFoundError:
        print("such file doesn't exist")

    #translating using the str.translate built-in method
    trans_table = str.maketrans(MORSE_CODE)
    translated = content.translate(trans_table)
    temp_text = re.sub(r'\n\n+', '<break>', translated) #replace double newlines with a placeholder for them to differ from the spaces between words in next line 
    temp_text = re.sub(r'\s+', '\n', temp_text) #turn spaces to new lines in order to have each word in it's own line
    output_string = temp_text.replace('<break>', '\n\n').rstrip('\n') #put back double newlines and remove final newline

    try:
        with open(output_file, "w") as output:
            output.write(output_string)
    except Exception: #every possible error
            print("couldn't write to file")
    finally:
        print("succesfull execution!")

    return output_string

if __name__ == '__main__':
    output_string = english_to_morse(
        input_file = "lorem.txt",
        output_file = "lorem_morse.txt")

