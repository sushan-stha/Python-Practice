foods= []
prices = []
total = 0

while True:
    food = input("Input a food you like to buy(or q to quit):")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}:Rs."))
        prices.append(price)
        foods.append(food)
        
print("-----YOUR CART-----")

for food in foods:
    print(food, end="  ")

for price in prices:
    total += price

print()
print(f"Your Total is Rs.{total} ")