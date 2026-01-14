# Write a Python program that does the following:
#1. Takes 2 numbers as input from the users.
#2. Performs basic mathematical operations : +, - , * , /

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
add=a+b
sub=a-b
mul=a*b
div=a/b
print('Addition:',add)
print('Subtraction:',sub)
print('Multiplication:',mul)
print('Division:',round(div,1))