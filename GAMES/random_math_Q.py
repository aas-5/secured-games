import random as r
import time
import pyautogui as gui

def math_game():
    operators = ['+', '-', '*']
    min_value = 3
    max_value = 12
    total_problems = 10

    def problem_generator():
        random_operator = r.choice(operators)
        left = r.randint(min_value, max_value)
        right = r.randint(min_value, max_value)

        expression = f"{str(left)} {random_operator} {str(right)}"
        answer = round(eval(expression))

        return expression, answer

    wrong = 0

    gui.alert("Press Start to begin the challenge...", title="Math Challenge", button="Start")

    start_time = time.time()

    for i in range(total_problems):
        expression, answer = problem_generator()
        while True:
            guess = gui.prompt(f"{expression} = ", title=f"Problem #{i + 1}:")
            if guess == str(answer):
                break
            elif guess is None:
                gui.alert(f"You quit the challenge at problem #{i + 1}.")
                quit()
            wrong += 1

    end_time = time.time()
    total_time = end_time - start_time

    gui.alert(f"Congratulations! Challenge completed! You made {wrong} mistakes and took {round(total_time, 2)} seconds to complete the challenge. Try again to improve your score.", title="Challenge Completed!")