from typing import Text


print('spam eggs')  # single quotes

print('doesn\'t')  # use \' to escape the single quote...

print("doesn't")  # ...or use double quotes instead

print('"Yes," they said.') # double or single quotes inside any one of the other are automaticaly escaped

print("\"Yes,\" they said.") # escape character

print('"Isn\'t," they said.') # double quotes are automatically escaped, single quotes 

print('''I dont know 
            what this 
does''')                   #If we use triple quotes, it will print the way it is given in multiple lines

Word = 'Python'
print(Word[0])          #you can index string from left to right using index 0
print(Word[-0])         #you can index string from right to left using negative numbers
print(Word[-1])         #since -0 is the same as 0, negative indices start from -1.

print(type(Word[-1]))   #unlike C or C++, there is only one class 'string' #no char data type
print(type(Word))
