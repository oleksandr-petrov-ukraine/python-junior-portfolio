def get_shift():
    while True:
        try:
            shift = int(input('Enter shift (must be an integer): '))
            shift %= 26  # normalize shift
            return shift
        except ValueError:
            print('Shift must be an integer')

def caesar_cipher(text, shift, mode):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for char in text:
        if char.lower() not in alphabet:
            result += char
            continue

        char_index = alphabet.find(char.lower())
        new_char_index = (char_index + shift) % len(alphabet) if mode == 0 else (char_index - shift) % len(alphabet)
        result += alphabet[new_char_index].upper() if char.isupper() else alphabet[new_char_index]

    return result

text = input('Enter text: ')

while True:
    try:
        mode = int(input('Enter mode (0 - encrypt, 1 - decrypt): '))
        if mode not in (0, 1):
            print('Mode must be 0 or 1')
            continue
        break
    except ValueError:
        print('Mode must be an integer')

shift = get_shift()
print(caesar_cipher(text, shift, mode))
