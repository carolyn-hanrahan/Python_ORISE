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