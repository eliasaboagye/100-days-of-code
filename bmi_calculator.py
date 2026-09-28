#get height 
height = float(input("Enter height in meters(m): "))
weight = float(input("Enter weight in kilograms(kg): "))
bmi = round(weight / (height ** 2))
print(f"Your bmi is {bmi :.2f}")
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
elif bmi < 30:
    print("overweight")
elif bmi < 35:
    print("obese")
else:
    print("clinically obese")
    
