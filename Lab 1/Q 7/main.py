def vowels_counter(str):
    vowels = ['a','e','i','o','u']
    counter = 0
    for i in str:
        if i.lower() in vowels:
            counter +=1
    return counter


print("Enter a sentence:")
inp = input()
print("The sentence contains ", vowels_counter(inp), " vowel(s).")

