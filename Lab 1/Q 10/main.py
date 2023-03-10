print("Gimme a few words:")
inp = input()

word_list = inp.split()

word_list.sort()

print("The words in alphabetical order are:")

for i in word_list:
    print(i)