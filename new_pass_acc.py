import pyautogui as gui
import random_pass_gen as pg

user = None
password = None

with open("account.txt", "r") as f:
    for line in f.readlines():
        if line == None:
            gui.alart("No account found. Please create a new account.")
    date = line.rstrip()
    user, password = date.split(" | ")
    default_pass = password.rsplit(': ')[1]

def pass_gen():
        random_password = pg.random_password()
        password = "".join(random_password)
        return str(password)


#access denied protocall
def access_denied():
        access_denied = gui.confirm("Access denied.", buttons=("proceed", "quit"))

        if access_denied == "proceed":
            action = gui.confirm("Do you want to change the password or create a new account?", buttons=("new password", "new account")).lower()
            
            while True:
                if action == "new password":
                    name = user.rsplit(': ')[1]
                    way = gui.confirm("Do you want to generate a password or create your own?", buttons=("generate", "use my own")).lower()
                    
                    if way == "use my own":
                        password = gui.password("New password: ")
                        confirm_pass = gui.password("Confirm password: ")
                        
                        if password != confirm_pass:
                            gui.alert("Passwords do not match. Please try again.")
                            continue
                        else:
                            with open("account.txt", "w") as f:
                                f.write(f"name: {name} | password: {password}\n")
                            gui.alert("Master password updated successfully.")
                            quit()

                    elif way == "generate":
                        random_pass = None
                        
                        while True:
                            random_pass = pass_gen()

                            gen_pass = gui.confirm(f"Random password: {random_pass}", "Generated password", buttons=("use", "regenerate")).lower()

                            if gen_pass == "use":
                                with open("account.txt", "w") as f:
                                    f.write(f"name: {name} | password: {random_pass}\n")
                                gui.alert("Master password updated successfully.")
                                quit()

                            elif gen_pass == "regenerate":
                                continue
                            

                elif action == "new account":
                    name = gui.prompt("Enter a new account name: ")
                    way = gui.confirm("Do you want to generate a password or create your own?", buttons=("generate", "use my own")).lower()
                    
                    if way == "generate":
                        random_pass = None

                        while True:
                            random_pass = pass_gen()

                            gen_pass = gui.confirm(f"Random password: {random_pass}", "Generated password", buttons=("use", "regenerate")).lower()

                            if gen_pass == "use":
                                with open("account.txt", "w") as f:
                                    f.write(f"name: {name} | password: {random_pass}\n")
                                gui.alert("Master password updated successfully.")
                                quit()

                            elif gen_pass == "regenerate":
                                continue

                        
                    elif way == "use my own":
                        password = gui.password("New password: ")
                        confirm_pass = gui.password("Confirm password: ")

                        if password != confirm_pass:
                            gui.alert("Passwords do not match. Please try again.")
                            continue

                        else:
                            with open("account.txt", "w") as f:
                                f.write(f"name: {name} | password: {password}\n")
                            gui.alert("Master password updated successfully.")
                            quit()
                    
                elif action == "no":
                    gui.alert("No changes made. Quitting the program.")
                    break

        elif access_denied == "quit":
            gui.alert("Exiting the program.")
            quit()



