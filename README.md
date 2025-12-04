# Mastermind
For a School Project.\
Mastermind är ett spel som liknar det populära spelet Wordle. Man ska gissa en kombination av fyra siffror mellan 1 och 6. Sedan så får man feedback på om man hade rätt eller inte med sina siffror. Till skillnad från Wordle så får man inte reda på vilken eller vilka siffror som var rätt. Du måste alltså både hitta vilken siffra som är rätt och sedan lista ut vilken av siffrorna du skrev var på rätt plats.

# How to run
Make a clone of the repository. Start the program by running main.py with python3.

# Example Run
```
         ☆ Ange fyra siffror mellan och inklusive 1-6: 3142
Runda |    Testade koder     | Feedback :)
-------------------------------------------
  12  |                      |
      |                      |
  11  |                      |
      |                      |
  10  |                      |
      |                      |
  9   |                      |
      |                      |
  8   |                      |
      |                      |
  7   |                      |
      |                      |
  6   |                      |
      |                      |
  5   |                      |
      |                      |
  4   |   3    1    4    2   | ✅❎❎❎      
      |                      | Fantastiskt❤️
  3   |   2    3    1    4   | ❎❎❎❎      
      |                      |
  2   |   2    3    4    1   | ✅❎❎❎      
      |                      | Fantastiskt❤️
  1   |   1    2    3    4   | ❎❎❎❎      
      |                      |
-------------------------------------------
         ☆ Ange fyra siffror mellan och inklusive 1-6: 3421
Runda |    Testade koder     | Feedback :)
-------------------------------------------
  12  |                      |
      |                      |
  11  |                      |
      |                      |
  10  |                      |
      |                      |
  9   |                      |
      |                      |
  8   |                      |
      |                      |
  7   |                      |
      |                      |
  6   |                      |
      |                      |
  5   |   3    4    2    1   | ✅✅✅✅      
      |                      | Fantastiskt❤️
  4   |   3    1    4    2   | ✅❎❎❎      
      |                      | Fantastiskt❤️
  3   |   2    3    1    4   | ❎❎❎❎      
      |                      |
  2   |   2    3    4    1   | ✅❎❎❎      
      |                      | Fantastiskt❤️
  1   |   1    2    3    4   | ❎❎❎❎      
      |                      |
-------------------------------------------
Grattis, du vann!
🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
Vill du fortsätta spela? Ja (1), Nej (2)
```
# Logs
Hanna log:\
generate file: 04.11.2025\
Quick and easy, issues: git and reptitive numbers.

11.11.2025\
I found some bugs in middle beaccuse function can modify global variables and i wasnt aware of that.\
also solved the issue of making x and check when theres only meant to be a check.

13.11.2025\
Finished the game. now it is fucntional but not perfect.\
What has been fixed:\
We fixed the puh (user input) but right now the comments are weird,\
Moved around some lines in main to make it more readable such as\
putting\
memory_numbers.append(user_input)\
memory_results.append(round_resuls)\
beside each other.

2025.11.20\
I made some useful functions that are good for general use today. Planning for the future. learnt about\
 *arg - list format\
 *kwarg  dicitonary\
order:\
    # regular parameters\
    # *args\
    # **kwargs\
for future general good functions.

Changing puh to repeating_inputs, reason for name: because it repeats every time the user geusses\
combined messages in repeating_inpputs such as sending all the outputs at the end.\
made a message file (messages.py) to make the text filled files look cleaner.\
moved the welcoome messages over there too

2025.12.02\
Changed middle name to scanner beacuse the file snacs for correct and wrong positions

Kseniya log:\
6.11.2025\
Wrote code for welcome message in puh file.\
Wrote input function where the player can write the numbers they are guessing.\
Also wrote function that replaces all gaps in the input incase if the player writes gaps.\
Begun writing functions for checking lenght of input.

11.11.2025\
Added code for checking lenght of input from player in puh file.

13.11.2025\
Fixed bugs in puh file with some help from Hanna. For example:\
One problem the program has is that it would for some reason not accept some specific numbers when it accepted those numbers before.\
Added while-loops. Wrote in better code for checking the amount of numbers the player inputted.\
Added code for checking and making sure the player only wrote in integers and not variabels.\
Should fix comments and the design of welcome message next time.

20.11.2025\
Changed the design of welcome message and input message in puh file.

Gustaf log:\
04.11.2025\
Skapade welcome.py med instruktioner och regler. Där väljer man också svårighetsgraden. Jag såg till att fixa så att den accepterar olika svar.

06.11.2025\
Designade output.py som innehåller formattering av utskrifterna. Jag hade problem med bredden på emojis där t.ex. högerjustering inte fungerade då avståndet angivet inte följdes. Jag löste det genoom att inte ha något efter en emoji på en rad. Alla emojis är alltså i slutet i en line.

18.11.2025\
Kort lektion. Jag la till kommentarer till welcome.py

20.11.2025\
Gjorde ett alternativ i welcome.py för att se längre regler och kortade ner tidigare regler.\
Ändrade i kommentarer för output.py


27.11.2025\
Implementerade Hannas funktion för att skriva ut tecknen i välkomsmeddelanden långsamt.\
Todo: Det tar lång tid att skriva ut allt och vi orkar inte alltid vänta -> Skapa ett sätt att snabba upp texten


2.12.2025\
Gjorde research om threading och skapade en trådning i Hannas sleep_write() som läser användarens input och skippar texten om denne skriver något.\
Fixade lite kommentarer

04.12.2025\
Skrev i README och fixade lite buggar. En bugg som ej är löst är att man måste trycka enter 2ggr om man ej skippar texten.
