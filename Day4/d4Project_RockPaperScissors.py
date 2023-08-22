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

#Write your code below this line 👇

import random

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.randint(0, 2)

choices = [rock, paper, scissors]

print(user_choice)
print(choices[user_choice])

print("Computer chose:")
print(choices[computer_choice])

if user_choice == computer_choice:
    print("It's a draw")
elif user_choice == 0:
    if computer_choice == 1:
        print("You lose")
    else:
        print("You win")
elif user_choice == 1:
    if computer_choice == 2:
        print("You lose")
    else:
        print("You win")
elif user_choice == 2:
    if computer_choice == 0:
        print("You lose")
    else:
        print("You win")
