print "Hello World!"

course = "CIS 122"
name = "Intro to Software Design"
print "Welcome to "+course+": "+name

a = 1.1
b = 3
c = a + b
print "The sum of %s and %s is %s" % (a,b,c)

x_print("Hello World!")

language = "Python"
adjective = "Fun"
x_print("Learning", language, "is", adjective)

pizzas = 10
slices_per_pizza = 8
total_slices = pizzas * slices_per_pizza
x_print("There are", total_slices, "slices in", pizzas, "pizzas.")
x_print(total_slices, ": It must be dinner time!",sep="")

'''
Description:

In this challenge, we'll be learning about the pseudocode Display command, and how to translate it to Python.
The pseudocode standard used in this challenge is based on the book Starting Out with Programming Logic and
Design, 3rd Edition by Tony Gaddis. If you want to test code that uses x_print (described below) in Python 3
outside of the CodeWars site, add this line to the top of the code:

x_print = print
Python 2.7 and Codewars

First, it's important to note that the Codewars site uses Python 2.7, which is an older version. One of the
important differences between Python 2.7 and Python 3.4 is that the print statement is different.

In Python 2.7, print is called like this:

#  Display "Hello World!"
print "Hello World!"
The print statement takes a single String argument. If you want to print multiple values, you need to either
use multiple print statements (one per each line of output), or you need to create a single String from the
values you want to print and print that single String (you can use the String concatenation operator + to do that). For example:

#  Declare String student_name = "Fred"
#  Declare String course_name = "Software Design"
#
#  Display "Hello", student_name, ", welcome to", course_name, "!"

student_name = "Fred"
course_name = "Software Design"

print "Hello " + student_name + ", wecome to " + course_name + "!"
The output from running this program will be:

Hello Fred, wecome to Software Design!
Note the use of spaces inside the strings "Hello " and ", welcome to " so that the resulting line is formatted
correctly.

Converting the output to a single String becomes a little more complicated when you want to print numbers,
because the following code produces an error:

#  Declare String assignment = "Exam 1"
#  Declare Real score = 85.5
#
#  Display "Your grade on", assignment, "was", score

assignment = "Exam 1"
score = 85.5

print "Your grade on " + assignment + " was " + score
The text of the error is:

TypeError: cannot concatenate 'str' and 'float' objects
The reason for the error is that only Strings can be concatenated with other Strings, and Reals
(floats in Python) are not Strings. The value of score is the Real number 85.5, not the String "85.5". To fix
that, we need to convert the Real to a String ourselves, using the str function in Python:

#  Declare String assignment = "Exam 1"
#  Declare Real score = 85.5
#
#  Display "Your grade on", assignment, "was", score

assignment = "Exam 1"
score = 85.5

print "Your grade on " + assignment + " was " + str(score)
Note that we don't need to put the call to str in our pseudocode, that's just a detail of our Python
implementation.

This version of the program should produce the following output in Python 2.7:

Your grade on Exam 1 was 85.5
Python 3

In Python 3, print is called like this:

#  Display "Hello World!"
print("Hello World!")
The print statement takes multiple arguments within the (...). If you want to print multiple values,
you can include them all in a single print statement, separated by commas like print(a, b, c, ..., n). For example:

#  Declare String student_name = "Fred"
#  Declare String course_name = "Software Design"
#
#  Display "Hello", student_name, ", welcome to", course_name, "!"

student_name = "Fred"
course_name = "Software Design"

print("Hello", student_name, ", wecome to" + course_name + "!")
The output from running this program will be:

Hello Fred , wecome to Software Design !
Note that Python prints each argument in order, separated by a single space (" "). You can control what
text the print command uses to separate values by supplying a sep argument, like this:

#  Declare String student_name = "Fred"
#  Declare String course_name = "Software Design"
#
#  Display "Hello", student_name, ", welcome to", course_name, "!"

student_name = "Fred"
course_name = "Software Design"

print("Hello ", student_name, ", wecome to " + course_name + "!", sep="")
The output from running this program will be:

Hello Fred, wecome to Software Design!
With Python 3 print, each argument is automatically converted to a String, so there's no need to use
the str function. This code should work properly:

#  Declare String assignment = "Exam 1"
#  Declare Real score = 85.5
#
#  Display "Your grade on", assignment, "was", score

assignment = "Exam 1"
score = 85.5

print("Your grade on", assignment, "was", score)
This version of the program should produce the following output in Python 3:

Your grade on Exam 1 was 85.5
When you print text, each print statement will add one line of output to the display by default.
It does this by automatically adding a linefeed character to the end of the output (in Python, the linefeed character is represented as "\n"). You can change this behavior by specifying a different value for the end argument like this:

print("Hello", end=" ")
print("World!")
Since the end-of-line string has been changed to a single space in the first print statement,
the output displays as:

Hello World!
x_print

Since print on Codewars is the Python 2.7 version of print, but we want to get practice with the
Python 3 version, I have included a command called x_print. It works the same way as the print command
works in Python 3. Use it like this:

#  Declare String assignment = "Exam 1"
#  Declare Real score = 85.5
#
#  Display "Your grade on", assignment, "was", score

assignment = "Exam 1"
score = 85.5

x_print("Your grade on", assignment, "was", score)
Challenge

To complete this challenge, supply both the Python 2.7 and Python 3 translations
(using x_print for the Python 3 version) for the pseudocode provided in the comments.
FUNDAMENTALS
'''