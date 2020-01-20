# In python a list is an ordered set of objects encompassed in square brackets with each item seperated by commas.
# The following is a list: primaryColors = [red, yellow, blue]

# Lists can contain numbers, strings, and/or other lists.

# The built-in function, zip(), takes two lists and returns an object resembling a merging of the two lists. EX:

# setup:
primaryColors=['red', 'blue', 'yellow']
numberOfPrimaryColors = [1,2,3]
orderOfColors=zip(numberOfPrimaryColors,primaryColors)
# supposedly if you don't use list(), and try to outright print the variable, it will say something like, "<zip object at 0x7f411ae0cc08>", pointing you to the location within your PC of the zip object you created.This wasn't my result when I ran this file in the terminal.
print(list(orderOfColors))

# results:
# [(1, 'red'), (2, 'blue'), (3, 'yellow')]

# append() method can be used to add a single object to the end of a list

# In order to add multiple items to a list you must combine the old list with another one.
names=['joe','mel','kayla']
print(str(names)+" - 1st")
names=names+['bob','dylan','tasha']
print(str(names)+" - 2nd")

# If you onlywant to add 1 element into the list using the plus, you would add it in square brackets
names=names+['lynn']
print(str(names)+" - 3rd")

# The built-in function, range(), creates a list of consecutive numbers.

# When range() is given a single argument, it creates a list with consecutive numbers starting at 0 and ending one number below the argument.
one = range(12)
print(one)
# prints: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# When range() is given two arguments (and the smallest number is given first), it creates a list with consecutive numbers starting at the least argument and ending 1 below the greatest argument.
two=range(15,29)
print(two)
# prints: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

# When range() is given three arguments, first two arguments mean the same they do when giving 2 arguments and the third argument is the number by which the output numbers are being counted by.
three=range(12,31,2)
print(three)
# prints: [12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

# When range() is given two arguments (and the greatest number is given first), it creates an empty list.
four=range(29,15)
print(four)
# prints: []
