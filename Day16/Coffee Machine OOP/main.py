from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def report(coffee_machine, money_machine):
    coffee_machine.report()
    money_machine.report()


def coffeeMachine():
    menu = Menu()
    machine = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        order = input(f"Welcome to the Coffee Machine! What would you like? {menu.get_items()}: ")

        if order == "report":
            report(machine, money_machine)
        elif order == "off":
            break
        elif order == "latte" or order == "espresso" or order == "cappuccino":
            drink = menu.find_drink(order)

            if machine.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    machine.make_coffee(drink)            

coffeeMachine()
