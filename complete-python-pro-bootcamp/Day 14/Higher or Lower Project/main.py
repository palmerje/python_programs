import random
import art
import game_data

# TODO assign a random game_data list entry to A and a random entry to B
person_a = random.choice(game_data.data)
person_b = random.choice(game_data.data)
player_score = 0
winning = True

# TODO print Logo, A data, VS symbol, and B Data
print(art.logo)

while winning:
    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
    print(art.vs)
    print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")

    # TODO Compare A and B followers, ask for guess from Player
    higher_count = ""
    if person_a['follower_count'] >= person_b['follower_count']:
        higher_count = "a"
    else:
        higher_count = "b"
    player_guess = input("Who has more followers: 'A' or 'B'? ").lower()

    # TODO If player correct, assign B value to A,
    #  assigned new random list entry to B that isn't the same as A and repeat comparison
    #  , add 1 to score count
    if player_guess == higher_count:
        player_score += 1
        print("\n"*20)
        print(art.logo)
        print(f"You're right! Current score: {player_score}")
        person_a = person_b
        while person_a == person_b:
            person_b = random.choice(game_data.data)
    else:
        print("\n" * 20)
        print(art.logo)
        print(f"Sorry that's wrong. Final Score: {player_score}")
        winning = False