alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(inputed_text, shift_amount):
    ciphered_text = ""
    for letter in inputed_text:
        position = alphabet.index(letter)
        new_position = position + int(shift_amount)
        new_letter = alphabet[new_position]
        ciphered_text += new_letter
    print(f"the encrypted text is: {ciphered_text}")   
def decrypt(ciphered_text, shift_amount):
    decrypted_text = ""
    for letter in ciphered_text:
        position2 = alphabet.index(letter)
        new_position2 = position2 - int(shift_amount)
        new_letter2 = alphabet[new_position2]
        decrypted_text += new_letter2
    print(f"the decrypted text is: {decrypted_text}")
    
if direction == "encode":
    encrypt(text, shift)
if direction == "decode":
    decrypt(text,shift)