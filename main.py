import welcome
import generate
import middle
import output
while True: #game will run unless said otherwise

    mode = welcome.welcome()
    #thiss will give rules and give us the mode
    combination_goal = generate.generate(mode)
    print(combination_goal) ##CHECKING
    
    memory_numbers = []
    memory_results = []
    for round in range(12):
        print("message") #TEMP
        user_input = [int(i) for i in input().split()] #this is temoprary for what kseniya is making 
        memory_numbers.append(user_input) #this is put before middle because middle will modify the user_input

        round_result = middle.middle(user_input, combination_goal) 
        #this will return a list of the checkmarks like ['✅', '✅', '✅']
        print("user_input:", user_input)
        #preparation for output
        #output wants the check in the form of ['✅✅✅', ''] so i'm joining my round_result
        round_result = "".join(round_result)
        #output also want everything past round in one list too so lets make a "memory"
        
        memory_results.append(round_result)
        output.output(memory_numbers, memory_results)
        if round_result == "✅✅✅✅":
            print("gg fam")
            break
    if round_result != "✅✅✅✅":
        #meaning you havent won after the for loops end
        print(f"fail, the answer was {"".join(combination_goal)}")

    #make an exit ticket
    print("Do you wanna keep on playing? Yes for again, anything else will end")
    answer = input()
    if answer.lower() != "yes":
        break

print("wahahaha")