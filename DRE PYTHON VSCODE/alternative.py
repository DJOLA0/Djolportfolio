# name the string
string = "Hello World"

# make a new empty string with 0 as starting numb for print
new_string = ""

# Loop through each character in the string
for i in range(len(string)):
# if index is even, make it uppercase
    if i % 2 == 0:
        new_string += string[i].upper()
# if index is odd, make it lowercase
    else:
        new_string += string[i].lower()

print(new_string)
''''''
# define the string
string = "I am learning to code"

# Split the string into a list of words
words = string.split()

# Loop through each word in the list 
for i in range(len(words)):
# if index is even, make it lowercase
    if i % 2 == 0:
        words[i] = words[i].lower()
# if index is odd, make it uppercase
    else: 
        words[i] = words[i].upper()
# Join the list back into one string with a space
back_together = " ".join(words)

print(back_together)

