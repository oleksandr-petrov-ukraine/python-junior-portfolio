def caesar_cipher(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift = 4
    result = ''

    for char in text:
        if char.lower() not in alphabet:
            result += char
            continue

        char_index = alphabet.find(char.lower())
        new_char_index = (char_index + shift) % len(alphabet)
        result += alphabet[new_char_index]

    return result


