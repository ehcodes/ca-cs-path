# for loops:
	# for -onject- in -sequence-:
	# 	do a thing or twenty
	# straightforward for in loop
	# iterates through sequences, can do something to each onject in the sequence.
	# EX:
cities_and_towns=['Boston','Malden','Southbridge','West Haven','Warwick','Brockton', 'Philadelphia']
for obj in cities_and_towns:
	print("I've lived in "+str(obj)+" before.")
# This for loop will iterate through this sequence and state that I've lived in the city/town next up in the sequence.
# Since python's for loop isn't like js and specifically targets the objects within the sequence, to get a counter and to avoid being tied to iterating through a specific sequence, range() is often used.
for obj in range(2):
	print('This will print 2 times')

# It's possible to create an infinite loop. If you keep making the list being iterated through larger, you'll never reach the end.
for number in imagined_list:
  imagined_list.append(number)

# break can be used to exit a loop
for number in imagined_list:
  print(number)

# continue can be used to avoid having to do anything with some objects in the sequence being looped through.
# In the example below, any objects less than 141 won't be printed.
for obj in sequence:
  if obj < 141:
    continue
  else:
    print(obj)

# while loops

all_orangutans = ["Al", "Edward", "Riza", "Hawkeye", "Lina", "Freezing", "Roy", "Mustang", "Full Metal"]
orangutans_freed = []

while len(all_orangutans)<6:
  temp = all_orangutans.pop()
  orangutans_freed.append(temp)
print(orangutans_freed)

# while condition is true:
	# do the stuff here

# The pop method (sequence.pop()) is used to remove an item from a sequence.
# .pop(index) takes one argument (the index number of the object we wish to remove from the sequence).
# if .pop() isn't given an argument it will remove the last item from the list.
people = ['person1','person2','person3','person4']
person4=people.pop()

# list comprehensions
# shorthand way of creating lists, you can avoid first creating an empty list by using list comprehensions.
# The two code snippets below do the same thing - they create a list called greetings pulled from the list words.

for word in words:
  if word[0] == 'hello':
    usernames.append(word)

greetings = [word for word in words if words[0] == 'hello']










































