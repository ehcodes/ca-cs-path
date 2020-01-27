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

print(add_greetings(["Owen", "Max", "Sophie"]))

# 3.
def delete_starting_evens(lst):
  if (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

print(delete_starting_evens([4, 8, 10]))

# 4.
def odd_indices(lst):
  newLst=[]
  for index in range(1, len(lst), 2):
    newLst.append(lst[index])
  return newLst

print(odd_indices([4, 3, 7, 10, 11, -2]))

# 5.
def exponents(bases, powers):
  products = []
  for base in bases:
    for power in powers:
      products.append(base**power)
  return products

print(exponents([2, 3, 4], [1, 2, 3]))

# 5.
def larger_sum(lst1, lst2):
  if sum(lst1) > sum(lst2):
    return lst1
  elif sum(lst1) < sum(lst2):
    return lst2
  else:
    return lst1

print(larger_sum([1, 9, 5], [2, 3, 7]))

# 6.
def over_nine_thousand(lst):
  if lst == []:
    return 0
  else:
    sum = 0
    for num in lst:
      if sum < 9000:
        sum+=num
        print(sum)
    return sum

print(over_nine_thousand([8000, 900, 120, 5000]))

# 7.
def max_num(nums):
  return max(nums)

print(max_num([50, -10, 0, 75, 20]))

# 8.
def same_values(lst1, lst2):
  index = 0
  same_vals=[]
  while index < len(lst1):
    if lst1[index] == lst2[index]:
      same_vals.append(index)
    index+=1
  return same_vals

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# 9.
def reversed_list(lst1, lst2):
  lst2.reverse()
  if lst1 == lst2:
    return True
  else:
    return False

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))