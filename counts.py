# Writing a Python code for genetic analysis 
# Carolyn Hanrahan 
# November 27th, 2024 
#------------------------------------------------------------------------------------------

sequence = "CGGTAGTCGAGCTGCGGATATAATATGCATATAGATCGCACGCTAGCTCATAAAAGCATGCATGCGGCTAGCTGCTGATCGTGTCG"

# Create an empty dictionary to store counts
letter_counts = {}

# Iterate over each character in the sequence
for letter in sequence:
    # Increment the count for the letter in the dictionary
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

# Print the resulting dictionary
print(letter_counts)