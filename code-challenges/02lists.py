# Create a function named double_index that has two parameters, a list named lst and a single number as index.
# The function should return a new list where all elements are the same as in lst except for the element at index, which should be double the value of the element at index of lst.
# If index is not a valid index, the function should return the original list.
# For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:
# double_index([1, 2, 3, 4], 2)


def double_index(list, index):
	if index >= len(list):
		return list
	elif index < 0:
		return list
	else:
		alteredList = list
		doubledNumber = alteredList[index] * 2
		alteredList[index] = doubledNumber
		return alteredList

print(double_index([1, 2, 3, 4], 2))

# Create a function named remove_middle which has three parameters named lst, start, and end.
# The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed.

def remove_middle(lst, start, end):
	end=end+1
	removingLst = lst[start:end]
	for elem in removingLst:
		lst.remove(elem)
	return lst

print(remove_middle([4, 8 , 15, 16, 23, 42], 1, 3))

# Create a function named more_than_n that has three parameters named lst, item, and n.
# The function should return True if item appears in the list more than n times. The function should return False otherwise.

def more_than_n(lst, item, n):
	if lst.count(item) > n:
		return True
	else:
		return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# Create a function named more_frequent_item that has three parameters named lst, item1, and item2.
# Return either item1 or item2 depending on which item appears more often in lst.
# If the two items appear the same number of times, return item1.

def more_frequent_item(lst, item1, item2):
	item1count = lst.count(item1)
	item2count = lst.count(item2)
	if item1count > item2count:
		return item1
	elif item2count > item1count:
		return item2
	else:
		return item1

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# Create a function called middle_element that has one parameter named lst.

def middle_element(lst):
	lstLen = len(lst)
	if lstLen%2==0:
	# 	If there are an even number of elements, the function should return the average of the middle two elements.
		pre_avg = lst[int(lstLen/2) - 1] + lst[int(lstLen/2)]
		return pre_avg/2
	else:
	# 	If there are an odd number of elements in lst, the function should return the middle element.
		return lst[int(lstLen/2)-.5]

print(middle_element([5, 2, -10, -4, 4, 5]))

# Write a function named append_sum that has one parameter named lst.
	# The function should add the last two elements of lst together and append the result to lst.
	# It should do this process three times and then return lst.
def append_sum(lst):
	for x in range(3):
		last = lst[-1]
		secLast = lst[-2]
		newNum = last+secLast
		lst.append(newNum)
		print(newNum)
	return lst

print(append_sum([1, 1, 2]))

# Write a function named larger_list that has two parameters named lst1 and lst2.
	#	The function should return the last element of the list that contains more elements.
	#	If both lists are the same size, then return the last element of lst1.

def larger_list(lst1, lst2):
	if len(lst2) > len(lst1):
		return lst2[-1]
	else:
		return lst1[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# Write a function named combine_sort that has two parameters named lst1 and lst2.
	# The function should combine these two lists into one new list and sort the result.
	# Return the new sorted list.

def combine_sort(lst1, lst2):
	lst3 = []
	for el1 in lst1:
		lst3.append(el1)
	for el2 in lst2:
		lst3.append(el2)
	lst3.sort()
	return lst3

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

# Create a function called append_size that has one parameter named lst.
# 	The function should append the size of lst (inclusive) to the end of lst.
# 	The function should then return this new list.

def append_size(lst):
	sizeOfLst = len(lst)
	lst.append(sizeOfLst)
	return lst

print(append_size([23, 42, 108]))


# Create a function called every_three_nums that has one parameter named start.
	# The function should return a list of every third number between start and 100 (inclusive).
	# If start is greater than 100, the function should return an empty list.
	# EX: every_three_nums(91) should return the list [91, 94, 97, 100].
def every_three_nums(start):
	if start<101 and start > 0:
		start=int(start)
		lst = []
		lst.extend(range(start,101,3))
		return lst
	else:
		return []
print(every_three_nums(91))

