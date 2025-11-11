def game_start ():
    print("Hewo Pwincess UwU \n Du ska ange en gissning som följd av fyra siffror!")
    numb = input("Ange fyra siffror mellan och inklusive 1-6:")
    replaced = numb.replace(" ","")
    #Denna biten printar först ut ett välkomst medelande som också get en kort förklaring av vad spelaren ska göra. Därefter defineras variabel "numb" och man får ange siffror.
    #Till sist byter den ut alla mellanslag som spelaren skrev in till inget.

    while True:
        lst = []
        #take an input
        length = len(replaced) #chheck length
        if length != 4:
            print("Wrong")
            continue
    #En while loop påbörjas. Loopen definerar först variabel "lst". Därefter checkar den om de nummer spelaren skrev in i inputen har exakt 4 siffror.
    #Om det inte är 4 siffror printar den ut "wrong" och man får skriva in några siffror igen tills det är 4 st siffror och koden fortsätter till nästa steg med "continue".

        for num in replaced:
            try:
                num = int(num)
                if num > 6 or num < 1:
                    print("Try again, too big or too small")
                    break
                lst.append(num)
                #append add smoethign to a list
                #[].append(1)
                #[1]

            except ValueError: #this means they answered a bokstav nto number
                print("Try again")
        if len(lst) == 4:
            break
    return lst

print(game_start())
        #Biten här påbörjar en For-loop.
        #Eftersom nummrerna spelaren skrev in räknas som en string, skriver man en kod för att omvandla stringen till integer.
        #Den checkar om nummrerna spelaren skrev in är nummer mellan och inklusive 1-6
        #Om en eller flera nummer är mindre än 1 eller högre än 6 printar den ut ett medelande som säger till spelaren att försöka igen.
        #Koden ger en error om man har skrivit en bokstav och printar ett medelande



#    print ("error, too many numbers")
#elif l < 1:
#    print ("error, too little numbers")
#else:
