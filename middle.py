

#[1, 2, 3, 4]
#always 

def middle(pers, dator): #pers = persons guess, dator = correct answer.
    answer = [0, 0, 0, 0] #2 = just in it, 1 = right spot?, 0 = nothing
    for i in range(4):#result will 
        if pers[i] == dator[i]: #same position.
            answer[i] = 1
            dator[i] = -1 #this number can't be counted twice now, dator.remove(dator[i]) is slower.

        elif pers[i] in dator: #this will onkly happen if they are not same position
            answer[i] = 2 #2 = included but wrong position
            dator[i] = -1 #Same reason
    
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

print(middle([2, 2, 3 , 4], [3, 2, 1, 5]))