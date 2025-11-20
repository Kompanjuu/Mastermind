
import messages

def welcome():
    print(messages.welcome_introduction)
    while True: 
        svårighetsgrad = str(input("Vilken svårighetsgrad? "))
        #Ger oss input
        if svårighetsgrad.lower() in ["1","lätt","easy","l"]: #returnerar svårighetsgraden lätt, vilket är 1
            return 1
        elif svårighetsgrad.lower() in ["2","svår","hard","svårt","s"]: #returnerar svårighetsgraden svår, vilket är 2
            return 2
        elif svårighetsgrad.lower() in ["3","exempel","ex","hjälp","regler","rules","e"]: #Printar extra regler
            print(messages.welcome_extra_rules)
        else: #om input inte matchar med något alternativ
            print("Fel inmatning, försök igen. Skriv lätt eller svår för att starta ett spel")



            