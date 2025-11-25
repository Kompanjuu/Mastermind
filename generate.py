#Refer to Hanna


#plan
# Generate a four number combination:
# random 1-6 and include them too.
# One with no repeating
# one that can be repeating

import random as rand

def generate(mode): #returns the gerenated sequence as a list
    possible_numbers = [1, 2, 3, 4, 5, 6]
    if mode == 1: #for easy mode
        combination = [] #i'll make this a list because the difficult is a list aswell easier to return
        
        for _ in range(4): #generate 4 numbers
            num = rand.choice(possible_numbers)
            combination.append(num)
            possible_numbers.remove(num) #This makes it so that the number can't repeat. Time complexity: at worst O(5+4+3) basically 0
        return combination
    #for difficult mode
    elif mode == 2:
        return rand.choices(possible_numbers, k = 4)

    #this will return a combination of length four as a list. Can repeat.

#this is a code that will return a combination of numbers between and including 1-6, variating depending on mode. 
# The return will be in the form of a list.