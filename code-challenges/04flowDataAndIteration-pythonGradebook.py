# This project is completed with data supplied by CA

# Create a list called subjects and fill it with the classes you are taking:
# "physics"
# "calculus"
# "poetry"
# "history"

subjects=["physics", "calculus", "poetry", "history"]

# Create a list called grades and fill it with your scores:
# 98
# 97
# 85
# 88

grades = [98, 97, 85, 88]

subjects.append("computer science")
grades.append(100)

# Use the zip() function to combine subjects and grades.
# Save this zip object as a list into a variable called gradebook.

gradebook = zip(subjects, grades)

gradebook=gradebook+[("visual arts", 93)]

print(gradebook)

# Your grade for Computer Science class just came in! You got a perfect score, 100!
# After your definitions of subjects and grades but before you create gradebook, use append to add "computer science" to subjects and 100 to grades.

# Your grade for visual arts just came in! You got a 93!
# After the creation of gradebook (but before you print it out), use append to add ("visual arts", 93) to gradebook.


# You also have your grades from last semester, stored in last_semester_gradebook.
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
# Create a new variable full_gradebook with the items from both gradebook and last_semester_gradebook.

full_gradebook = last_semester_gradebook + gradebook