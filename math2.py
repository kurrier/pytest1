#!/usr/bin/python
print "Python Calculator\n"

nonum = "Error: no number"
firstnum = "What is the first number?"
secnum = "What is the second number?"

def division(n1,n2):
	div = n1/n2
	print "%d divided by %d is: %d" % (n1, n2, div)
	return div

def multiply(n1,n2):
        mult = n1 * n2
        print "%d multiplied by %d is: %d" % (n1, n2, mult)
        return mult

def addition(n1,n2):
        add = n1 + n2
        print "%d added to %d is: %d" % (n1, n2, add)
        return add

def subtraction(n1,n2):
        subt = n1 - n2
        print "%d subtracted by %d is: %d" % (n1, n2, subt)
        return subt

num1 = raw_input(firstnum)
if len(num1) > 0 and num1.isdigit():
	num1 = int(num1)
else:
	print nonum
	exit()
num2 = raw_input(secnum)
if len(num2) > 0 and num2.isdigit():
	num2 = int(num2)
else:
	print nonum
	exit()

print("")
print "Addition (add), Division (div), Multipication? (mult)?, or Subtraction (sub): ",
ask = raw_input()
if ask == "add":
        addition(num1,num2)
elif ask == "div":
        division(num1,num2)
elif ask == "mult":
        multiply(num1,num2)
elif ask == "sub":
        subtraction(num1,num2)
else:
        print("Wrong choice!\n")
        exit()
print("")


