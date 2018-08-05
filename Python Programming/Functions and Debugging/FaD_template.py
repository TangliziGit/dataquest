
# coding: utf-8

# In[1]:

from __future__ import print_function


# #Python Programming

# ##Functions and Debugging

# ###1: Reading the file in

# ####Instructions

# The story is stored in the "story.txt" file. Open the file and read the contents into the story variable.

# In[2]:

# Load the story stored in the file "story.txt".
f = open("data/story.txt", "r")
story = f.read()

print("story:", story)


# ###2: Tokenizing the file

# We now have to tokenize the file. Tokenizing sounds complicated, but its just the process of splitting the file into individual words.
# 
# We can get fancy with this, but for now, we'll just split the file up based on whitespace (the space character).

# ####Instructions

# The story is loaded into the story variable.
# 
# Tokenize the story, and store the tokens into the tokenized_story variable.

# In[3]:

# Split strings into lists with the .split() method.
text = "Bears are probably better than sharks, but I can't get close enough to one to be sure."
tokenized_text = text.split(" ")
tokenized_story = story.split(" ")

print("tokenized_story:", tokenized_story)


# ###3: Replacing punctuation

# In order to spell check our words, we'll be comparing the words in the story to a dictionary.
# 
# If the word is in the dictionary, it will be correct.
# 
# If it isn't, it will be incorrect.
# 
# Simple, but it will be effective in this situation.
# 
# In order to ensure that words that have apostrophes, commas, or other punctuation don't get falsely marked as incorrect, we need to remove all punctuation.

# ####Instructions

# The story has been loaded into tokenized_story.
# 
# Replace all of the punctuation in each of the tokens.
# 
# You'll need to loop through tokenized_story to do so.
# 
# You'll need to use multiple replace statements, one for each punctuation character to replace.
# 
# Append the token to no_punctuation_tokens once you are done replacing characters.
# 
# Don't forget to remove newlines!
# 
# Print out no_punctuation_tokens if you want to see which types of punctuation are still in the data.

# In[4]:

# Use the .replace function to replace punctuation in a string.
text = "Who really shot John F. Kennedy?"
text = text.replace("?", "?!")
#print(text)

# Replace strings with blank spaces in order to remove them.
text = text.replace("?", "")
#print(text)

no_punctuation_tokens = []
for token in tokenized_story:
    token = token.replace(".", "")
    token = token.replace(",", "")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    no_punctuation_tokens.append(token)
print("no_punctuation_tokens:", no_punctuation_tokens)


# ###4: Lowercasing the words

# For the same reason that we replace punctuation, we also need to make the tokens lower case.
# 
# We don't want to run into a situation where 'Farmer' isn't in the dictionary, but 'farmer' is.

# ####Instructions

# The tokens without punctuation have been loaded into no_punctuation_tokens.
# 
# Loop through the tokens and lowercase each one.
# 
# Append each token to lowercase_tokens when you're done lowercasing.

# In[5]:

# Make strings all lowercase using the .lower() method.
text = "MY CAPS LOCK IS STUCK"
text = text.lower()

# The text is much nicer to read now.
#print(text)

lowercase_tokens = []
for token in no_punctuation_tokens:
    token = token.lower()
    lowercase_tokens.append(token)
print("lowercase_tokens:", lowercase_tokens)


# ###5: Making a basic function

# Let's make a basic function.

# ####Instructions

# Define a function that takes degrees in fahrenheit as an input, and return degrees celsius
# 
# Use it to convert 100 degrees fahrenheit to celsius. Assign the result to celsius_100.
# 
# Use it to convert 150 degrees fahrenheit to celsius. Assign the result to celsius_150.

# In[6]:

# A simple function that takes in a number of miles, and turns it into kilometers
# The input at position 0 will be put into the miles variable.
def miles_to_km(miles):
    return miles/0.62137

# Return the number of kilometers equivalent to one mile.
print("miles_to_km(1):", miles_to_km(1))

# Convert 'a' from 10 miles to kilometers.
a = 10
a = miles_to_km(a)

# Convert and assign to a different variable.
b = 50
c = miles_to_km(b)

# Function that takes degrees in fahrenheit as an input, and return degrees celsius.
fahrenheit = 80
celsius = (fahrenheit - 32)/1.8

def convert(degrees):
    return (degrees - 32)/1.8

celsius_100 = convert(100)
print("celsius_100:", celsius_100)

celsius_150 = convert(150)
print("celsius_150:", celsius_150)


# ###6: Practice: functions

# Now that we know what a function is, let's practice a bit with them.

# ####Instructions

# Make a function that takes a string as input and outputs a lowercase version.
# 
# Then use it to turn the string lowercase_me to lowercase.
# 
# Assign the result to lowercased_string.

# In[7]:

# Function to split a string into a list.
def split_string(text):
    return text.split(" ")

sally = "Sally sells seashells by the seashore."
print("sally:", sally)

# Split 'sally' into a list.
print("split_string(sally):", split_string(sally))

# Assign the output to 'sally_tokens'.
sally_tokens = split_string(sally)

lowercase_me = "I wish I was in ALL lowercase"
print("lowercase_me:", lowercase_me)

# Function output a lowercase version of a string. 
def lowercase(text):
    return text.lower()

# Assign the output to 'lowercased_string'.
print("lowercase(lowercase_me):", lowercase(lowercase_me))


# ###7: Types of errors

# We are starting to get into more complex code now.
# 
# Before we go too far down that road, let's look into common code errors, and how to fix them.

# ####Instructions

# There are multiple syntax errors in the code to the right.
# 
# You can tell because of the error showing up in the results panel.
# 
# Fix the errors and get the code running properly. It should print all of the items in a.

# In[8]:

a = ["Errors are no fun!", "But they can be fixed", "Just fix the syntax and everything will be fine"]
b = 5
for item in a:
    if b == 5:
        print("item:", item)


# ###8: More syntax errors

# Syntax errors can take a lot of forms, so let's look at a few more.

# ####Instructions

# The code to the right has multiple syntax errors.
# 
# Fix them so the code prints out "I never liked that 6"

# In[9]:

a = 5
if a == 6:
    print("6 is obviously the best number")
else:
    print("I never liked that 6")


# ###9: Index errors

# Index errors occur when a list index that doesn't exist is referenced.

# ####Instructions

# The code to the right has multiple index errors.
# 
# Fix them so that the code prints the last item in each list.

# In[10]:

the_list = ["Harrison Ford", "Mark Hammil"]
print("the_list[1]:", the_list[1])

another_list = ["Jabba"]
print("another_list[0]:", another_list[0])


# ###10: Multiline functions

# Let's make a function to remove all punctuation.

# ####Instructions

# All the tokens from Julius's story are in the tokenized_story variable.
# 
# Write a function that removes all punctuation from an input string.
# 
# Then loop over tokenized_story and call the function to remove the punctuation from each token.
# 
# Append the tokens to no_punctuation_tokens.

# In[11]:

# Basic math function.
def do_math(number):
    # Multiply the number by 10.
    number = number * 10
    # Add 20 to the number.
    number = number + 20
    return number

print("do_math(20):", do_math(20))
a = do_math(10)

no_punctuation_tokens = []
def remove_punctuation(token):
    token = token.replace(".", "")
    token = token.replace(",", "")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    return token
    
for token in tokenized_story:
    token = remove_punctuation(token)
    no_punctuation_tokens.append(token)
print("no_punctuation_tokens:", no_punctuation_tokens)


# ###11: Making a function to lowercase input

# Now, let's add to our function so that it also lowercases input.

# ####Instructions

# We've written the remove_punctuation function for you. Can you add to it so that it also makes the output lowercase?
# 
# Then loop over the tokens in tokenized_story and normalize them with the function.
# 
# Append the tokens to normalized_tokens when you're done.

# In[12]:

def normalize(token):
    token = token.replace(".", "")
    token = token.replace(",", "")
    token = token.replace("'", "")
    token = token.replace(";", "")
    token = token.replace("\n", "")
    token = token.lower()
    return token

normalized_tokens = []
for token in tokenized_story:
    token = normalize(token)
    normalized_tokens.append(token)
print("normalized_tokens:", normalized_tokens)


# ###12: Practice with multiple argument functions

# Let's practice with functions that take multiple arguments

# ####Instructions

# Create a multiply function that takes in x, y, and z argument.
# 
# The function should return x * y * z
# 
# Assign the values of multiply(10,3,5) to a
# 
# Assign the values of multiply(20,-1,3) to b

# In[13]:

# Function to divide numbers at position 0 and 1
def divide(x,y):
    return x/y

# 5 is assigned to x, and 1 is assigned to y based on positions
print("divide(5,1):", divide(5,1))

# 1 is assigned to x, and 5 is assigned to y based on positions.
print("divide(1,5):", divide(1,5))

# Function to multiply numbers at position 0, 1, 2
def multiply(x, y, z):
    return x * y * z

a = multiply(10,3,5)
b = multiply(20,-1,3)


# ###13: Reading in and normalizing the dictionary

# The dictionary is stored in dictionary.txt
# 
# We'll need to read it in and normalize it.

# ####Instructions

# Read in the dictionary from the "dictionary.txt" file.
# 
# Split it into tokens based on the space character.
# 
# Normalize each token using the normalize function.
# 
# Append the normalized tokens to normalized_dictionary_tokens.

# In[14]:

def normalize(token):
    token = token.replace("."," ")
    token = token.replace(","," ")
    token = token.replace("'", " ")
    token = token.replace(";", " ")
    token = token.replace("\n", " ")
    token = token.lower()
    return token

normalized_dictionary_tokens = []
f = open("data/dictionary.txt", "r")
tokens = f.read().split("\n")
for token in tokens:
    token = normalize(token)
    normalized_dictionary_tokens.append(token)
print("normalized_dictionary_tokens:", normalized_dictionary_tokens)

normalized_story_tokens = []
f = open("data/story.txt", "r")
tokens = f.read().split(" ")
for token in tokens:
    token = normalize(token)
    normalized_story_tokens.append(token)
print("normalized_story_tokens:", normalized_story_tokens)


# ###14: Finding words that aren't spelled correctly

# A solution is in sight! All we need to do is loop through the normalized story tokens, and check if they are in the dictionary. If they aren't, they are potential misspellings.

# ####Instructions

# The normalized story tokens are in normalized_story_tokens, and the normalized dictionary tokens are in normalized_dictionary_tokens.
# 
# Loop through the story tokens, and check if each token is in the dictionary.
# 
# If the token is in normalized_dictionary_tokens, append it to correctly_spelled
# 
# If it isn't, append it to potential_misspellings.

# In[15]:

potential_misspellings = []
correctly_spelled = []
for token in normalized_story_tokens:
    if token in normalized_dictionary_tokens:
        correctly_spelled.append(token)
    else:
        potential_misspellings.append(token)

print ("correctly_spelled:", correctly_spelled)
print ("potential_misspellings:", potential_misspellings)

