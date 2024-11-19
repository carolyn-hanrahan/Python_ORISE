# My first solo python script 

#print("Hello, World!")

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