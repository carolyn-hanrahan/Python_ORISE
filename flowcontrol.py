# Flow control AKA if statements, ifelse statements, while loops...
# Importatn iterative processes for programming
# Carolyn Hanrahan 
# November 21st, 2024 

# If statements (and elif statements... which seem to be python's way of saying if/else or ifelse statement): 

# elif statements 

#if a:
    #do this
#if (not a) and b:
    #do that
#if (not a) and (not b) and c:
   # do something else
#if (not a) and (not b) and (not c):
   # print "none of the above"
#As you can see, the elif...else notation allows you to write the same logic (the same control flow) without repeating the a condition over and over again.


# If statements: 
print("\nIF Statement 1\n")
diffexp = 67
if (diffexp > 0):
    print("Upregulated")
else:
    print("Downregulated")


print("\nIF Statement 2\n")
diffexp = -9
if (diffexp > 0):
    print("Upregulated")
else:
    print("Downregulated")


print("\nIF Statement 3\n")
# An if statement doesn't need an else
if (diffexp < 0):
    print("Downregulated")

print("\nIF Statement 4\n")
# If statements can have multiple elif (else if)
# Try changing the value of diffexp to see how the output changes.
# The if statement below has a logical error, see if you can find it.
diffexp = 25
if (diffexp > 50):
    print("Very Upregulated")
elif (diffexp > 0):
    print("Upregulated")
elif (diffexp < 0):
    print("Downregulated")
elif (diffexp < -50):
    print("Very Downregulated")

print("\nIF Statement 5\n")
# You can use "and", "or", & "not" to write more complex conditions
if (diffexp > 0 and diffexp < 50):
    print("Differential expression between 0 and 50")

print("\nIF Statement 6\n")
if (diffexp < -50 or diffexp > 50):
    print("High Down or Up regulation")

print("\nIF Statement 7\n")
# The body of an if statement can have multiple lines of code
diffexp=25
if (diffexp > 0 and diffexp < 50):
    print("Differential expression between 0 and 50")
    print("Check the significance")

print("\nIF Statement 8\n")
# You can have nested if statements
sig = 0.049
if (diffexp > 0 and diffexp < 50):
    print("Differential expression between 0 and 50")

    if (sig < 0.05):
        print("It's significant!")


# Practice problem!----------------------------------------------------------------------------------------------------------------------- 
        
#PRACTICE: Create a gene expression dictionary like the one from the Dictionary section to use below. Write an if statement (or statements) that do the following:

#if both SYF2 and FBX04 exist in the dictionary and both are upregulated (i.e. values > 0), then print “GO:1”
#Otherwise, if ATF2 does not exist in the dictionary or PLK1 exists and is downregulated (i.e. value < 0), then print “GO:2”
#Otherwise, if HUS1B exists and HUS1B is downregulated or SYF2 does not exist, then print “GO:3”
#Otherwise, print “GO:4”
#Change the keys and values in your dictionary to get each of the print statements to execute

# creating a gene expression dictionary:
gene_expression_dict = {"SYF2":43.2,"WASH7P":45,"MIR6859-1":60.1,"MIR1302-2HG":12,"MIR1302-2":0.5,"FAM138A":23, "FBX04":2, "HUS1B":-2}

# checking to see if certain genes exist in my dictionary: 
if "SYF2" in gene_expression_dict and "FBX04" in gene_expression_dict:
    print("SYF2 and FBX04 exist!")
else:
    print("SYF2 and FBX04 do not exist!")

# checking if certain genes exist in my dictionary, and if they do, whether their values are over 0. 
    
if "SYF2" in gene_expression_dict and "FBX04" in gene_expression_dict:
    if gene_expression_dict["SYF2"] > 0 and gene_expression_dict["FBX04"] > 0:
        print("GO:1")
elif "ATF2" not in gene_expression_dict or ("PLK1" in gene_expression_dict and gene_expression_dict["PLK1"] < 0):
    print("GO:2")
elif "HUS1B" in gene_expression_dict and gene_expression_dict["HUS1B"] < 0 and "SYF2" not in gene_expression_dict:
    print("GO:3")
else:
    print("GO:4")

# Yay I did it :')
    
#--------------------------------------------------------------------------------------------------------------------------------

# My favorite 'for loop'...

# A for loop is a programming construct that is used to run a a task 
# many times in a row, where you know how many times you want to loop

# Iterating using indices: 

print("\nFor Loops\n")

# The range(n) function returns values from 0 to n-1
for i in range(5):
    print(i)

# Iterating through a list

gene_list = ["DDX11L1","WASH7P","MIR6859-1","MIR1302-2HG","MIR1302-2","FAM138A"]

print("\nIterating through a list\n")

for id in gene_list:
    print(id + " is a gene of interest")

# Iterating through a dictionary
    
gene_exp_dict = {"DDX11L1":43.2,"WASH7P":45,"MIR6859-1":60.1,"MIR1302-2HG":12,"MIR1302-2":0.5,"FAM138A":23}

print("\nIterating through a dictionary\n")

for gene in gene_exp_dict.keys():
    print("Gene", gene, "has expression value:", gene_exp_dict[gene])

# While loops
# a while loop is used when you don't know how many times something will loop. 
# the body of the loop will continue to execute over and over until condition becomes false. 
#    
print("\nWhile Loops\n")

n = 1
fact = 1
while (n < 8):
    fact = fact * n
    n += 1
print(fact)

# Break and continue 

gene_list = ["DDX11L1","WASH7P","MIR6859-1","MIR1302-2HG","MIR1302-2","FAM138A"]


print("\nBreak\n")

for id in gene_list:
    print(id + " is a gene of interest")
    if (id == "MIR1302-2HG"):
        break

print("\nContinue\n")

for id in gene_list:
    if (id == "MIR1302-2HG"):
        continue

    print(id + " is a gene of interest")

#PRACTICE: Using your personnel dictionary (from the Dictionary practice), use a 
#single loop to print out all of the information for all of the employees. Using 
#the gene expression dictionary (from the Dictionary practice), use multiple nested 
#loops to print out all of the expression values individually for each sample.

# Start by recreating that dictionary in this script: 
    
# Creating a dictionary with keys that have multiple values associated with them 

employees = {"1234": "Steve Stephenson, M, 10/24/1900",
             "1235": "Malachi Dorby, M, 12/12/23",
             "1236": "Ellie Fluffball, F, 08/08/2021"}

for i in employees:
    print(employees[i])


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ nested for loop version... not exactly sure if this is what they wanted ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

          

# Nested loop to print all expression values
          
# Simulating a nested structure
data = [{"Gene_Expressions": gene_exp_dict}]

# Nested loops
for dataset in data:  # Outer loop (iterates over datasets)
    print("Dataset:")
    for gene, expression_value in dataset["Gene_Expressions"].items():  # Inner loop
        print(f"  Gene: {gene}, Expression Value: {expression_value}")