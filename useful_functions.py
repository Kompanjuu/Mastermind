

# *arg - list format
# *kwarg  dicitonary

    # regular parameters
    # *args
    # **kwargs

def single_int_input(): #when you jsut want a number: 1234, 1, 9000 not 0009
    while True:
        user_input = input()
        try:
            user_input = int("".join(char for char in user_input if char != " ")) #gets rid of spaces and turns it into a string
            return user_input
        except ValueError: #if it become value error then do this instead
            print("Please enter a string of numbers")

def clean_string(user_input):
    user_input = "".join(char for char in user_input if char != " "); user_input.lower()
    return user_input


#go trhough the string and if the word is in the long rando string then it works
#like virus question
#for i in word (word = "hugjdkslaujigkdsmbhgsioalchfdjkslfd")
#abcd is it in.
#lghsidjkhgdsjkähjgjdskhgsjkdtjgidoslkngldst
#hgsjdkghnjeskbgdlättbidhkghdsjihgsnd       ___..--
 

def single_include_string_input(requirement, message):
    #just enter with a list of the things you want the the string to be part of
    while True:
        user_input = input()
        user_input = "".join(char for char in user_input if char != " "); user_input.lower()
            #gone with all spaces. O(n) space.
        if user_input in requirement:
            return user_input
        else:
            print(message)


# def safe_input(user_input, *restrictions, **mode): #for now its just an input
#     #restrictions should be in a list format.
#     #input, restriction_list, Exclude = False, (String = False)
#     #the input will be in string format
#     ##if you want input as a word then String = True, If input as int then String = False (defult)
#     #if you want exclude == True then the list is of stuff you wanan include, else it's Exclude = False (defult)
#     #be in the format 
    
#     if len(mode) > 0: #you have some mode
#         mode["Exclude"]

    
#     print(user_input)
#     print(restrictions)
#     print(mode)
#safe_input(3, Exclude = True) #true means the thing has to be included

import sys
import threading
import time
def listen_for_enter():
    global sleep_write_stopped
    while True:
        char = sys.stdin.read(1)
        #if char == " ":
        sleep_write_stopped = True
        break

def sleep_write(word):
    global sleep_write_stopped
    sleep_write_stopped = False
    listener = threading.Thread(target=listen_for_enter, daemon=True)
    listener.start()
    for i in word:
        print(i, flush = True, end="")
        if not sleep_write_stopped:
            time.sleep(0.03)
    print("")

# 
# # time.sleep(seconds)
# import messages
# word = messages.welcome_introduction
# for i in word:
#     print(i, end="", flush = True)
#     time.sleep(0.03)

