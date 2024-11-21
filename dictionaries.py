# Python script specifically made for practicing dictionaries 
# Carolyn Hanrahan 
# November 21st, 2024 

capitals = {"Vermont": "Montpelier",
            "Massachusetts": "Boston",
            "Other state": "I don't know"}

#print(capitals)

#print(capitals["Vermont"])

#print(capitals["Other state"])

#print(capitals.get("Vermont"))


# Using if/else statements to check what values exist within our dictionary 
if capitals.get("Rhode Island"):
    print("that capital exists")
else:
    print("that capital doesn't exist")

if capitals.get("Vermont"):          # just switch out the value of state you are trying to find the capital for, in this case. 
    print("that capital exists")
else:
    print("that capital doesn't exist")

# Altering your dictionary: 

capitals.update({"Florida":"Tallahassee"})

#print(capitals)

# Creating a dictionary with keys that have multiple values associated with them 

employees = {"1234": "Steve Stephenson, M, 10/24/1900",
             "1235": "Malachi Dorby, M, 12/12/23"}


#print(employees)

#print(employees["1234"])

print(employees["1234"(2)])

# Creating a dictionary that is more genetics-themed ---------------------------------------------------------------------

gene_exp_dict = {"DDX11L1":43.2,"WASH7P":45,"MIR6859-1":60.1,"MIR1302-2HG":12,"MIR1302-2":0.5,"FAM138A":23}

# You can access a value in the dictionary by referencing the key
print("Value for key 'WASH7P: ")
print(gene_exp_dict["WASH7P"])

# You can overwrite a value
gene_exp_dict["WASH7P"] = 39
print("New value for 'WASH7P': ")
print(gene_exp_dict["WASH7P"])

# You can add a new value
gene_exp_dict["BRCA2"] = 100
print("gene_exp_dict with new key/value: ")
print(gene_exp_dict)

# dict built-in methods

# returns all the keys
print("List of keys in gene_exp_dict: ")
print(gene_exp_dict.keys())

# returns all the values
print("List of values in gene_exp_dict: ")
print(gene_exp_dict.values())

# returns all the key,value pairs
print("Key/Value pairs in gene_exp_dict: ")
print(gene_exp_dict.items())

# you can also check if a key exists in a dictionary
print("Does BRCA2 exist as a key in gene_exp_dict: ")
print("BRCA2" in gene_exp_dict)

# to make a copy of a dictionary, you need to use the "copy" method
#gene_exp_dict_copy = gene_exp_dict.copy() 



