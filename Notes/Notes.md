# General Python Notes & Definitions
## Variables
Example:
```python
message = "Hello Python world!"
print(message)
```
Here 'message' is a created Variable and when called (print(message)) the text will be printed

```python
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)
```
Now the Variable 'message' has been replaced, or overwritten.  Both lines will be printed but only the last one will be remembered.

## Strings
Strings are numbers or letters contained within "quotation marks" or 'apostrophes'.
Either can be used as long as you're consistent.

This allows a 'string to contain "a quote" within'

### Changing Case in a String with Methods
```python
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
```
title = Capitalises first letter of each word

upper = Capitalises all characters

lower = changes any uppercase to lowercase

### Concatenating Strings
Useful to combine inputs from seperate entries
```python
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")
```
The + combines the variables together.

A space in quotation marks adds a space (" ")

This can also be stored in a variable
```python
message = "Hello, " + full_name.title() + "!"
print(message)
```
If this was added to the previous program would print the message "Hello, Ada Lovelace!" whilst simultaneously storing it in a variable for easy calling.

### Adding Tabs or Newlines to Strings
Tab or Indent = \t
```python
>>> print("Python")
Python
>>> print("\tPython")
    Python
```

Newline = \n
```python
>>> print("Languages:\nPython\nC\nJavaScript")
Languages:
Python
C
JavaScript
```

They can be combined too
```python
>>> print("Languages:\n\tPython\n\tC\n\tJavaScript")
Languages:
    Python
    C
    JavaScript
```

### Removing Whitespace
Whitespace are just spaces that could be accidentally inputted or otherwise.

Python interperets these as intentional so you can do the following to ensure certain spaces arent meant to be there.

```python
>>> favorite_language = ' python '
>>> favorite_language.rstrip()
' python'
>>> favorite_language.lstrip()
'python '
>>> favorite_language.strip()
'python'
```
.rstrip() = Removes spaces from the Right end

.lstrip() = Removes spaces from the left/beginning

.strip() = Removes spaces from either end

### Numbers as Strings (or Text)

```python
age = 25
str(age)
```
Or put the number directly inbetween the parenthesis

```python
# either
number_string = '25'
# or
number_string = str(25)
```

## Lists

In Python, square brackets [] denote a list, and individual items in the list are separated by commas.

### Creating a list

Example of a list:
```python
consoles = ['xbox', 'playstation', 'switch', 'steam deck']
print(consoles)
```

Items can be printed from a list using numbers starting from 0, for example:
```python
consoles = ['xbox', 'playstation', 'switch', 'steam deck']
print(consoles[0])
```
This would print the first item in the above list which would be xbox.  By putting -1 instead of 0 would give you the last item at the end of the list (-2, second to last etc)
Methods can also be used if you want to be all fancy and capitalise them etc
```python
consoles = ['xbox', 'playstation', 'switch', 'steam deck']
print(consoles[0].title())
```
This would capitalise the first letter: Xbox

### Forming or concatenating a sentence from a List
```python
consoles = ['xbox', 'playstation', 'switch', 'steam deck']
message = "I dont yet have my own " + consoles[-1].title() + "."

print(message)
```
Would return: I dont yet have my own Steam Deck.

## Making edits to a List
General info about altering items in a List

### Swapping items out for another
Doing a simple swap
```python
consoles = ['xbox', 'playstation', 'switch', 'steam deck']

consoles[0] = 'xbox series x'
print(consoles)
```
All this has done is change the first item in the list to the new one.  The newly printed List would be:
['xbox series x', 'playstation', 'switch', 'steam deck']

### Adding items to a list
To add a new item to the end of an existing list, you would append it.
```python
consoles = ['xbox', 'playstation', 'switch', 'steam deck']
print(consoles)
# The above is the initial list
# Below is the 'appended' list that has an addition.

consoles = ['xbox', 'playstation', 'switch', 'steam deck']
consoles.append('dreamcast')
print(consoles)
```
This would result in the following:
['xbox', 'playstation', 'switch', 'steam deck']
['xbox', 'playstation', 'switch', 'steam deck', 'dreamcast']


You could even start off with an empty list and 'append' items to it as you go along by starting off with:
```python
emptyList = []
```

### Slotting items into a list
Not to be confused with 'append', you can insert or slot new items into a list with insert().  Do this by telling it the index location of where you want the new item, and the existing items will move one space to the right.
```python
consoles = ['xbox', 'playstation', 'switch', 'steam deck']
consoles.insert(0, 'dreamcast')
print(consoles)
```
This would print:
['dreamcast', 'xbox', 'playstation', 'switch', 'steam deck']

### Permenantly removing items from a list
By using the del statement you can remove items permenantly from a list if you know the position.
```python
consoles = ['xbox', 'playstation', 'switch', 'steam deck']
print(consoles)

del consoles[1]
print(consoles)
```
Here I've just removed 'playstation' from the list.

### Removing, but NOT deleting, an item from a list
Using the pop() Method you can remove an item form a list and store it somewhere else temporarily to be called upon later.


Simply using pop() will 'pop' the last item off of the list, whereas specifying the item location number pop(2), will in thi case remove the 3rd item in the list.
```python
consoles = ['xbox', 'playstation', 'switch', 'steam deck']
print(consoles)

poppedConsoles = consoles.pop(1)
print(consoles)
print(poppedConsoles)
```
Above I start with a list and printed it.
Then I created a Variable to store 'playstation' (which was at position 1) and simultaneously popped 'playstation' straight into it.
Next I asked to print the new main List as well as the newly created pop list which would give you:
['xbox', 'playstation', 'switch', 'steam deck']
['xbox', 'switch', 'steam deck']



## if Statement
```python
if n > 5:
    pass
```