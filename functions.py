# Functions in Python 
# Carolyn Hanrahan 
# November 25th, 2024 
# a function is a block of code that only gets run
# when it is called. 

# First, practice making a BASIC function. 

def first_function(number):
    print(number +1)

first_function(2)

def second_function():
    print("we have created another function")

second_function()

def custom_function(number, power):
    print(number**power)


# imports are used to be able to use code from other libraries
import math

#print("\nFunctions\n")

#print("\nFunction 1\n")
# Functions can have zero parameters and return nothing
#def hello():
   # print("Hello, World!")

#hello()

#print("\nFunction 2\n")
# Or they can have multiple parameters and return something
def logfc(exp1,exp2):
    retval = math.log(exp2/exp1)
    return(retval)

gene_exp_dict = {"DDX11L1":43.2,"WASH7P":45,"MIR6859-1":60.1,"MIR1302-2HG":12,"MIR1302-2":0.5,"FAM138A":23}

de = logfc(gene_exp_dict['WASH7P'], gene_exp_dict['FAM138A'])
#print("The DE value is", de)

#print("\nFunction 3\n")

# They can also have default values for any of the parameters
def logfc(exp1,exp2,sigdig=3):
    retval = math.log(exp2/exp1)
    retval = round(retval, sigdig)
    return(retval)

#print(logfc(89,12,5))
#print(logfc(89,12))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ practice ~~~~~~~~~~~~~~

# write a function to calculate fibonacci numbers
# given a maximum value!.

def fib_function(Fn1, Fn2):
    print("Fn equals", Fn1+Fn2)

fib_function(4,2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def fibonacci_below_max(max_value):
    """
    Generate a list of Fibonacci numbers below the given maximum value.
    
    Parameters:
        max_value (int): The maximum value for Fibonacci numbers.
    
    Returns:
        list: A list of Fibonacci numbers below max_value.
    """
    if max_value <= 0:
        return []
    
    fib_numbers = []
    a, b = 0, 1
    while a < max_value:
        fib_numbers.append(a)
        a, b = b, a + b
    
    return fib_numbers

# Call the function with a maximum value of 100
print(fibonacci_below_max(100))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Global vs. local variables 

"""
when a varible is defined outside of a function, 
it is known as a global variable. a local variable is 
only accessible within a function. It is generally 
good programming etiquette to use local variables
rather than global variables when writing functions


"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# File handling --> learning how to read from and write files

# I saved a TSV file (tab separated values file)


# Reading in a file: 
print("\nFile Handling\n")

# open the file for reading
f = open("DMR.GBM2.vs.NB1.tsv", "r")
print(f.readline())
print(f.readline())

# you can use a loop to read the whole file, line by line
f2 = open("DMR.GBM2.vs.NB1.tsv", "r")
for line in f2:
    print(line)

# always close file handles when you're done with them
f.close()
f2.close()

# Writing a file: 

# open a new file for writing, will create if doesn't exist
f3 = open("myfile.txt", "w")
f3.write("Hello World!")
f3.close()

# read the whole file at once
f4 = open("myfile.txt","r")
print(f4.read())
f4.close()

# Now append to the file
f3 = open("myfile.txt", "a")
f3.write("How are you?")
f3.close()

f4 = open("myfile.txt","r")
print(f4.read())
f4.close()