# Reverse complement program 
# Carolyn Hanrahan 
# November 27th, 2024 



# Define the sequence
sequence = "CGGTAGTCGAGCTGCGGATATAATATGCATATAGATCGCACGCTAGCTCATAAAAGCATGCATGCGGCTAGCTGCTGATCGTGTCG"

# Define the complement dictionary
complement_dict = {
    "A":"T",
    "T":"A",
    "G":"C",
    "C":"G"
}

# Step 2: Create a list of complements
complements = [complement_dict[base] for base in sequence]

# Step 3: Reverse the list
reversed_complements = complements[::-1]

# Step 4: Join the list into a string
reverse_complement = "".join(reversed_complements)

# Output the reverse complement to a file                  # this writes our Python code to a new text file called "reverse_complement.txt"
with open("reverse_complement.txt", "w") as file:
    file.write(reverse_complement)

# Print the reverse complement
print("Reverse Complement:", reverse_complement)

