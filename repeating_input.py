
import messages

def game_start ():
    txt = "│Hej spelare!│🖑"
    
    print("\n", txt.center(65), sep = "")
    print("\t ☆ Du ska ange en gissning som följd av fyra siffror!")


    while True: #contantly try to take an input until proper input is inputted.
        error_message = []
        numb = input("\t ☆ Ange fyra siffror mellan och inklusive 1-6: ")
        numb = numb.replace(" ","")
        #Denna biten printar först ut ett välkomst medelande som också get en kort förklaring av vad spelaren ska göra. Därefter defineras variabel "numb" och man får ange siffror.
        #Till sist byter den ut alla mellanslag som spelaren skrev in till inget.

        #now we have a string with no spaces. Length? Number?

        numb_lst = []
        length = len(numb) #check length
        retry = False
        if length != 4: #this filters out all thats not length 4
            error_message.append(messages.length_not_four)
            # continue, instead of directly going to the next loop lets collect everything thats wrong with the lessage
        #En while loop påbörjas. Loopen definerar först variabel "lst". Därefter checkar den om de nummer spelaren skrev in i inputen har exakt 4 siffror.
        #Om det inte är 4 siffror printar den ut "wrong" och man får skriva in några siffror igen tills det är 4 st siffror och koden fortsätter till nästa steg med "continue".
        #continue continues the loop. it goes onto the next loop.

        for num in numb: #is every individual "character" in the string once. ABCD -> A -> B -> C -> D
            try:
                num = int(num) #filters out if you inputed a bokstav
                #This will try turning the num into an integer.
                #this will fail is num is not a heltal (0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11....)
                numb_lst.append(num)
            except ValueError: #this means they answered a bokstav nto number
                error_message.append(messages.not_integers)
                break


        for num in numb_lst: #this is a list of 4 integers (heltal). We want to chack the range.
            if num > 6 or num < 1: #Another filter. we check if its withtin the range that we allow (1 to 6)
                error_message.append(messages.int_not_within_range)
                break
            #append add smoethign to a list
            #[].append(1)
            #[1]
        if len(error_message) > 0: #this is a collected place where all the errors gets sent./Hanna
            error_message = list(map(lambda x: " ☆ " + x, error_message))#this adds a "☆ " before each message. Cleaner looking
            print("\nSecret hints just for you ;):" ,"\n\t","\n\t".join(error_message),"\n", sep="") #this is where the message gets send out
            continue
        break #if it psses all of our filters.
    return numb_lst
# print(game_start())
        #Biten här påbörjar en For-loop.
        #Eftersom nummrerna spelaren skrev in räknas som en string, skriver man en kod för att omvandla stringen till integer.
        #Den checkar om nummrerna spelaren skrev in är nummer mellan och inklusive 1-6
        #Om en eller flera nummer är mindre än 1 eller högre än 6 printar den ut ett medelande som säger till spelaren att försöka igen.
        #Koden ger en error om man har skrivit en bokstav och printar ett medelande


#    print ("error, too many numbers")
#elif l < 1:
#    print ("error, too little numbers")
#else:
