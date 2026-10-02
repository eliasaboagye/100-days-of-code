import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
    '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^',
    '_', '`', '{', '|', '}', '~'
]

digits = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

print("\nWelcome to PyPassword Generator!")

nr_letters = int(input("How many numbers of letters would you like in your password: \n"))
nr_symbols = int(input("How many symbols would you like in your password: \n"))
nr_digits = int(input("How many digits would you like in your password: \n"))

frequencies = {
    "letters" : nr_letters,
    "symbols" : nr_symbols,
    "digits" : nr_digits
}
password = ""

while frequencies:
    option = random.choice(list(frequencies.keys()))
    if frequencies[option] == 0:
        del frequencies[option]
        continue
    if option == "letters":
        password += random.choice(letters)
    elif option == "symbols":
        password += random.choice(symbols)
    else:
        password += random.choice(digits)

    frequencies[option] -= 1

print(f"Your generated password is {password}")
