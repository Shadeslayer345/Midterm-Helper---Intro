from Tkinter import *
import os
import time
import tkMessageBox
import sys
''' This is the backbone code for the GUI that is executed when the corresponding button is pressed '''
''' This is the corresponding code for question 1 '''
def question1():
	question="Question 1"
	q1l1=Label(frmMain,text="Solution to "+question)
	answer="The expression str(3) + str(1) will yield " +str(3)+str(1)
	q1l1.pack()
	listbox.pack()
	line1=''
	line2='def question1 ():'
	line3='  question = "Question 1" '
	line4='  print "Solution to " + question'
	line5='  answer = str(3) + str(1)'
	line6='  print "The expression str(3) + str(1) will yield " + answer'
	line7='  Remember, the cake is a lie'
	lines=[line1,line2,line3,line4,line5,line6]
	listbox.insert(END,answer)
	if (tkMessageBox.askyesno("Decision Time!","Would you like to see the code used to achieve this answer?")==YES):
		
		n=len(lines)
		count=0
		while n>0:
			listbox.insert(END,lines[count])
			n-=1
			count+=1
	else:	
		listbox.insert(END,line7)
	if (tkMessageBox.askokcancel("Bleeop","Click OK when you're done!")==True):
		listbox.delete(0,END)
		listbox.forget()
		q1l1.forget()
''' This is the corresponding code for question 2 '''
def question2():
	question="Question 2"
	q2l1=Label(frmMain,text="Solution to "+question)
	myVar=7>8
	answer="The variable myVar will return a value of "+str(myVar)+" which is a Boolean"
	q2l1.pack()
	listbox.pack()
	listbox.insert(END, answer)
	line1=''
	line2='def question2 ():'
	line3='   question = "Question 2"'
	line4='   print "Solution to " + question'
	line5='   myVar = 7 > 8'
	line6='   answer = myVar'
	line7='   print "The variable myVar will return a value of " + str(myVar) + " which is a Boolean"'
	line8='"Remember, the cake is a lie"'
	lines=[line1,line2,line3,line4,line5,line6,line7]
	if (tkMessageBox.askyesno("Decision Time!","Would you like to see the code used to achieve this answer?")==YES):
		n=len(lines)
		count=0
		while n>0:
			listbox.insert(END,lines[count])
			n-=1
			count+=1
	else:	
		listbox.insert(END,line8)
	if (tkMessageBox.askokcancel("Time!!!","Click OK when you're done!")==True):
			listbox.delete(0,END)
			listbox.pack_forget()
			q2l1.pack_forget()
''' This is the corresponding code for question 3 '''
def question3():
	question="Question 3"
	q3l1=Label(frmMain,text="Solution to "+question)
	answer="In Python the expression 7/2 will yield "+str(7/2)
	q3l1.pack()
	listbox.insert(END, answer)
	listbox.pack()
	line1=''
	line2='def question3 ():'
	line3='   question = "Question 3"'
	line4='   print "Solution to " + question'
	line5='   answer = 7/2'
	line6='   print "In Python the expression 7/2 will yield " + str(answer)'
	line7='"Remember, the cake is a lie"'
	lines=[line1, line2, line3, line4, line5,line6]
	if (tkMessageBox.askyesno("Decision Time!","Would you like to see the code used to achieve this answer?")==YES):
		n=len(lines)
		count=0
		while n>0:
			listbox.insert(END, lines[count])
			n-=1
			count+=1
	else:
		listbox.insert(END,line7)
	if (tkMessageBox.askokcancel("Time!!!", "Click OK when you're done!")==True):
			listbox.delete(0,END)
			listbox.pack_forget()
			q3l1.pack_forget()
''' This is the corresponding code for question 4 '''
def question4():
	question="Question 4"
	q4l1=Label(frmMain, text = "Solution to " + question)
	def opTest():
		a=7
		b=a+6
		c=2
		return a+b+c
	answer="The function opTest will result in an error "
	q4l1.pack()
	listbox.insert(END,answer)
	listbox.pack()
	line1=''
	line2='def question4 ():'
	line3='  question = "Question 4"'
	line4='  print "Solution to " + question'
	line5='  def opTest():'
	line6='      a = 7'
	line7='      b = a/c + 6'
	line8='      c = 2'
	line9='      return a + b + c'
	line10='      answer = opTest()'
	line11=' print "The function opTest will return a value of " + str(answer)'
	line12='"Remember, cake is a lie"'
	lines=[line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11]
	if (tkMessageBox.askyesno("Decision Time!", "Would you like to see the code in order to find the error?") == YES ):
		n=len(lines)
		count=0
		while n>0:
			listbox.insert(END, lines[count])
			n-=1
			count+=1
	else:
		listbox.insert(END,line12)
	if (tkMessageBox.askokcancel("Time!!!","Click OK when you're done!")==True):
			listbox.delete(0,END)
			listbox.pack_forget()
			q4l1.pack_forget()
''' This is the corresponding code for question 5 '''
def question5():
	question="Question 5"
	q5l1=Label(frmMain,text="Solution to "+question)
	def doPrint ():
		print "Hello",
		return "World"
		print "Goodbye",
		return "World"
	answer="The function doPrint will return a value of "+doPrint()
	q5l1.pack()
	listbox.insert(END,answer)
	listbox.pack()
	line1=''
	line2='def question5 ():'
	line3='   question = "Question 5"'
	line4='   print "Solution to " + question'
	line5='	def doPrint ():'
	line6='       print "Hello",'
	line7='       return "World"'
	line8='       print "Goodbye",'
	line9='       return "World"'
	line10='Remember, the cake is a lie'
	lines=[line1,line2,line3,line4,line5,line6,line7,line8,line9]
	if (tkMessageBox.askyesno("Decision Time!", "Would you like to see the code used to achieve this answer?")==YES):
		n=len(lines)
		count=0
		while n>0:
			listbox.insert(END, lines[count])
			n-=1
			count+=1
	else:
		listbox.insert(END, line10)
	if (tkMessageBox.askokcancel("Time!!!","Click OK when you're done!")==True):
			listbox.delete(0,END)
			listbox.pack_forget()
			q5l1.pack_forget()
''' This is the corresponding code for question 6 '''
def question6():
	question="Question 6"
	q6l1=Label(frmMain,text="Solution to Problem"+question)
	a=True
	counter=0
	while (a):
		b=False
		a=b
		counter+=1
	answer="The program will execute "+str(counter)+" time(s) because after the first execution of the loop, [a] has a value of "+str(a)
	q6l1.pack()
	listbox.pack()
	listbox.insert(END,answer)
	line1=''
	line2='def question6 ():'
	line3=' a = True'
	line4=' counter = 0'
	line5=' while (a):'
	line6='     b = False'
	line7='     a = b'	
	line8='     answer'
	line9='Remember, the cake is a lie' 
	lines=[line1,line2,line3,line4,line5,line6,line7,line8]
	if (tkMessageBox.askyesno("Decision Time!", "Would you like to see the code used to achieve this answer?")==YES):
		n=len(lines)
		count=0
		while n>0:
			listbox.insert(END, lines[count])
			n-=1
			count+=1
	else:
		listbox.insert(END, line9)
	if (tkMessageBox.askokcancel("Time!!!","Click OK when you're done!")==True):
			listbox.delete(0,END)
			listbox.pack_forget()
			q6l1.pack_forget()
''' This is the corresponding code for question 7 '''
def question7():
	question="Question 7"
	q7l1=Label(frmMain,text=question+" - Code Reading")
	accumulator=";"
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
	answer="The while loop will go on forever because the value of max does not decrease, it only appears to do so(decrease) because of the print statement though the value is not assigned anywhere so it disappears!"
	q7l1.pack()
	listbox.insert(END,answer)
	listbox.pack()
	line1=''
	line2='def question7 ():'
	line3=' print "Code Reading"'
	line4=' accumulator = ";"'
	line5=' max = 9'
	line6=' if max  + 4 > 10:'
	line7='     print "Big Output Mode!"'
	line8=' if max < 10'	
	line9='     print "Max < 10"'
	line10='    else:'
	line11='    print "max = 0"'
	line12=' while (max > 0):'
	line13='    print max - 8'
	line14='    accumulator += str(max) + ";"'
	line15=' print accumulator'
	line16="Remember, the cake is a lie"
	lines=[line1,line2,line3,line4,line5,line6,line7,line7,line8,line9,line10,line11,line12,line13,line14,line15]
	if (tkMessageBox.askyesno("Decision Time!", "Would you like to see the code in order to find the error?")==YES):
		n=len(lines)
		count=0
		while n>0:
			listbox.insert(END, lines[count])
			n-=1
			count+=1
	else:
		listbox.insert(END, line16)
	if (tkMessageBox.askokcancel("Time!!!","Click OK when you're done!")==True):
			listbox.delete(0,END)
			listbox.pack_forget()
			q7l1.pack_forget()
''' This is the corresponding code for question 8 '''
def question8():
	def raisePower():
		entryFrame.pack_forget()
		entry1.pack_forget()
		baseEntry.pack_forget()
		entry2.pack_forget()
		exponentEntry.pack_forget()
		solve.pack_forget()
		x=int(baseEntry.get())
		n=int(exponentEntry.get())
		line1=''
		line2='def raisePower (base, exponent):'
		line3='   if (base != 0) and (exponent >= 0):'
		line4='       return base ** exponent'
		line5='   else:'
		line6='       return -1'
		line7='x = input ("Enter the value of the base =========> ")'
		line8='n = input ("Enter the value of the exponent =========> ")'
		line9='answer = raisePower(x,n)'
		line10='print str(x) + "raised to the " + str(n) + " yields " + str(answer)'
		line11="Remember, the cake is a lie"
		lines=[line1,line2,line3,line4,line5,line6,line7,line8,line9,line10]
		if (x!=0) and (n>=0):
			value=x**n
			answer=str(x)+" raised to the power of "+str(n)+" yields "+str(value)
			listbox.insert(END,answer)
			listbox.pack()
		if (tkMessageBox.askyesno("Decision Time!", "Would you like to see the code used to achieve this answer?")==YES):
			n=len(lines)
			count=0
			while n>0:
				listbox.insert(END, lines[count])
				n-=1
				count+=1
		else:
			listbox.insert(END, line11)
		if (tkMessageBox.askokcancel("Time!!!","Click OK when you're done!")==True):
			listbox.delete(0,END)
			listbox.pack_forget()
			q8l1.pack_forget()
			
		else:
			return -1
	question="Question 8"
	q8l1=Label(frmMain,text=question+" - Writing Functions")
	entry1=Label(entryFrame,text="Enter the value for the Base here")
	entry2=Label(entryFrame,text="Enter the value for the exponent here")
	baseEntry=Entry(entryFrame)
	exponentEntry=Entry(entryFrame)
	solve=Button(frmMain,text="Submit",command=raisePower)
	q8l1.pack()
	entryFrame.pack()
	entry1.pack()
	baseEntry.pack()
	entry2.pack()
	exponentEntry.pack()
	solve.pack()
''' This is the corresponding code for question 9 '''
def question9(): 
	def numPrint():
		entryFrame.pack_forget()
		entry1.pack_forget()
		numEntry.pack_forget()
		solve.pack_forget()
		line1=''
		line2='def question9():'
		line3=' origN = input ("Enter your favorite number! =========> ")'
		line4=' modN = origN'
		line5=' stringN = ""'
		line6=' while (modN > 0):'
		line7='     stringN += str(origN)'
		line8='     modN -= 1'
		line9=' print  "Surprise!! " + stringN'
		line10=' print "Now arent you " + str(n) + " times happier?"'
		line11='Remember the cake is a lie'
		lines=[line1,line2,line3,line4,line5,line6,line7,line8,line9,line10]
		origN=int(numEntry.get())
		modN=origN
		stringN=""
		while(modN>0):
			stringN+=str(origN)
			modN-=1
		surprise="Surprise!! "+stringN
		message="Now aren't you "+str(origN)+" times happier?"
		listbox.insert(END,surprise)
		listbox.insert(END,message)
		listbox.pack()
		if (tkMessageBox.askyesno("Decision Time!", "Would you like to see the code used to achieve this answer?")==YES):
			n=len(lines)
			count=0
			while n>0:
				listbox.insert(END, lines[count])
				n-=1
				count+=1
		else:
			listbox.insert(END, line11)
		if (tkMessageBox.askokcancel("Time!!!","Click OK when you're done!")==True):
			listbox.delete(0,END)
			listbox.pack_forget()
			q9l1.pack_forget()
	question="Question 9"
	q9l1=Label(frmMain,text=question+" - Writing While Loops")
	entry1=Label(entryFrame,text="Enter your favorite number here")
	numEntry=Entry(entryFrame)
	solve=Button(frmMain,text="Submit",command=numPrint)
	q9l1.pack()
	entryFrame.pack()
	entry1.pack()
	numEntry.pack()
	solve.pack()
''' This code executes a separate file that allows the terminal to run instead of the GUI Application '''			
def terminal():
    os.startfile('midterm practice.py')
''' This creates the Main GUI for the Application'''
frmMain = Tk()
frmMain.minsize(1000,450)
frmMain.maxsize(1400,850)
''' This creates the ListBox Widgets for listing outputs'''
listbox = Listbox(frmMain)
listbox.config(height=20)
listbox.config(width=168)
''' This creates the Entry Widget for Problems 8 & 9 '''
entryFrame=Frame(frmMain)
''' This is where the interactive elements of the program are instantiated '''
label=Label(frmMain, text="Midterm Solver 1.0!")
Intro=Label(frmMain, text="My Name is JaPyC# and I'm here to help you")
question=Label(frmMain, text="Would you like to receive my help?")
Or=Label(frmMain, text="OR")
space=Label(frmMain, text="")
bterm=Button(frmMain, text="Click Here to enter the terminal",command=terminal)
b1=Button(frmMain,text="Click Here to view GUI for Problem 1",command=question1)
b2=Button(frmMain,text="Click Here to view GUI for Problem 2",command=question2)
b3=Button(frmMain,text="Click Here to view GUI for Problem 3",command=question3)
b4=Button(frmMain,text="Click Here to view GUI for Problem 4",command=question4)
b5=Button(frmMain,text="Click Here to view GUI for Problem 5",command=question5)
b6=Button(frmMain,text="Click Here to view GUI for Problem 6",command=question6)
b6=Button(frmMain,text="Click Here to view GUI for Problem 6",command=question6)
b7=Button(frmMain,text="Click Here to view GUI for Problem 7",command=question7)
b8=Button(frmMain,text="Click Here to view GUI for Problem 8",command=question8)
b9=Button(frmMain,text="Click Here to view GUI for Problem 9",command=question9)
'''		This is where the GUI Application becomes interactive	'''
label.pack()
Intro.pack()
bterm.pack(pady=5)
Or.pack(pady=5)
b1.pack(pady=5)
b2.pack(pady=5)
b3.pack(pady=5)
b4.pack(pady=5)
b5.pack(pady=5)
b6.pack(pady=5)
b7.pack(pady=5)
b8.pack(pady=5)
b9.pack(pady=5)
''' This is where the program ends '''
frmMain.mainloop()
