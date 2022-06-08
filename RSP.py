import random


def Rock_rule():
    if player_choice == "Rock" and computer_choice == selection[2]:
        print("Player wins")
       
    if computer_choice == selection[0] and player_choice == "Scissors":
        print("CPU wins")
      


def Paper_rule():
    if player_choice == "Papers" and computer_choice == selection[0]:
        print("Player wins")
     
    if computer_choice == selection[1] and player_choice == "Rock":
        print("CPU wins")
      


def Scissors_rule():
    if player_choice == "Scissors" and computer_choice == selection[1]:
        print("Player wins")
      
    if computer_choice == selection[2] and player_choice == "Papers":
        print("CPU wins")
      


def Tie_rule():
    if player_choice == computer_choice:
        print("Tie")


selection = ["Rock", "Papers", "Scissors"]

choice = True

while choice:
    print("welcome to Rock Paper Scissors game")
    player_choice = input(
        "which one will you like to select? (Rock Papers Scissors)\n")
    computer_choice = random.choice(selection)

    print("Player: %a" % player_choice)
    print("CPU: %a" % computer_choice)

    if player_choice == "Rock" or computer_choice == selection[0]:
        print(Rock_rule())

    elif player_choice == computer_choice:
        Tie_rule()

    elif player_choice == "Papers" or computer_choice == selection[1]:
        Paper_rule()

    elif player_choice == "Scissors" or computer_choice == selection[2]:
        Scissors_rule()

    else:
        print("not amongst our option")
