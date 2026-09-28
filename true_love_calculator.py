
print("WELCOME TO TRUE LOVE CALCULATOR!!!!\n\n")
my_name = input("Input your name: ")
crush_name = input("Input your crush's name: ")

combined_name = my_name.lower() + crush_name.lower()

t_count = combined_name.count("t")
r_count = combined_name.count("r")
u_count = combined_name.count("u")
e_count= combined_name.count("e")
l_count = combined_name.count("l")
o_count = combined_name.count("o")
v_count = combined_name.count("v")

true_count = t_count + r_count + u_count + e_count
love_count = l_count + o_count + v_count + e_count

print(f"\nT occurs {t_count} times\nR occurs {r_count} times\nU occurs {u_count} times\nE occurs {e_count} times")
print(f"Total = {true_count}\n")

print(f"L occurs {l_count} times\nO occurs {o_count} times\nV occurs {v_count} times\nE occurs {e_count} times")
print(f"Total = {love_count}\n")


percentage = true_count * 10 + love_count

if percentage < 10 or percentage > 90:
    print(f"Your score is {percentage}, and you go together like coke and mentos.")
elif percentage > 40 and percentage < 50:
    print(f"Your score is {percentage}. You are alright together.")
else:
    print(f"Your score is {percentage}")