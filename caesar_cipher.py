
lowercase_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
def encrypt(message, shift):
    encrypt_message = ""
    for char in message:
        if char ==  " " or char.isdigit():
            encrypt_message += char
        else:
            encrypt_message += lowercase_letters[(lowercase_letters.index(char) + shift) % 26]
    return encrypt_message

def decrypt(message, shift):
    return encrypt(message, -shift)


while True:
    toDo = input("\nWelcome to Caesar Cipher. Type \"encode\" to encrypt message or \"decode\" to decrypt message.\n").lower()
    message = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    if toDo == "encode":
        print("The encoded message is", encrypt(message, shift))
    else:
        print("The decoded message is", decrypt(message, shift))

    quit = input("Type \"yes\" if you want to continue. Otherwise type \"no\". ").lower()
    if quit == "no":
        break