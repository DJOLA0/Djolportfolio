# name the string with all the ! characters added
str_fox = "The!quick!brown!fox!jumps!over!the!lazy!dog!." 

# .replace() function to switch the ! with spaces
respaced = str_fox.replace("!" , " ")
print(respaced)
# reverse the string
reverse = respaced [::-1]
print(reverse)
# capitalise the reverse string with the .upper() fucntion and print
bigletters = reverse.upper()
print(bigletters)