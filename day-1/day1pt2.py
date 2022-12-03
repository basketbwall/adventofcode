with open('input.txt') as f:
    lines = f.readlines()
    calorie = 0
    res = []
    for line in lines:
        if line == "\n":
            #update result
            res.append(calorie)
            #reset calorie
            calorie = 0
        else:
            #increment calorie
            calorie += int(line.strip())
    sorted = sorted(res)
    ans = 0
    for i in range(len(sorted)-1, len(sorted)-4, -1):
        ans += sorted[i]
    print(ans)