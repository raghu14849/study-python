# Program to count vowels and consonants in a string

# Read a string from user
string = input("Enter a string: ")

# Convert to lowercase for easier comparison
string = string.lower()

# Define vowels
vowels = "aeiou"

# Initialize counters
vowel_count = 0
consonant_count = 0

# Count vowels and consonants
for char in string:
    if char.isalpha():  # Check if character is a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Print the results
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
