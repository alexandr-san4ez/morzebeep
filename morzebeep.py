from winsound import Beep
from sys import argv

__all__ = ['play']

CODES = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    '': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '......',
    ' ': '.......',
    ',': '.-.-.-',
    ':': '---...',
    ';': '-.-.-.',
    '(': '-.--.-',
    ')': '-.--.-',
    '\'': '.----.',
    '\"': '.-..-.',
    '-': '-....-',
    '\\': '-..-.',
    '?': '..--..',
    '!': '--..--',
    '@': '.--.-.',
    '\n': '..-.-'
}

def play(text, duration=100, frequency=1000):
    """
    Translate text to morze and play

    Args:
        text (str): source text
        duration (int): duration of one signal. Check `winsound.Beep` function
        frequency (int): parameter specifies frequency, in hertz, of the sound. Check `winsound.Beep` function

    """

    text = text.upper()
    for char in text:
        code_char = CODES.get(char)

        if not code_char:
            continue

        for i in code_char:
            if i == '.':
                Beep(frequency, duration)
            else:
                Beep(frequency, duration * 3)

def main():
    play(' '.join(argv[1:]))
    # play('Hello world.')


if __name__ == "__main__":
    main()
