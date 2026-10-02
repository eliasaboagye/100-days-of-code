import random
hangman =[
"""
    +-----+
    |     |
    |     
    |    
    |
    |
    |
============
""",
"""
    +-----+
    |     |
    |     O
    |    
    |    
    |
    |
============
""",
"""
    +-----+
    |     |
    |     O
    |    /
    |    
    |
    |
============
""",
"""
    +-----+
    |     |
    |     O
    |    /|
    |    
    |
    |
============
""",

"""
    +-----+
    |     |
    |     O
    |    /|\\
    |    
    |
    |
============
""",
"""
    +-----+
    |     |
    |     O
    |    /|\\
    |    / 
    |
    |
============
""",
"""
    +-----+
    |     |
    |     O
    |    /|\\
    |    / \\
    |
    |
============
"""
]

def draw_hangman(n):
    print(hangman[6-n])

def make_word(char_list):
    word = ""
    for char in char_list:
        word += char + " "
    return word
lives = 6
word_list = ["hangman", "creature", "chosen", "word"]
word = random.choice(word_list)
guess_list = ["_"] * len(word)
guess_word = make_word(guess_list)
while lives > 0 and "_" in guess_list:
    print(f"{guess_word}")
    guess = input("Enter a letter:\n").lower()
    guessed_right = False
    for i in range(len(word)):
        if word[i] == guess:
            guess_list[i] = word[i]
            guessed_right = True

    if not guessed_right:
        print(f"\nYou guessed {guess}, that's not in the word. You lost a life.")
        lives -= 1
    else:
        guess_word = make_word(guess_list)
        print(f"{guess_word}")
    draw_hangman(lives)
if lives > 0:
    print("\nCongratulations. You Won!!!")
else:
    print("\nYou lost :(, Better luck next time")


    

    