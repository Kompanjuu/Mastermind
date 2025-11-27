import welcome
import generate
import middle
import output
import repeating_input
import messages
import useful_functions

while True: #game will run unless said otherwise

    mode = welcome.welcome()
    #thiss will give rules and give us the mode
    combination_goal = generate.generate(mode)
    #print(combination_goal) ##CHECKING
    
    memory_numbers = []
    memory_results = []
    repeating_input.first_game_start_msg()
    
    for round in range(12):
        #print(combination_goal)
        
        user_input = repeating_input.game_start()

        round_result = middle.middle(user_input, combination_goal) 


        #this will return a list of the checkmarks like ['✅', '✅', '✅']
        #print("user_input:", user_input); print("combination_goal:", combination_goal)
        #GET RID OF THIS LATER

        #output() wants the check in the form of ['✅✅✅', ''] so i'm joining my round_result
        round_result = "".join(round_result)
        #output also want everything past round in one list too so lets make a "memory"


        memory_numbers.append(user_input) #this is put before middle because middle will modify the user_input, issue fixed so now its after message for clarity
        memory_results.append(round_result) 
        output.output(memory_numbers, memory_results)
        if round_result == "✅✅✅✅": #you have won early.
            print(messages.winning_message)
            break
    
    if round_result != "✅✅✅✅":
        #meaning you havent won after the for loops end
        combination_goal = "".join([str(x) for x in combination_goal])
        print(messages.fail_message, combination_goal)

    #make an exit ticket
    print("Vill du fortsätta spela? Ja/Nej")
    answer = input()
    answer = useful_functions.clean_string(answer)
    if answer != "ja":
        break
    
print(messages.goodbye_message)