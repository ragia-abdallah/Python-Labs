print("How many numbers do you have?")
n = int(input())

inp = []
for i in range(n):
    print("Gimme a number:")
    x = float(input())
    inp.append(x)

def get_max_number(numbersList):
    maxNum = numbersList[0]
    for i in numbersList:
        if i > maxNum:
            maxNum = i
    return maxNum

print("The maximum number was: ",get_max_number(inp))