# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

#Function with more than 1 input

def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")

#positional arguments
greet_with("Jack Bauer", "Nowhere")

#Key word Arguments
greet_with(location="Nowhere", name="Jack Bauer")
