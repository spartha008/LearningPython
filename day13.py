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

str3 = "WelcomeToTheConsole0"
print(str3.isalnum()) # Checks if the given string is alphanumeric (A-Z, a-z, 0-9) in boolean data type
print(str3.isalpha()) # Checks if the given string is aplha
print(str3.islower()) # Checks if the given string is in lower case 

str4 = "We wish you a Merry Christmas\n"
print(str4.isprintable()) # checks if the given string is printable

str5 = "        " # Using Spacebar
str6 = "        " # Using tab
print(str5.isspace()) # True if the sting contains white spaces
print(str6.isspace())  

str7 = "World Health Organization"
print(str7.istitle()) # Checks if every word of the string is a Capital

str8 = "Python is a Interpreted Language"
print(str8.startswith("Python")) # Checks if the given string starts with the given charecters
print(str8.swapcase()) # Swaps the cases of the words in the string
print(str8.title()) # Capitalizes each word within the string 