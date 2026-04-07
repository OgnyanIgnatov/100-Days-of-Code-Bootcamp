MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def report():
    for key, value in resources.items():
        print(f"{key} = {value} ml")
    print(f"Money: ${profit}")

def check_suffieciency(drink):
    for ingr, value in drink["ingredients"].items():
        if resources[ingr] < value:
            print(f"Not enough {ingr}")
            return False
    
    return True

def process_coins():
    pennies = int(input("How many pennies?: "))
    nickels = int(input("How many nickels?: "))
    dimes = int(input("How many dimes?: "))
    quarters = int(input("Hoe many quarters?: "))

    return pennies*0.01 + nickels*0.05 + dimes*0.10 + quarters*0.25

def process_change(total, drink_price):
    return total - drink_price

def load_machine():
    if resources["water"] <= 250:
        resources["water"] += 500

    if resources["milk"] <= 100:
        resources["milk"] +=100

    if resources["coffee"] <= 50:
        resources["coffee"] += 50


def Coffee_Machine():
    global profit
    

    while True:
        order = input("Welcome to The Coffee Machine! What would you like to order? (espresso, latte or cappuccino): ")

        if order == "report":
            report()
        elif order == "off":
            break
        elif order == "espresso" or order == "latte" or order == "cappuccino":
            if check_suffieciency(MENU[order]):
                total = process_coins()
                drink_price = MENU[order]["cost"]

                if total < drink_price:
                    print("Not enough money! Money returned")
                    continue

                profit += drink_price
                change = process_change(total, drink_price)

                for res in resources:
                    resources[res] -= MENU[order]["ingredients"][res]


                print(f"Here is ${change:.2f} in change!")
                print(f"Here is you {order}! Enjoy your drink!")

            else:
                print("Machine is loaded!")
                load_machine()
                continue



Coffee_Machine()





