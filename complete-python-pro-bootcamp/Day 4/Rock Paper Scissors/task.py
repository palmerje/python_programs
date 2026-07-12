import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

player1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(choices[player1])
computer = random.randint(0, 2)
print("Computer chose: ", choices[computer])

if player1 == 0 and computer == 0:
    print("Its a draw!")
if player1 == 0 and computer == 1:
    print("You lose!")
if player1 == 0 and computer == 2:
    print("You win!")
if player1 == 1 and computer == 0:
    print("You win!")
if player1 == 1 and computer == 1:
    print("Its a draw!")
if player1 == 1 and computer == 2:
    print("You lose!")
if player1 == 2 and computer == 0:
    print("You lose!")
if player1 == 2 and computer == 1:
    print("You win!")
if player1 == 2 and computer == 2:
    print("Its a draw!")
