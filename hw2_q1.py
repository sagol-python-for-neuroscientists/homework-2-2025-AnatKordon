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


# def english_to_morse(
#     input_file: str = "lorem.txt",
#     output_file: str = "lorem_morse.txt"
# ):
#     """Convert an input text file to an output Morse code file.

#     Notes
#     -----
#     This function assumes the existence of a MORSE_CODE dictionary, containing a
#     mapping between English letters and their corresponding Morse code.

#     Parameters
#     ----------
#     input_file : str
#         Path to file containing the text file to convert.
#     output_file : str
#         Name of output file containing the translated Morse code. Please don't change
#         it since it's also hard-coded in the tests file.
#     """
 
#     with open(input_file, "r") as input:
#         content = input.read()
#     print(content)
#     upper_text = content.upper().split()
#     #print(upper_text)
#     upper_text2 = content.upper().split(' ')
#     print(upper_text2)

#     output_string = ""
#     for word in upper_text:
#         new_word = ""
#         for letter in word:
#             if letter in MORSE_CODE:
#                 new_word += MORSE_CODE[letter]    
              
#         output_string += new_word + '\n' 
#         #print(output_string[0:82])

#     with open(output_file, "w") as output: 
#         output.write(output_string)
#     return output_string

def english_to_morse(input_file="lorem.txt", output_file="lorem_morse.txt"):
    with open(input_file, "r") as input:
        content = input.read().upper()

    # Split text by paragraphs
    paragraphs = content.split("\n\n")
    output_lines = []

    for paragraph in paragraphs:
        words = paragraph.split()
        for word in words:
            morse_word = ""
            for char in word:
                if char in MORSE_CODE:
                    morse_word += MORSE_CODE[char]
            output_lines.append(morse_word)
        output_lines.append("")  # empty line between paragraphs

    output_string = '\n'.join(output_lines)

    with open(output_file, "w") as output:
        output.write(output_string)

    return output_string

output_string = english_to_morse(
    input_file = "lorem.txt",
    output_file = "lorem_morse.txt")

###TESTS

# # Reverse the dict to decode
# MORSE_TO_ENG = {v: k for k, v in MORSE_CODE.items()}

# def decode_morse_word(morse_word):
#     decoded = ""
#     i = 0
#     while i < len(morse_word):
#         for j in range(len(morse_word), i, -1):
#             chunk = morse_word[i:j]
#             if chunk in MORSE_TO_ENG:
#                 decoded += MORSE_TO_ENG[chunk]
#                 i = j
#                 break
#         else:
#             # No match found – something went wrong
#             decoded += '?'
#             i += 1
#     return decoded

# word1 = decode_morse_word('.-....-.....-.---')
# word2 = decode_morse_word('--.-.-.-..-..-...')
# print(word1, word2)