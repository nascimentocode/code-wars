import string

def alphabet_position(text):
    alphabet = list(string.ascii_lowercase)
    alphabetPosition = []
    for letterText in text.lower():
        if letterText.isalpha():
            alphabetPosition.append(str(alphabet.index(letterText)+1))

    return " ".join(alphabetPosition)