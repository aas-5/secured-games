import random
import pyautogui as gui

PASSWORD_CHR = []


def random_password():
    while True:
        random_pass = []
        password_length = gui.prompt("Enter the desired password length (must be between 8 and 12):")

        if password_length is not None and password_length.isdigit():
            password_length = int(password_length)

            if 8 <= password_length <= 12:
                for i in range(10):
                    PASSWORD_CHR.append(i)

                for i in range(password_length):
                    random_chr = random.choice(PASSWORD_CHR)
                    random_pass.append(str(random_chr))

                # password = "".join(random_pass)
                break
            else:
                gui.alert("Invalid input. Please enter a number between 8 and 12.")
                continue
        else:
            gui.alert("Invalid input. Please enter a number between 8 and 12.")
            continue

    return random_pass


