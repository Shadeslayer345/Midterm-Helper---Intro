#Midterm practice answers

def question1():
	question="Question 1"
	print "Solution to "+question
	answer=str(3)+str(1)
	print "The expression str(3) + str(1) will yield " + answer
	print ""
	choice=raw_input ("Would you like to see the code for this solution? (y/n) )=========>" )
	print ""
	if choice=='y' or choice == 'Y' or choice == 'yes' or choice == 'Yes':
		print'def question1 ():'
		print'	question = "Question 1"'
		print'	print "Solution to " + question'
		print'	answer = str(3) + str(1)'
		print'	print "The expression str(3) + str(1) will yield " + answer'
	else:
		print"Remember the cake is a lie"

def question2():
	question="Question 2"
	print "Solution to "+question
	myVar=7>8
	answer=myVar
	print "The variable myVar will return a value of " + str(answer) + " which is a Boolean"
	print ""
	choice=raw_input ("Would you like to see the code for this solution? (y/n) )=========>" )
	print ""
	if choice == 'y' or choice == 'Y' or choice == 'yes' or choice == 'Yes':
		print'def question2 ():'
		print'	question = "Question 2"'
		print'	print "Solution to " + question'
		print'	myVar = 7 > 8'
		print'	answer = myVar'
		print'	print "The variable myVar will return a value of " + str(answer) + " which is a Boolean"'
	else:
		print"Remember the cake is a lie" 

def question3():
	question = "Question 3"
	print "Solution to " + question
	answer = 7/2
	print "In Python the expression 7/2 will yield " + str(answer)
	print ""
	choice = raw_input ("Would you like to see the code for this solution? (y/n) )=========>" )
	print ""
	if choice == 'y' or choice == 'Y' or choice == 'yes' or choice == 'Yes':
		print 'def question3 ():'
		print '	question = "Question 3"'
		print '	print "Solution to " + question'
		print '	answer = 7/2'
		print '	print "In Python the expression 7/2 will yield " + str(answer)'
	else:
		print "Remember the cake is a lie"

def question4():
	question = "Question 4"
	print "Solution to " + question
	def opTest():
		a = 7
		b = a + 6
		c = 2
		return a + b + c
	answer = opTest()
	print "The function opTest will result in an error "
	print "" 
	choice = raw_input ("Would you like to see the code for this solution in order to find the error? (y/n) )=========>" )
	print ""
	if choice == 'y' or choice == 'Y' or choice == 'yes' or choice == 'Yes':
		print 'def question4 ():'
		print '	question = "Question 4"'
		print '	print "Solution to " + question'
		print '	def opTest():'
		print '		a = 7'
		print '		b = a/c + 6'
		print '		c = 2'
		print '		return a + b + c'
		print '		answer = opTest()'
		print '	print "The function opTest will return a value of " + str(answer)'
	else:
		print "Remember the cake is a lie" 

def question5 ():
	question = "Question 5"
	print "Solution to " + question
	def doPrint ():
		print "Hello",
		return "World"
		print "Goodbye",
		return "World"
	answer = doPrint()
	print "The function doPrint will return a value of " + answer
	print "" 
	choice = raw_input ("Would you like to see the code for this solution in order to find the error? (y/n) )=========>" )
	print ""
	if choice == 'y' or choice == 'Y' or choice == 'yes' or choice == 'Yes':
		print 'def question5 ():'
		print '	question = "Question 5"'
		print '	print "Solution to " + question'
		print '	def doPrint ():'
		print'		print "Hello",'
		print'		return "World"'
		print'		print "Goodbye",'
		print'		return "World"'
	else:
		print "Remember the cake is a lie"
	
def question6 ():
	a = True
	counter = 0
	while (a):
		b = False
		a = b
		counter += 1
	answer = "The program will execute " + str(counter) + " time(s) because after the first execution of the loop, a has a value of " + str(a)
	print answer
	choice = raw_input ("Would you like to see the code for this solution in order to find the error? (y/n) )=========>" )
	print ""
	if choice == 'y' or choice == 'Y' or choice == 'yes' or choice == 'Yes':
		print 'def question6 ():'
		print '	a = True'
		print '	counter = 0'
		print '	while (a):'
		print '		b = False'
		print '		a = b'	
		print '		answer'
	else:
		print "Remember the cake is a lie" 

def question7():
	print "Code Reading"
	accumulator = ";"
	max = 9
	if max  + 4 > 10:
		print "Big Output Mode!"
	if max < 10:
		print "Max < 10"
	else:
		print "max = 0"
	#while (max > 0):
		#print max - 8
		#accumulator += str(max) + ";"
	print "The while loop will go on forever because the value of max does not decrease, it only appears to do so because of the print statement though the value is not assigned anywhere so it disappears!"
	print ""
	choice = raw_input ("Would you like to see the code for this solution in order to find the error? (y/n) )=========>" )
	print ""
	if choice == 'y' or choice == 'Y' or choice == 'yes' or choice == 'Yes':
		print 'def question7 ():'
		print '	"Code Reading"'
		print '	accumulator = ";"'
		print '	max = 9'
		print '	if max  + 4 > 10:'
		print '		print "Big Output Mode!"'
		print '	if max < 10'	
		print '		print "Max < 10"'
		print '	else:'
		print '		print "max = 0"'
		print '	while (max > 0):'
		print '		print max - 8'
		print '		accumulator += str(max) + ";"'
		print '	print accumulator'
	else:
		print "Remember the cake is a lie"

def question8 ():
	print "Writing Functions"
	def raisePower (base, exponent):
		if (base != 0) and (exponent >= 0):
			return base ** exponent
		else:
			return -1
	x = input ('Enter the value of the base =========> ')
	n = input ('Enter the value of the exponent =========> ')
	answer = raisePower(x,n)
	print str(x) + "raised to the " + str(n) + " yields " + str(answer)
	print ""

def question9 (): 
	print "Writing While Loops"
	origN = input ('Enter your favorite number! =========> ')
	modN = origN
	stringN = ""
	while (modN > 0):
		stringN += str(origN)
		modN -= 1
	
	print  "Surprise!! " + stringN
	print "Now arent you " + str(n) + " times happier?"
	print ""

def problemSolver (num):
		questions [num]()
		
		
def answerSheet (num, choice):
	if choice == 'y' or choice == 'Y' or choice == 'yes' or choice == 'Yes':
		problemSolver(num)
		print ""
		choice = raw_input ("Would you like to see another problem? (y/n) ========> " )	
		print ""
		if choice == 'y' or choice == 'Y' or choice == 'yes' or choice == 'Yes': 
			num = input ("Enter the problem number you would like to see =========> " )
			print ""
			answerSheet (num, choice)
		elif choice == 'n' or choice == 'N' or choice == 'no' or choice == 'No':
			print "Thanks for using ProblemSolver! The cake is a lie"
	else: 
		print "Have a Nice Day"	
		
		
		
questions = {
	1 : question1,
	2 : question2,
	3 : question3,
	4 : question4,
	5 : question5,
	6 : question6,
	7 : question7,
	8 : question8,
} 

problemNumber = input ("Enter the problem number you would like the solution to =========> " ) 
problemHelp = raw_input ("Do you wish to see the problem to solution " + str(problemNumber) + "? (y/n) =========> ") 
print ""
answerSheet(problemNumber, problemHelp)
