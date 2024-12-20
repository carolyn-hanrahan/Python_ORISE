# Basic Data Strucutres: Lists and Dictionaries

# NOTE: in python, java, and C, the first item in a list is indexed at 0. This is different from R, where the first item is 1.


print("\nLists\n")

gene_list = ["DDX11L1","WASH7P","MIR6859-1","MIR1302-2HG","MIR1302-2","FAM138A"]

# get the first element in the list, 0-indexed
gene1 = gene_list[0]
print("The 0th element of gene_list is: " + gene1)

# getting the last element in a list
last_gene = gene_list[-1]
print("The last element of gene_list is: " + last_gene)

# OR
last_gene = gene_list[5]
print("The element at index 5 of gene_list is: " + last_gene)

# getting a range of the list
print("Elements 1 to 3 (non-inclusive) of gene_list:", gene_list[1:3])
print("Elements -3 to end of gene_list:", gene_list[-3:])
print("Elements beginning to 3 of gene_list:", gene_list[:3])

# The same range concept works for strings
mystring = "The Quick Brown Fox"
print("Letters 4 to 9 (non-inclusive) of mystring: " + mystring[4:9])

# get the length of a list
print("The length of gene_list is", len(gene_list))

# lists can have elements of any type
gene_exp = [43.2, 45, 60.1, 12, 0.5, 23]
expval = gene_exp[2]
print("Element index 2 of gene_exp is:", expval)

# You can overwrite an element of the list
gene_list[3] = "BRCA3"
print("gene_list is now:", gene_list)

# creating a new variable equal to a list does NOT create a copy
# both variables point to the same list
gene_list2 = gene_list
gene_list2[2] = "DMR3"
print("gene_list has changed:", gene_list)

# use the copy method to make a actual copy of a list
gene_list2 = gene_list.copy()
gene_list2[2] = "DMR5"
print("gene_list:", gene_list)
print("gene_list2:", gene_list2)

# use the "in" keyword to check for membership in a list # this seems useful for checking the contents of a list. 
print("Is 'BRCA2' in gene_list?: ")
print("BRCA2" in gene_list)

exit()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Keys and dictionaries 

# dictionary = a collection of {key:value} pairs 

# example

practice_dictionary = {"stressed": chamomile,
                       "tired": matcha,
                       "confused": jasmine}



capitals = {"USA": "Washington D.C.",
                    "India": "New Delhi",
                    "China": "Beijing",
                    "Russia": "Moscow"}

print(capitals["China"])

colors = {"Rachel": "purple",
                  "Zak": "green",
                  "Carolyn": "blue-ish",
                  "Shilpa": "orange",
                  "Cian": "neon pink"}


print(friendsColors.get("Rachel"))


#print(gene_exp_dict["WASH7P"])

# https://www.youtube.com/watch?v=MZZSMaEAC2g following this video...



# Dictionary practice from the UC Davis course: 

#print("\nDictionaries\n")

#gene_exp_dict = {"DDX11L1":43.2,"WASH7P":45,"MIR6859-1":60.1,"MIR1302-2HG":12,"MIR1302-2":0.5,"FAM138A":23}

# You can access a value in the dictionary by referencing the key
#print("Value for key 'WASH7P: ")
#print(gene_exp_dict["WASH7P"])

# You can overwrite a value
#gene_exp_dict["WASH7P"] = 39
#print("New value for 'WASH7P': ")
#print(gene_exp_dict["WASH7P"])

# You can add a new value
#gene_exp_dict["BRCA2"] = 100
#print("gene_exp_dict with new key/value: ")
#print(gene_exp_dict)

# dict built-in methods

# returns all the keys
#print("List of keys in gene_exp_dict: ")
#print(gene_exp_dict.keys())

# returns all the values
#print("List of values in gene_exp_dict: ")
#print(gene_exp_dict.values())

# returns all the key,value pairs
#print("Key/Value pairs in gene_exp_dict: ")
#print(gene_exp_dict.items())

# you can also check if a key exists in a dictionary
#print("Does BRCA2 exist as a key in gene_exp_dict: ")
#print("BRCA2" in gene_exp_dict)

# to make a copy of a dictionary, you need t