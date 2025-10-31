import random
import pyautogui as gui

def rock_paper_scissors():
    user_win = 0   # score
    computer_win = 0
    draw = 0

    options = ["rock", "paper", "scissors"]

    gui.alert("This is a game of Rock, Paper, Scissors. Press OK to start.", title="Rock Paper Scissors Game")

    rounds = 5
    for i in range(rounds):
        user_choice = gui.confirm("Pick your option:", buttons=("rock", "paper", "scissors", "quit"), title="User Choice")  # user choice
        if user_choice == "quit":  # to quit the game
            quit()

        random_number = random.randint(0, 2)  # random number for computer to make a choice

        computer_choice = options[random_number]  # computer's choice
        gui.alert(f"you: {user_choice}\ncomputer: {computer_choice}", title="Choices")  # show computer choice

        if user_choice == computer_choice:
            draw += 1
        elif user_choice == "rock" and computer_choice == "scissors":
            user_win += 1
        elif user_choice == "paper" and computer_choice == "rock":
            user_win += 1
        elif user_choice == "scissors" and computer_choice == "paper":
            user_win += 1
        else:
            computer_win += 1

    gui.alert(f"User score: {user_win}, Computer score: {computer_win}, Draws: {draw}", title="Game Score")

    if user_win > computer_win:
        gui.alert("You won!", title="Winner")
    elif computer_win > user_win:
        gui.alert("You lost!", title="Winner")
    else:
        gui.alert("It's a tie!", title="Winner")

