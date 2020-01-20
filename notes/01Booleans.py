# True or False is returned when using relational operators which cocmpare two values.
# Equals is == and Not Equals is !=
# True and False are "bool" types
# a boolean variable is a variable set to a bool (True or False)

# Boolean operators combine smaller boolean expressions into a single exxpression.

# Three major boolean operators are as follows:
# 	and
# 		combines two boolean expressions and evaluates as True only if both expressions are True
# 	or
# 		combines two boolean expressions and evaluates as True as long as one of the expressions is true
# 	not
# 		takes one boolean expressions and reverses it's value. Adding not to the beginning of the Boolean expression makes it the oppositie of what it would have been without the not operator.

# 		he registrar’s office at Calvin Coolidge’s Cool College has been so impressed with your work so far that they have another task for you. They want you to return to the first function you wrote, graduation_reqs, and add in several checks using and and not statements.

# If a student meets both requirements the function should return
# "You meet the requirements to graduate!"
# If a student’s GPA is greater or equal to 2.0 but they don’t have enough credits the function should return
# "You do not have enough credits to graduate."
# If they have enough credits but their GPA is less than 2.0 the function should return
# "Your GPA is not high enough to graduate."
# If they do not have enough credits and their GPA is less than 2.0, the function should return
# "You do not meet either requirement to graduate!"
# Make sure your return value matches those strings exactly. Capitalization, punctuation, and spaces matter!

# 	def graduation_reqs(gpa, credits):
# 		if (gpa >= 2.0) and (credits >= 120):
# 			return "You meet the requirements to graduate!"
# 		if (gpa >= 2.0) and (not credits >= 120):
# 			return "You do not have enough credits to graduate."
# 		if (gpa < 2.0) and (credits >= 120):
# 			return "Your GPA is not high enough to graduate."
# 		if (not gpa >= 2.0) and (not credits >= 120):
# 			return "You do not meet either requirement to graduate!"

# if... elif... else... statements
# def grade_converter(gpa):
# 	if(gpa>=4.0):
# 		return "A"
# 	elif(gpa>=3.0):
# 		return "B"
# 	elif(gpa>=2.0):
# 		return "C"
# 	elif(gpa>=1.0):
# 		return "D"
# 	else:
# 		return "F"

# try and except statements:

# 	try
# 		functionThatDoesStuff()
# 	except ErrorName:
# 		print("You've run into a name error!")


# try and except statements will run the "try" statement, if it comes across the error in the except statement it will run the code in that statement.















# Space saving, fuck this scroll to bottom nonsense.