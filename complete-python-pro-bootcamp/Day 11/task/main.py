import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = []
player_hand = []

def deal_player_cards():
    another_card = True
    while another_card:
        print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
        print(f"Dealer's hand: {dealer_hand}")
        hit_me =input(f"Do you want another card? Type 'y' or 'n': ")
        if hit_me == "n":
            another_card = False
        if hit_me == "y":
            player_hand.append(random.choice(cards))
        if sum(player_hand) > 21:
            if 11 in player_hand:
                player_hand.remove(11)
                player_hand.append(1)
            else:
                break

def deal_dealer_cards():
    dealer_hand.append(random.choice(cards))
    if sum(player_hand) <= 21:
        while sum(dealer_hand) < 17:
            dealer_hand.append(random.choice(cards))

def final_score_check():
    if sum(player_hand) > 21:
        print("You Busted, You lose!")
    elif sum(dealer_hand) > 21:
        print("Dealer Busts, You Win!")
    elif sum(player_hand) > sum(dealer_hand):
        print("You Win!")
    elif sum(player_hand) < sum(dealer_hand):
        print("You Lose!")
    elif sum(player_hand) == sum(dealer_hand):
        print("Its a Draw!")


#Initial Game Start
print(art.logo)
start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
play_blackjack = False
if start_game == "y":
    play_blackjack = True

while play_blackjack:
    #inital hands
    dealer_hand = []
    player_hand = []
    dealer_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))

    # Player's Hand Dealing
    deal_player_cards()

    # Dealer's Hand Dealing
    deal_dealer_cards()

    #Final Score
    print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
    print(f"Dealer's final hand: {dealer_hand}, dealer's score: {sum(dealer_hand)}")
    final_score_check()

    start_game = input("Do you want to play another game? Type 'y' or 'n': ")
    if start_game == "n":
        play_blackjack = False
    print(" "*100)
    print(art.logo)




