# Mastermind
A mastermind game for a School Project
Vi har fått uppgifen att skapa ett program som fungerar som spelet Mastermind.


Hanna log:
generate file: 04.11.2025
Quick and easy, issues: git and reptitive numbers.

11.11.2025
I found some bugs in middle beaccuse function can modify global variables and i wasnt aware of that.
also solved the issue of making x and check when theres only meant to be a check.

13.11.2025
Finished the game. now it is fucntional but not perfect.
What has been fixed:
We fixed the puh (user input) but right now the comments are weird,
Moved around some lines in main to make it more readable such as
putting
memory_numbers.append(user_input)
memory_results.append(round_resuls)
beside each other.

2025.11.20
I made some useful functions that are good for general use today. Planning for the future. learnt about
 *arg - list format
 *kwarg  dicitonary
order:
    # regular parameters
    # *args
    # **kwargs
for future general good functions.

Changing puh to repeating_inputs, reason for name: because it repeats every time the user geusses
combined messages in repeating_inpputs such as sending all the outputs at the end.
made a message file (messages.py) to make the text filled files look cleaner.
moved the welcoome messages over there too

2025.12.02
Changed middle name to scanner beacuse the file snacs for correct and wrong positions


Kseniya log:
6.11.2025
Wrote code for welcome message in puh file.
Wrote input function where the player can write the numbers they are guessing.
Also wrote function that replaces all gaps in the input incase if the player writes gaps.
Begun writing functions for checking lenght of input.

11.11.2025
Added code for checking lenght of input from player in puh file.

13.11.2025
Fixed bugs in puh file with some help from Hanna. For example:
One problem the program has is that it would for some reason not accept some specific numbers when it accepted those numbers before.
Added while-loops. Wrote in better code for checking the amount of numbers the player inputted.
Added code for checking and making sure the player only wrote in integers and not variabels.
Should fix comments and the design of welcome message next time.

20.11.2025
Changed the design of welcome message and input message in puh file.


Gustaf log:
04.11.2025
Skapade welcome.py med instruktioner och regler. Där väljer man också svårighetsgraden. Jag såg till att fixa så att den accepterar olika svar.

06.11.2025
Designade output.py som innehåller formattering av utskrifterna. Jag hade problem med bredden på emojis där t.ex. högerjustering inte fungerade då avståndet angivet inte följdes. Jag löste det genoom att inte ha något efter en emoji på en rad. Alla emojis är alltså i slutet i en line.

18.11.2025
Kort lektion. Jag la till kommentarer till welcome.py

20.11.2025
Gjorde ett alternativ i welcome.py för att se längre regler och kortade ner tidigare regler.
Ändrade i kommentarer för output.py

27.11.2025
Implementerade Hannas funktion för att skriva ut tecknen i välkomsmeddelanden långsamt.
Todo: Det tar lång tid att skriva ut allt och vi orkar inte alltid vänta -> Skapa ett sätt att snabba upp texten

2.12.2025
Gjorde research om threading och skapade en trådning i Hannas sleep_write() som läser användarens input och skippar texten om denne skriver något.
Fixade lite kommentarer

Stuff i wanna work on include making messages a totally different function perhaps ex in repeating_numbers
To avoid
                         │Hej spelare!│🖑
         ☆ Du ska ange en gissning som följd av fyra siffror!
         ☆ Ange fyra siffror mellan och inklusive 1-6:
repeating every time. It's fun the first time after that its like hmmm

Improve next time:
- Some messages have to be edited (We can make it more aesthetic)
- in puh: I would prefer if it printed out all the issues at the end rather than only one comment directly and the breaking when it finds an issue
- change name of files or function names


      |                      | Snyggt🔥
  2   |   6    6    6    6   | ✅
      |                      | Snyggt🔥
  1   |   6    3    4    2   | ✅✅
      |                      | Snyggt🔥
-------------------------------------------
            |Hej Spelare!|

*Du ska ange en gissning som följd av fyra siffror!

*Ange fyra siffror mellan och inklusive 1-6: {user input}
Runda |    Testade koder     | Feedback :)
-------------------------------------------

advice: kesniya: \t makes a tab

Feedback from playtesting:
- Too many rules I dont wanna read. #actual issue if we wanna make the game fun...
-

Advice: Make an input function with right and wrong checking.
#useful_function

