#!/usr/bin/python

nonum = "Error: no number"
firstnum = "What is the first number?"
secnum = "What is the second number?"

print "Starting Math Problem\n"

def division():
	global nonum
	print "Division Problem:\n"
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
	print("The Question is: %s / %s\n") % (num1, num2)
	div = num1 / num2
	print "The Answer is:"
	print div
	print('')

def multiply():
        global nonum
        print "Multiplication Problem\n"
        num1 = raw_input(firstnum)
        if len(num1) > 0 and num1.isdigit():
                num1 = int(num1)
        else:
                print('nonum\n')
                exit()
        num2 = raw_input(secnum)
        if len(num2) > 0 and num2.isdigit():
                num2 = int(num2)
        else:
                print nonum
                exit()
        print("The Question is: %s / %s\n") % (num1, num2)
        mult = num1 * num2
        print "The Answer is:"
        print mult
        print('')

print "Division (div) or Multipication? (mult)?: ",
ask = raw_input()
if ask == "div":
        division()
elif ask == "mult":
        multiply()
else:
        print("Wrong choice!\n")
        exit()

