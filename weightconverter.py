# PYTHON WEIGHT CONVERTER
weight = float(input("Enter your weight:"))
unit = input("Enter K for Kilograms and P for Pounds:")


if unit == "K":
    weight = weight*2.205
    print(f"Your weight in Pounds is: {round(weight)}")
elif unit == "P":
    weight = weight/2.205
    print(f"Your weight in Kilograms is: {weight}")
else:
    print(f"{unit} is invalid!!!")


