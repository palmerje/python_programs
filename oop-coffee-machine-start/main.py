from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

machine_on = True

while machine_on:
    print("Welcome to the coffee machine!")
    options = menu.get_items()
    order_name = input(f"What would you like? ({options}): ")
    if order_name == "report":
        coffee_maker.report()
        money_machine.report()
    elif order_name == "off":
        print("Powering down coffee machine!")
        quit()
    else:
        order_to_make = menu.find_drink(order_name)
        if order_to_make != None:
            if coffee_maker.is_resource_sufficient(order_to_make):
                if money_machine.make_payment(order_to_make.cost):
                    coffee_maker.make_coffee(order_to_make)
    print("\n"*2)


