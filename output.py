def output(numbers, results):
    print(f"Runda |{"Testade koder": ^22}| Feedback :)") #Översta raden
    print(f"{"":-<43}")
    for i in range(11,-1,-1):
        #Loopar igenom omgångarna
        if len(numbers)-1 < i:
            #Om omgången som ska printas ej har körts
            print(f"{(i+1): ^6}|{"": >22}|") 
            #Rad med en siffra för omgång
            print(f"{"": ^6}|{"": <22}|") 
            #Mellanrad
        else:
            #Om omgången som ska printas har körts
            print(f"{(i+1): ^6}| {numbers[i][0]: ^5}{numbers[i][1]: ^5}{numbers[i][2]: ^5}{numbers[i][3]: ^5} | {results[i]: <10}")
            #Rad med en siffra för omgång, gissade värden och respons
            
            #Extrasaker för en mellanrad:
            if "✅" in results[i]: 
                #Mellanrad som får extra feedback om man har gjort något bra
                if len(results[i]) > 2: #Om många saker är rätt
                    print(f"{"": ^6}|{"": <22}| Fantastiskt❤️")
                else: #Om få saker är rätt
                    print(f"{"": ^6}|{"": <22}| Snyggt🔥")
            else:
                print(f"{"": ^6}|{"": <22}|") 
                #Mellanrad som inte får extra feedback
    print(f"{"":-<43}") 
#Debugging
# list1 = [[1,2,3,4],[2,3,4,5],[3,4,5,6],[1,2,2,2]]
# list2 = ["✅","","✅✅✅",""]
# output(list1,list2)