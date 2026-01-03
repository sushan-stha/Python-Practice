unit = input("Is temperature in Celsius or Farenheit (C/F):")
temp = float(input("Enter the temperatue:"))
if(unit == "C"):
    temp = round((9*temp)/5 + 32, 1)
    print(f"The temperature in farenheit is:{temp}")
elif(unit == "F"):
    temp = round(temp - 32)*5/9 
    print(f"The temperature in celsius is: {temp}")
else:
    print(f"{unit}is Invalid!!!")