
# Range function with for loop
for number in range(1,10):
    print(number)

# Find total of all numbers from 1 to 100
total = 0
for number in range(1,101):
    total += number
print(total)

#Gauss Challenge
for number in range(1, 101):
    if (number%3 == 0)and(number%5 == 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)