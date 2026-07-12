import random
import my_module

#random_integer = random.randint(1, 10)

#print(random_integer)

#print(my_module.my_favorite_number)

#random_number_0_to_1 = random.random() * 10
#print(random_number_0_to_1)

#random_float = random.uniform(0, 10)
#print(random_float)


random_integer = random.randint(1, 10)
if random_integer % 2 == 0:
    print("Heads")
else:
    print("Tails")
