# Turtle Race Project
import turtle
import random
from pyautogui import alert, prompt

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan", "magenta"]



def no_of_racers():
    racers = 0
    
    while True:
        racers = prompt("Enter the number of racers (2-10) or 'q' to quit:", "Racer Members")
        try:
            if racers != "q":
                if racers.isdigit():
                    racers = int(racers)
                    if 2 <= racers <= 10:
                        return racers
                    else:
                        alert("Please enter a number between 2 and 10.", "Error", "Try Again")
                else:
                    alert("Invalid input.", "Error", "Try Again")
            else:
                alert("Quitting race...", "Race Quit", "Quit")
                quit()
        except AttributeError:
            # alert("Please enter something...", "Error", "Try Again")
            pass

def race_track():
    screen = turtle.Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.title("Race Track")

def race(colors):
    turtles = create_racers(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 10)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_racers(color):
    turtles = []
    position = WIDTH // (len(color) + 1)
    for i, color in enumerate(color):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * position, -HEIGHT // 2 + 20)
        racer.pendown()

        turtles.append(racer) 

    return turtles 

def bet():
    total_turtels = no_of_racers()
    while True:
        bet_turtle = prompt("Enter the possion NO of the turtle you want to bet on:", "Betting")

        if bet_turtle.isdigit():
            bet_turtle = int(bet_turtle)
        
        else:
            alert("Invalid input. Please enter a number.", "Error", "Try Again")
            continue
        

        if bet_turtle > total_turtels:
            alert(f"Please enter a number between 1 and {total_turtels}.", "Error", "Try Again")
            continue
        elif bet_turtle < 1:
            alert("Please enter a number greater than 0.", "Error", "Try Again")
            continue
        else:
            alert(f"You have placed a bet on turtle number {bet_turtle}.", "Bet Placed", "start race")
            return bet_turtle, total_turtels

        
def main():
    bet_turtel, racers = bet()

    race_track()

    random.shuffle(COLORS)
    colors = COLORS[:racers]

    bet_turtel
    winner = race(colors)
    if winner == colors[bet_turtel - 1]:
        alert(f"Congratulations! You won the bet on the {winner} turtle!", "Bet Result", "Close")

    else:
        alert(f"Sorry! You lost the bet. The {winner} turtle won the race.", "Bet Result", "Close")

