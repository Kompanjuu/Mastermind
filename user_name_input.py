
import useful_functions 

def get_user_name():
    print("What is your name?")

    while True:
        name = input("-> ")
        answer = input(f"""{name}, is that correct? 
Enter 'no' to retry
-> """)
        answer = useful_functions.clean_string(answer)
        if answer == "no":
            print("Lets retry.")
            continue
        else:
            break
get_user_name()
#this functions gets a name out of the player

