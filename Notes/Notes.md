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

## if Statement
```python
if n > 5:
    pass
```