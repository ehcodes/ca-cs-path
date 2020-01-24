# 1.
def divisible_by_ten(nums):
	total = 0
	for num in nums:
		if num % 10 == 0:
			total += 1
	return total

print(divisible_by_ten([20, 25, 30, 35, 40]))

# 2.
def add_greetings(names):
	greetings = ["Hello, "+ name for name in names]
	return greetings

# 3.

print('StartHEREHEREHEREHEREHEREHEREHEREHERE')
def delete_starting_evens(lst):
	# newlst = [lstEl.pop(i) for el in lst if ]
	for lstEl in lst:
		if lstEl[0] % 2 == 0:
			lst.pop(0)
			print lst
	print(str(lst)+" final")
# The function should remove elements from the front of lst until the front of the list is not even.
# The function should then return lst.
# For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].
# Make sure your function works even if every element in the list is even!
print(delete_starting_evens([4, 8, 10]))
