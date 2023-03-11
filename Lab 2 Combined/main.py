#Q1
print("1 - Write a Python program that uses the math module to calculate\
 the area of a circle with a radius of 5.")

import math

rad = 5
area = round(math.pi * math.pow(rad, 2),2)

print(f'The area of a circle with the radius {rad}m is: {area}m2')




#Q2
print("\n2 - Create a custom Python module called my_module with a function that takes a string \
as input and returns the reverse of the string. Then write a Python program that imports the my_module \
module and uses the reverse_string function to reverse the string 'Hello, world!'.")

import my_module as mod

str = "Hello, World!"

new_str = mod.string_reverse(str)

print(new_str)




#Q3
print("\n3- Write a Python program that imports only the randint function from the random module \
and uses it to generate a random integer between 1 and 10.")

from random import randint

random_number = randint(1, 10)

print(random_number)




#Q4
print("\n4 - Write a Python program that imports the datetime module with the alias dt and uses \
the now function to get the current date and time.")

import datetime as dt

now = dt.datetime.now()

print(f'The current date and time is {now.strftime("%c")}')




#Q5
print("\n5- Write a Python program that reads a file named example.txt and counts the number \
of lines in the file.")

print("method 1")
with open("example.txt","r") as file:
    f = file.read()
    f_split = f.split("\n")
    lines = len(f_split)
    print(f'This file has {lines} line(s).')

print("method 2")
with open("example.txt","r") as file:

    counter = sum(1 for line in file)
    print(f'This file has {counter} line(s).')




#Q6
print("\n6 - Write a Python program that reads a file named example.txt and prints the contents \
of the file in reverse order.")

with open("example.txt","r") as file:
    content = file.read()
    listed = content.split("\n")
    listed.reverse()
    for i in listed:
        print(i)




#Q7
print("\n7 - Write a Python program that reads a file named example.txt and removes \
all newline characters from the file.")

with open("example.txt","r") as file:
    f = file.read()
    f_str = f.replace("\n"," ")
    print(f_str)



#Q8
print("\n8 - Write a Python program that reads a file named example.txt and writes its contents \
to a new file named copy.txt.")

f = ""
with open("example.txt","r") as file:
    f = file.read()

# with open("copy.txt","x") as file: >> this will give error if run multiple times
with open("copy.txt", "w") as file: # used w mode to avoid error
    file.write(f)




#Q9
print("\n9 - Write a Python program that reads a file named example.txt and prints \
the longest word in the file.")

with open("example.txt","r") as file:
    f = file.read()
    words = f.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    print(f'The longest word is "{longest}".')





#Q10
print("\n10 - Write a function that takes a list of integers as input and returns \
the sum of all even numbers in the list.")


def sum_of_even(*args):
    sum = 0
    for i in args:
        if i % 2 == 0:
            sum += i
    return sum


tup = (1,5,3,6,2,8)
print(f'Numbers entered are: {tup}')
sum = sum_of_even(1,5,3,6,2,8)
print(f'The sum of even numbers is: {sum}')




#Q11
print("\n11 - Write a function that takes a list of strings as input and returns \
a new list containing only the strings that start with the letter 'a'.")

def a_words(wordlist):
    a_list = []
    for i in wordlist:
        if i.startswith("a") or i.startswith("A"):
            a_list.append(i)
    return a_list


my_list = ["ragia", "abdallah", "Ahmed", "hazem", "Awam"]

my_new_list = a_words(my_list)

print(my_new_list)




#Q12
print("\n12 - Write a function that takes a dictionary as input and returns a \
new dictionary with the keys and values swapped (i.e., the keys \
become the values and the values become the keys).")

