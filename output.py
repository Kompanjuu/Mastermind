def output(numbers, results):
    print(f"Runda |{"Testade koder": ^22}| Feedback :)")
    print(f"{"":-<43}")
    for i in range(11,-1,-1):
        if len(numbers)-1 < i:
            print(f"{(i+1): ^6}|{"": >22}|")
            print(f"{"": ^6}|{"": <22}|")
        else:
            print(f"{(i+1): ^6}| {numbers[i][0]: ^5}{numbers[i][1]: ^5}{numbers[i][2]: ^5}{numbers[i][3]: ^5} | {results[i]: <10}")
            if "✅" in results[i]:
                if len(results[i]) > 2:
                    print(f"{"": ^6}|{"": <22}| Fantastiskt❤️")
                else:
                    print(f"{"": ^6}|{"": <22}| Snyggt🔥")
            else:
                print(f"{"": ^6}|{"": <22}|")
    print(f"{"":-<43}")
list1 = [[1,2,3,4],[2,3,4,5],[3,4,5,6],[1,2,2,2]]
list2 = ["✅","","✅✅✅",""]
output(list1,list2)