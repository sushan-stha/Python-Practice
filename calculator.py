num1 = float(input("Enter the 1st number:"))
operator = input("Please select an operator(+ - * /):")
num2 = float(input("Enter the 2nd number:"))

if operator == "+":
    res = num1+num2
    print(f"Sum is: {round(res, 3)}")
elif operator == "-":
    res = num1-num2
    print(f"Subtraction is: {round(res, 3)}")
elif operator == "*":
    res = num1*num2
    print(f"Product is: {round(res, 3)}")
elif operator == "/":
    res = num1/num2
    print(f"Division is: {round(res, 3)}")
else:
    print(f"{operator} is not valid operator")