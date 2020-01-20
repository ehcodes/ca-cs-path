# Create a function named in_range() that has three parameters named num, lower, and upper. The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.
def in_range(num,lower,upper):
  if(num>=lower) and (num<=upper):
    return True
  else:
    return False

# Create a function named movie_review() that has one parameter named rating.
# 	If rating is less than or equal to 5, return "Avoid at all costs!".
# 	If rating is between 5 and 9, return "This one was fun.".
# 	If rating is 9 or above, return "Outstanding!"

def movie_review(rating):
	if (rating<=5):
		return "Avoid at all costs!"
	elif(rating>5) and (rating<9):
		return "This one was fun."
	else:
		return "Outstanding!"


# Create a function named twice_as_large() that has two parameters named num1 and num2.
# Return True if num1 is more than double num2. Return False otherwise.

def twice_as_large(num1,num2):
	if(num1>(num2*2)):
		return True
	else:
		return False

# Create a function named large_power() that takes two parameters named base and exponent.
# If base raised to the exponent is greater than 5000, return True, otherwise return False

def large_power(base,exponent):
	if((base**exponent)>5000):
		return True
	else:
		return False


# Create a function called divisible_by_ten() that has one parameter named num.
# The function should return True if num is divisible by 10, and False otherwise. Consider how to use modulo (%) to check for divisibility.

def divisible_by_ten(num):
	if(num%10==0):
		return True
	else:
		return False


# Create a function called max_num() that has three parameters named num1, num2, and num3.
# The function should return the largest of these three numbers. If any of two numbers tie as the largest, you should return "It's a tie!".

def max_num(num1,num2,num3):
	numList=[num1,num2,num3]
	maxNum = max(numList)
	if(num1==num2 and maxNum==num1) or (num2==num3 and maxNum==num2) or (num3==num1 and maxNum==num3):
	    return "It's a tie!"
	else:
		return maxNum

# Create a function called over_budget that has five parameters named budget, food_bill, electricity_bill, internet_bill, and rent.
# The function should return True if budget is less than the sum of the other four parameters. You’ve gone over budget! Return False otherwise.

def over_budget(budget,food_bill,electricity_bill,internet_bill,rent):
	moneySpent=food_bill+electricity_bill+internet_bill+rent
	if budget < moneySpent:
		return True
	else:
		return False

# Create a function named always_false() that has one parameter named num.
# Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no matter what number is stored in num.

def always_false(num):
	if num+1>num:
		return False
	elif num-1<num:
		return False

# Create a function named not_sum_to_ten() that has two parameters named num1 and num2.
Return True if num1 and num2 do not sum to 10. Return False otherwise.

def not_sum_to_ten(num1,num2):
	if num1+num2!=10:
		return True
	else:
		return False

# Create a function named same_name() that has two parameters named your_name and my_name.
# If our names are identical, return True. Otherwise, return False.

def same_name(your_name,my_name):
	if your_name==my_name:
		return True
	else:
		return False