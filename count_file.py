# Get the nucleotide count from a fasta file 
# Carolyn Hanrahan 
# November 27th, 2024 

#-------------------------------------------------

# We are going to use a similar method as was used in my 'counts.py' file. 

# Define the path to your FASTA file
fasta_file = "seq.fa" #(note that we save our file in the same folder!)

# Initialize an empty dictionary to store counts
letter_counts = {}

# Open the file and read it line by line
with open(fasta_file, "r") as file:
    for line in file:
        # Remove the newline character from the end of the line
        line = line.strip()

        # Skip header lines (lines that start with ">")
        if line.startswith(">"):
            continue
        
        # Iterate over each character in the sequence line
        for letter in line:
            # Increment the count for the letter in the dictionary
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

# Print the resulting dictionary with counts
print(letter_counts)