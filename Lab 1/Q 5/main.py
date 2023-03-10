def longest_string(strList):
    maxStr = ""
    for i in strList:
        if len(i) > len(maxStr):
            maxStr = i
    return maxStr

print("Enter a sentence:")
inp = input()

inpList = inp.split(" ")
print("The longest word is: ",longest_string(inpList))
