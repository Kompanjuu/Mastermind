# Mastermind
A mastermind game for a School Project

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

Kseniya log:
6.11.2025
Wrote code for welcome message in puh file.
Wrote input function where the player can write the numbers they are guessing.
Also wrote function that replaces all gaps in the input incase if the player writes gaps.
Begun writing functions for checking lenght of input.

11.11.2025
Added code for checking lenght of input from player in puh file.

13.11.2025
Fixed bugs in puh file with some help from Hanna.
Added while-loops. Wrote in better code for checking the amount of numbers the player inputted.
Added code for checking and making sure the player only wrote in integers and not variabels.
Should fix comments and the design of welcome message next time.

20.11.2025
Changed the design of welcome message and input message in puh file.

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
