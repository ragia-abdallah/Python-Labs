# flagX = True
# while flagX:
#     print("Enter x:")
#     x = int(input())
#     if isinstance(x, int):
#         flagX = False
#     else:
#         print("Wrong data type")
#
# flagY = True
# while flagY:
#     print("Enter y:")
#     y = input()
#     if isinstance(y, int):
#         flagY = False
#     else:
#         print("Wrong data type")

print("Enter x:")
x = int(input())
print("Enter y:")
y = int(input())

mySum = x + y
myDif = abs(x - y)
myProd = x * y
myQuot = 0
if x > y:
    myQuot = x % y
else:
    myQuot = y % x

print("Sum of X and Y is: ",mySum)
print("Difference of X and Y is: ",myDif)
print("Product of X and Y is: ",myProd)
print("Quotient of X and Y is: ",myQuot)