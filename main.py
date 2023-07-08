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

def is_resource_sufficient(order_ingredient):
    is_enough = True
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            is_enough = False
    return is_enough


def processing_coins():
    print("Insert a coins")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def is_transaction_successfully(money_received, cost_of_drink):
    if money_received >= cost_of_drink:
        change = round(money_received - cost_of_drink, 2)
        print(f"Here is the change {change}")
        global profit
        profit += cost_of_drink
        return True
    else:
        print("Sorry that is not enough money. Money is refunded")
        return False


def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name}")


is_On = True
while is_On:
    choice = input("What would you like? (espresso/latte/cappuccino) or reports: ").lower()
    if choice == "off":
        is_On = False
    elif choice == "report":
        print(f"water: {resources['water']} ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):  # Pass the correct argument
            payment = processing_coins()
            if is_transaction_successfully(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
