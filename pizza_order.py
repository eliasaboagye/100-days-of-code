
small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25
pepperoni_s_price = 2
pepperoni_m_l_price = 3
extra_cheese_price = 1

size = input("Input pizza size (S, M, L): ")
add_pepperoni = input("Do you want pepperoni? (Y or N): ")
add_extra_cheese = input("Do you want extra cheese? (Y or N): ")


price = 0

if size == "S":
    price = small_pizza_price
   
elif size == "M":
    price = medium_pizza_price
   
else:
    price = large_pizza_price

if add_pepperoni == "Y":
        if size == "S":
            price += pepperoni_s_price
        else:
            price += pepperoni_m_l_price

if add_extra_cheese == "Y":
    price += extra_cheese_price

print(f"Your final bill is: ${price}")