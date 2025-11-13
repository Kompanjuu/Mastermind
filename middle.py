

#[1, 2, 3, 4]
#always 

def middle(pers, dator): #pers = persons guess, dator = correct answer.
    answer = [0, 0, 0, 0] #2 = just in it, 1 = right spot?, 0 = nothing
    
    temp_pers = [] #make a copy
    for i in pers:
        temp_pers.append(i)
    temp_dator = []
    for i in dator:
        temp_dator.append(i)
    
    for i in range(4):
        #first for look through for all the matches
        if temp_pers[i] == temp_dator[i]: #same position.
            answer[i] = 1 #1 = right position
            temp_dator[i] = -1 #this number can't be counted twice now, temp_dator.remove(temp_dator[i]) is slower.
            temp_pers[i] = -2 
            #this number isnt the same as temp_dator because we dont want them to match up -1
            #this is also why i made a temp_pers
    for i in range(4):
        #then look for all the other
        if temp_pers[i] in temp_dator: #this will onkly happen if they are not same position
            match_index = temp_dator.index(temp_pers[i]) #find the index of this match

            answer[i] = 2 #2 = included but wrong position
            temp_dator[match_index] = -1 #Same reason
            temp_pers[i] = -2

    answer.sort() #makes smallest first aka the checkmarks first
    output = [] 
    for result in answer:
        match result:
            case 1:
                output.append("✅") 

            case 2:
                output.append("❎")
            #case 0: do nothing
    return output                

print(middle([4, 3, 2, 1], [1, 2, 3, 4]))
