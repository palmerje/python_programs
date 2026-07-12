import art

def add(n1, n2):
    return n1 + n2

# TODO: Write out the other three functions
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

# TODO: Add these functions into a dictionary with the keys "+" "-" "*" "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

solution = 0
while True:
    print(art.logo)
    number_1 = float(input("What's the first number: "))
    continue_calculator = True
    while continue_calculator:
        for operator in operations:
            print(operator)
        chosen_operator = input("Pick an operation: ")
        number_2 = float(input("What's the second number: "))
        solution = operations[chosen_operator](number_1, number_2)
        print(f"{number_1} {chosen_operator} {number_2} = {solution}")
        number_1 = solution
        continue_selection = input(
            f"Type 'y' to continue calculating with {solution}, "
            f"type 'n' to start a new calculation, "
            f"type 'e' to exit program: ")
        if continue_selection == "n":
            continue_calculator = False
        if continue_selection == "e":
            quit()


