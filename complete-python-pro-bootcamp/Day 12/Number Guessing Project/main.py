import random
import art


# TODO function that generates a random number  between 1 and 100
def random_number():
    """Returns a random integer between 1 and 100"""
    return random.randint(1,100)

# TODO Set Attempt Counter
def set_attempts(difficulty):
    """Sets the number of attempts to guess the number"""
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
    return attempts


# TODO Function that Decrements the attempt count
def decrement_number(attempt):
    """Decrements the number of attempts to guess the number"""
    attempt = attempt - 1
    return attempt

# TODO Function that Evaluates the Random number against the guess
def evaluate_number(players_guess, random_num_to_guess):
    """Evaluates the players guess against the random number"""
    if players_guess == random_num_to_guess:
        print(f"You got it! The answer was {random_num_to_guess}.")
        global attempt_counter
        global win
        attempt_counter = 0
        win = True
    elif players_guess < random_num_to_guess:
        print("Too low")
    elif players_guess > random_num_to_guess:
        print("Too high")


# TODO Main code
print(art.logo2)
print("Welcome to the Number Guessing Game")
difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ")
attempt_counter = set_attempts(difficulty)
random_num = random_number()
win = False

while attempt_counter > 0:
    print(f"You have {attempt_counter} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    attempt_counter = decrement_number(attempt_counter)
    evaluate_number(guess, random_num)

if not win:
    print("You've run out of guesses. You lose!")
