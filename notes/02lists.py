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

# When range() is given a single argument, it creates a list with consecutive numbers starting at 0 and ending one number below the argument.
one = range(12)
print(one)
# prints: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# When range() is given two arguments (and the smallest number is given first), it creates a list with consecutive numbers starting at the least argument and ending 1 below the greatest argument.
two=range(15,29)
print(two)
# prints: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

# When range() is given three arguments, first two arguments mean the same they do when giving 2 arguments and the third argument is the number by which the output numbers are being counted by.
three=range(12,31,5)
print(three)
# prints: [12, 17, 22, 27]

# When range() is given two arguments (and the greatest number is given first), it creates an empty list.
four=range(29,15)
print(four)
# prints: []

# The len() method returns the number of elements in the list used as it's argument (Len is short for length).
print("The are "+str(len(three))+" elements in list three.")

# python lists are zero-indexed
# If you try to reference an element not in the list, you will receive the following error "IndexError: list index out of range"
indexMax4=[1,2,3,4,5]
# print(indexMax4[5]) - have to comment out in order to continue taking notes in this file
# unsurprisingly this produces, error "IndexError: list index out of range"

# using an index of -1 will always turn up the last element in a list
print(indexMax4[-1])
# produces: 5 because 5 is the last element in indexMax4

# Slicing a list is when you copy a portion of one list and create another list with it. It does not alter the original list.
# list[start:end]
	# list - the list you're copying from
	# start - index number to begin copying at.
	# end - index+1 of the last index we're copying'.

islands = ['barbados', 'puerto rico', 'hawaii', 'trinidad', 'hispaniola', 'cuba']
print(islands)
# results: ['barbados', 'puerto rico', 'hawaii', 'trinidad', 'hispaniola', 'cuba']

beginning = islands[0:2]

print(beginning)
# results: ['barbados', 'puerto rico']

# List Slicing Tips & Tricks:

# 	start can be ommitted if we're starting at the 0 indexed element - would look like-> list[:end]
print(str(islands[:3])+" islands[:3]")
# 	results: ['barbados', 'puerto rico', 'hawaii'] islands[:3]

# 	end can be ommitted if you want to end with the last indexed element
print(str(islands[2:])+" - islands[2:]")
# 	results: ['hawaii', 'trinidad', 'hispaniola', 'cuba'] - islands[2:]

# 	if start is a negative number and end is omitted, you start copying the absolute value of [start], elements from the end.
print(str(islands[-3:])+" - islands[-3:]")
# 	results: ['trinidad', 'hispaniola', 'cuba'] - islands[-3:]

# Count method can be used to search through a list and return the number of times the supplied argument is in a list.
print(islands.count('barbados'))
# results:	1

cities = ['LDN', 'Pari', 'Roma', 'LA', 'NY']
print(cities)

# if you try to assign your sorted list to a new variable, it will be a NoneType.
# The sort method sorts the existing list, it doesn't create a new list so you can't store the not-new list in a new variable.
# This attempt to assign the sorted list to a variable, will sort the list so if you re-print it you will find it is now alphabetically sorted.
sorted_cities = cities.sort()
print(str(sorted_cities))
print(cities)

# The sorted method is similar to sort, except it envelopes the list instead of using dot notation.
sorted_names = sorted(names)

# sorted() creates a new list, it does not sort the existing list and can be assined to a new variable.

print(sorted_names)
# results:['bob', 'dylan', 'joe', 'kayla', 'lynn', 'mel', 'tasha']

print(names)
# results: ['joe', 'mel', 'kayla', 'bob', 'dylan', 'tasha', 'lynn']

# tuples are immutable objects similar to lists, tuples are sequences.
# tuples use parenthesis, not square brackets.
my_info = ('engrid',25,'alive')

# tuple can be unpacked (ex. below)
name, age, status = my_info
print(name) # prints 'engrid'
print(age) # prints 25
print(status) # prints 'alive'

# single element tuples have to use a trailing comma, otherwise it's just being stored as a varaible.
single_element_tuple = (4,)
vs
failed_to_become_tuple = (4)














