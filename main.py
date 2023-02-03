MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient} to make your order.")
            return False
    return True


def process_coins(drink_cost):
    print(f"That'll be ${drink_cost}. Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    print(f"${total}")
    total += int(input("How many dimes?: ")) * 0.10
    print(f"${total}")
    total += int(input("How many nickels?: ")) * 0.05
    print(f"${total}")
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, cost_of_drink):
    if money_received >= cost_of_drink:
        change = round(money_received - cost_of_drink, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost_of_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for resource in order_ingredients:
        resources[resource] -= order_ingredients[resource]
    print(f"Here is your {drink_name} ☕️, enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        for item in resources:
            if item == "water" or item == "milk":
                print(f"{(item.capitalize())}: {resources[item]}ml")
            elif item == "coffee":
                print(f"{(item.capitalize())}: {resources[item]}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins(drink["cost"])
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])





