def welcome():
    print("""Välkommen till Mastermind!
Ett projekt av Hanna, Kseniya & Gustaf.

Mastermind är ett spel där du har 12 omgångar att gissa en 4-siffrig kombination av siffrorna 1-6.
Efter varje gissning får du reda på hur många av siffrorna var på rätt ställe med ✅, samt hur många siffror som är rätt men på fel ställe med ❎
Till exempel om rätt kombination är 6253 och du gissar 1234 kommer du få svaret ✅❎
Du får ✅ då 2:an är på rätt plats.
Du får ❎ då 3:an finns men är på fel plats.

Det finns 2 svårighetsgrader:
Lätt: Det förekommer inte några dubbletter.
Svår: Det kan förekomma dubbletta siffror""")
    while True: 
        svårighetsgrad = str(input("Vilken svårighetsgrad? "))
        #Ger oss input
        if svårighetsgrad.lower() in ["1","lätt","easy"]: #Checkar att det är giltig input och returnar den
            return 1
        elif svårighetsgrad.lower() in ["2","svår","hard"]:
            return 2
        else:
            print("Fel inmatning, försök igen")