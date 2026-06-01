# String Methods in Python
# Strings are immutable
a = "!!!Harry!! !!!! !Harry"
print(len(a))
print(a)
print(a.upper()) # All uppercase 
print(a.lower()) # All lowercase
print(a.rstrip("!")) # Removes ! from the end of the sentence
print(a.replace("Harry", "John")) # Replaces 
print(a.split(" ")) # Turns it into a list when the sentence is separated by space
blogHeading = "introduction tO js"
print(blogHeading.capitalize()) # Coverts all the other letters to lowercase

str1 = "Welcome to the Console!!!"
print(len(str1))
print(str1.center(50, ".")) # Moves the sentance to the center and uses . to fill in the space
print(len(str1.center(50)))
print(a.count("Harry")) # Counts the number of times the word is repeated in the sentence
print(str1.endswith("!!!")) # Tells us if the string ends with the specific charecters in boolean data type
print(str1.endswith("to", 4, 10)) 

str2 = "He's name is Dan. He is an honest man."
print(str2.find("is")) # Searches for the first occurance of the given charecter
print(str2.index("is")) # Searches for the first occurance of the given value and returns the index where it is present
    # Raises exception if the given value is absent from the string

str3 = "WelcomeToTheConsole"
print(str3.isalnum()) # Checks if the given string is alphanumeric (A-Z, a-z, 0-9) in boolean data type
