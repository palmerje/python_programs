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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}


def power_off_machine():
    """Powers off machine, exits code"""
    print("Powering down coffee machine!")
    quit()


def print_report():
    """Prints report of money and resources available"""
    print("System Report:")
    print(f"water: {resources['water']}")
    print(f"milk: {resources['milk']}")
    print(f"coffee: {resources['coffee']}")
    print(f"money: ${resources['money']}")

def resource_check(selection):
    """Checks if resource is available, returns True if available, False if not"""
    enough_resources_available = True
    for ingredient, value in MENU[selection]["ingredients"].items():
        if value > resources[ingredient]:
            enough_resources_available = False
    return enough_resources_available


def collect_money(selection):
    """Collects money from the user, returns if enough money, returns change, adds money to machine resources"""
    print("Please insert money:")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total_input = (quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
    if total_input < MENU[selection]["cost"]:
        print("Sorry, you don't have enough money! Money refunded")
        enough_money_collected = False
        print(f"Money refunded: ${total_input}")
        return enough_money_collected
    else:
        enough_money_collected = True
        print(f"Thank you! Your change is: ${total_input - MENU[selection]["cost"]}")
        resources['money'] += MENU[selection]["cost"]
        return enough_money_collected


# ********************** Main Code *****************************

machine_on = True
while machine_on:
    user_selection = input("What would you like? Type espresso, latte, or cappuccino: ")

    if user_selection == "off":
        power_off_machine()
    elif user_selection == "report":
        print_report()
    else:
        enough_resources = resource_check(user_selection)
        if enough_resources:
            enough_money = collect_money(user_selection)
            if enough_resources and enough_money:
                for ingredient, value in MENU[user_selection]["ingredients"].items():
                    resources[ingredient] -= value
                print(f"Here is your {user_selection}! Enjoy!")
        else:
            print("Sorry, machine needs more ingredients!")
    print(f"\n"*2)

