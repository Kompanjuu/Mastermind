
#Idea is to make things cleaner by putting all of out messages in variables and storing them here


#for welcome
welcome_introduction ="""Välkommen till Mastermind!
Ett projekt av Hanna, Kseniya & Gustaf.

I Mastermind har du 12 omgångar att gissa en 4-siffrig kombination av siffrorna 1-6.
Du får feedback på hur många siffror som var på rätt plats med ✅ och på fel plats med ❎.
Till exempel om rätt kombination är 6253 och du gissar 1234 kommer du få svaret ✅❎.

Det finns 2 svårighetsgrader samt längre regler:
Lätt: Det förekommer inte några dubbletter.
Svår: Det kan förekomma dubbletta siffror
Exempel: JAG VILL HA BÄTTRE FÖRKLARADE REGLER"""

welcome_extra_rules = """-----------------------------------------------------------
Här kommer en längre förklaring av reglerna
Målet är att knäcka en fyrsiffrig kod innan 12 rundor är slut. Koden består av siffrorna 1-6.
Om du spelar på svårighetsgraden lätt så kan en siffra bara vara med 1 gång men på svår så kan den vara med flera gånger.

Varje gång du gör en gissning så berättar programmet för dig olika saker om din gissning.
Om en siffra är rätt OCH är på rätt plats så får du en ✅.
Om en siffra är rätt men INTE på rätt plats så får du en ❎.
Om en siffra är fel så får du inte något.
Programmet beräknar varje siffra, men du får sen inte reda på vilken siffra som gav ett svar.

Här kommer några exempel:
Om rätt kombination är 6253 och du gissar 1234 kommer du få svaret ✅❎. Här kommer svaret steg för steg.
Siffran 6 är fel så du får inget.
Siffran 2 är rätt och på rätt plats så du får ✅.
Siffran 5 är fel så du får inget.
Siffran 3 är rätt men på rätt plats så du får ❎.

Om rätt kombination är 1524 och du gissar 1234 får du✅✅❎
Siffran 1 är rätt och på rätt plats så du får ✅.
Siffran 2 är rätt men på rätt plats så du får ❎.
Siffran 3 är fel så du får inget.
Siffran 4 är rätt och på rätt plats så du får ✅.
Notera att programmet inte visar ✅❎✅

Det finns 2 svårighetsgrader samt längre regler(Det som precis visades):
Lätt: Det förekommer inte några dubbletter.
Svår: Det kan förekomma dubbletta siffror
Exempel: JAG VILL HA BÄTTRE FÖRKLARADE REGLER"""


#For puh
length_not_four = "Four numbers, no more no less"
not_integers = "Numbers, not any other character"
int_not_within_range = "The numbers should be between and including 1 to 6"

#for main
winning_message = """Congratulations you have won!
wow
encouragement"""
fail_message = "Dun dun better luck next time the combination was:"
goodbye_message = """Credits:
are you..
.
.
.
.
.
.
real?"""
