try:
    age = int(input("How old are you?"))
except ValueError:
    print("Please enter a valid age using a numerical value.")
    age = int(input("How old are you?"))
if age >= 18:
    print(f"You can drive at age {age}.")
else:
    print(f"You cannot drive at age {age}.")