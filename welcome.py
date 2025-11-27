import useful_functions
import messages

def welcome():
    useful_functions.sleep_write(messages.welcome_introduction)
    while True: 
        svårighetsgrad = useful_functions.clean_string(str(input("Ange vad du vill göra: Lätt (1), Svår (2) eller Hjälp (3) ")))
        #Ger oss input
        if svårighetsgrad in ["1","lätt","easy","l"]: #returnerar svårighetsgraden lätt, vilket är 1
            return 1
        elif svårighetsgrad in ["2","svår","hard","svårt","s"]: #returnerar svårighetsgraden svår, vilket är 2
            return 2
        elif svårighetsgrad in ["3","exempel","ex","hjälp","regler","rules","e"]: #Printar extra regler
            useful_functions.sleep_write(messages.welcome_extra_rules)
        else: #om input inte matchar med något alternativ
            print("Fel inmatning, försök igen. Skriv lätt eller svår för att starta ett spel")

            