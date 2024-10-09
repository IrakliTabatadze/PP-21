# alphabet = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
# ]
# hashmap = {}
# secondHash = {}
#
#
# def chiper(orient, k, n):
#     res = ''
#     for i in range(len(n)):
#         if n[i].lower() in alphabet:
#             if orient == 1:
#                 code = alphabet.index(n[i].lower()) - k # secondHash[n[i].lower()] - k
#                 if code < 0:
#                     code = 26 - abs(code)
#                 if n[i].isupper():
#                     res += alphabet[code].upper()
#                 else:
#                     res += alphabet[code]
#     return res
#
#
# print(chiper(1, 13, "AttackAtDawn") == 'NggnpxNgQnja')


def caesar_cipher(text, shift, direction='right'):
    result = ""
    if direction == 'left':
        shift = -shift % 26
    elif direction == 'right':
        shift = shift % 26
    else:
        raise ValueError("Direction must be either 'left' or 'right'")

    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result