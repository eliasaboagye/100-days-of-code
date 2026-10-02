

for i in range(1, 101):
    print_word = ""
    if i % 3 == 0:
        print_word += "fizz"
    if i % 5 == 0:
        print_word += "buzz"
        
    if len(print_word) > 0:
        print(print_word)
    else:
        print(i)