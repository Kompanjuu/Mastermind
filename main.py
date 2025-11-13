import welcome
import generate
import middle
import output
import puh
while True: #game will run unless said otherwise

    mode = welcome.welcome()
    #thiss will give rules and give us the mode
    combination_goal = generate.generate(mode)
    #print(combination_goal) ##CHECKING
    
    memory_numbers = []
    memory_results = []
    for round in range(12):
        #print(combination_goal)
        
        user_input = puh.game_start()

        round_result = middle.middle(user_input, combination_goal) 


        #this will return a list of the checkmarks like ['✅', '✅', '✅']
        print("user_input:", user_input); print("combination_goal:", combination_goal)

        #output() wants the check in the form of ['✅✅✅', ''] so i'm joining my round_result
        round_result = "".join(round_result)
        #output also want everything past round in one list too so lets make a "memory"


        memory_numbers.append(user_input) #this is put before middle because middle will modify the user_input
        memory_results.append(round_result) 
        output.output(memory_numbers, memory_results)
        if round_result == "✅✅✅✅": #you have won early.
            print("gg fam")
            break
    
    if round_result != "✅✅✅✅":
        #meaning you havent won after the for loops end
        print(f"fail, the answer was {combination_goal}")

    #make an exit ticket
    print("Do you wanna keep on playing? Yes/No")
    answer = input()
    if answer.lower() != "yes":
        break

print("wahahaha")