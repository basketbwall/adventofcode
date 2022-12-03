with open('input.txt') as f:
    lines = f.readlines()
    calorie = 0
    res = 0
    for line in lines:
        if line == "\n":
            print("this is a space")
            #update result
            res = max(res, calorie)
            #reset calorie
            calorie = 0
        else:
            #increment calorie
            calorie += int(line.strip())
    
    print(res)