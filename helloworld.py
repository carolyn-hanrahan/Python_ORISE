# My first solo python script 
# Carolyn Hanrahan 
# November 19th, 2024 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#print("Hello, World out there....")

# integers: 
print("Basic Data Types\n")

gene_count = 7
print("Gene count is: ", gene_count)

# floats: 
gene_exp = 3.89
print("Gene expression is: ", gene_exp)

# strings:  
gene_id = "BRCA2"
print("Gene ID is: ", gene_id)

carolyn_state = "tired"

print("carolyn's state:", carolyn_state)

# built-in string methods: 

tmpstr = "hello my name is Carolyn."

allcaps = tmpstr.upper()
print("tmpstr in all caps: ", allcaps)

newstr = tmpstr.replace("Carolyn","Caro")
print("After replacing Carolyn with Caro")
print(newstr)

# This is a comment. Comments are lines that being with a hashtag symbol.
# They are ignored by the python interpreter and are used to document your code.

# you can also use the + symbol to concatenate strings
tmpstr2 = "How are you doing?"
print(tmpstr + " " + tmpstr2)

# you can find the position of one string in another
print("Position of 'you' in tmpstr2")
print(tmpstr2.find("you"))

# returns -1 if not found
print("Position of 'california' in tmpstr2")
print(tmpstr2.find("california"))

# Exploring the “split”, “isdigit”, and “index” methods

#'isdigit'
x = tmpstr2.isdigit()
print(x)

#'split'
txt = "welcome to the jungle"

x = txt.split()

print(x)

#'index'
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Booleans.... https://ucdavis-bioinformatics-training.github.io/2024-November-Introduction-To-Python-For-Bioinformatics/python/python2

# Boolean data types are true or false 

# fun python/VS code thing I learned: highlight code and press shift followed by enter to run a specific setion of code 


print("\nBooleans\n")

control = False
treatment = True
print("Value of control: ", control)
print("Value of treatment: ", treatment) 

# Booleans are good at making comparisons. 
# For example, compare the following integers: 

print("Is 1<1?")
print(1<1)
print("Is 1<2?")
print(1<2)
print("Is 2>1?")
print(2>1)
print("Is 1<=1?")
print(1<=1)
print("Is 2>=1?")
print(2>=1)

# the double equals is an equality comparison, a single equals is for assignment.
print("Does 1 equal 1?")
print(1==1)
print("Does 0 equal 1?")
print(0==1)

# not equals
print("Is 2 not equal to 7?")
print(2 != 7)

# You can also do string comparisons
gene_id = "BRCA2"
hw = "HELLO!!! WORLD!!!"
print("Does gene_id equal 'BRCA2'?")
print(gene_id == "BRCA2")
print("Does hw equal 'hello'?")
print(hw == "hello")
print(gene_id == hw)

# Built-in datatypes and the type function 

# you can use the 'type' function to query the type of variable 
type(control) #boolean
type(hw) #string 

# okay I think we get this part. 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Some basic math functions:
print("\nArithmetic\n")

a = 21
b = 3

# Addition
print("a + b is: ")
sum = a + b

print("a + b is", sum)

# "c += 5" is shorthand for "c = c + 5"
c = 83
c += 5
print(c)
print("The current value of c is:", c)

# Subtraction
print("b - a is:", b - a)

# Division
print("a / b is: ")
print(a/b)

# Exponents
print("4 to the power of b is: ", 4**b)
#or
expb = pow(4,b)
print(expb)

# Remainder 
print("4 mod 3 is: ", 4 % 3)

# Absolute value
av = abs(22-32)
print("The absolute value of 22 - 32 is: ", av)

# Round, Floor, Ceiling
print("3.2 rounded:", round(3.2))
print("3.2 truncated:", int(3.2))

import math
print("Ceiling of 3.2 is:", math.ceil(3.2))
print("Floor of 3.2 is:", math.floor(3.7))
print("Truncating 3.7:", int(3.7))

# The math package has many common math functions 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Basic Data Strucutres: Lists and Dictionaries -> See new file "lists.py"

