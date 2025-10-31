import pyautogui as gui
import random

# Asking the user whether to play or not
def guess_number():
    gui.alert("""
Welcome to the Guessing Game!
You have 3 chances to guess the number between 0 and 10.
Click OK to play or close to quit.
""")
    # Game
    random_number = random.randint(0, 10)
    i = 0
    while i < 3:
        guess = gui.prompt("Guess the number:", title="Guess the Number")
        if guess is None:
            gui.alert("Game quit.")
            quit()
        elif guess.isdigit():
            guess = int(guess)
            if guess == random_number:
                gui.alert("Congratulations! You won!", title="You Won", button="OK")
                quit()
            else:
                i += 1
        else:
            gui.alert("Please enter a valid number.")

    gui.alert("All 3 of your guesses were wrong. You lost.", title="Game Over")