import pyautogui as gui
#password and account creator 
import new_pass_acc as acc
#games
from GAMES import turtle_race as race
from GAMES import random_math_Q as math_q
from GAMES import rps
from GAMES import guessing_game



while True:
    main_pass = gui.password("master password (q to quit): ", title="Security System") #user input password

    default_pass = acc.default_pass #saved password

    #access granted protocall
    def access_granted():
        gui.alert("Access granted. Welcome to the games hub!")
        path = gui.confirm("chose what do you want to access:", title="access path", buttons=("account menager", "games", "quit"))
        
        #path access to games
        if path == "games":
            game = gui.confirm("Choose your game", title="Games", buttons=("turtle race", "random math question", "rock paper scissors", "guessing game", "quit"))

            if game == "turtle race":
                race.main()
            elif game == "random math question":
                a = math_q.math_game()
            elif game == "rock paper scissors":
                rps.rock_paper_scissors()
            elif game == "guessing game":
                guessing_game.guess_number()
            else:
                gui.alert("More interesting games are coming soon. Quitting for now...")
                quit()

        elif path == "account menager":
            acc.access_denied()

        elif path == "quit":
            gui.alert("exiting the program...")
            quit()
            

        
    #acces denied protocall
    def access_denied():
        acc.access_denied()

    #main check ups
    if main_pass == "q":
        gui.alert("Exiting the program.")
        quit()
    elif main_pass == default_pass:
        access_granted()
        break
    else:
        wrong_pass = gui.confirm("Incorrect password. Do you want to try again or change the password/account?", buttons=("try again", "change password/account", "quit"))

        if wrong_pass == "try again":
            continue
        elif wrong_pass == "change password/account":
            access_denied()
            break
        else:
            gui.alert("Exiting the program.")
            quit()