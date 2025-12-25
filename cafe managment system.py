#Define the menu of resturant
menu = {
    'Pizza':100,
    'Pasta':50,
    'Burger':40,
    'Salad':50,
    'Cold Coffee':60,
    'Chai':30,
    'Manchurain':70,
    'Freid Rice':60,
    'Brownie':55,
    'French Fries':70,
}

#Greet
print("Welcome to PYTHON Restraurant")
print("Pizza:100\nPasta:50\nBurger:40\nSalad:50\nCold Coffee:60\nChai:30\nManchurain:70\nFreid Rice:60\nBrownie:55\nFrench Fries:70")

order_total = 0
#70 + 50 = 120

Item_1 = input("Enter the name of item you want to order = ")
if Item_1 in menu:
    order_total += menu[Item_1]
    print(f"Your Item {Item_1} has been added to your order")

else:
     print(f"Ordered item {Item_1} is not avaiable yet")

another_order = input("Do you want to add another item ? (Yes/No)")
if another_order == "Yes":
    Item_2 = input("Enter the name of second item = ")
    if Item_2 in menu:
        order_total += menu[Item_2]
        print(f"Item{Item_2} has been added to order")
    else:
        print(f"Ordered Item {Item_2} is not avaialable")

print(f"The total amount of Items to pay is {order_total}")