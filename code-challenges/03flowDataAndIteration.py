# This project is completed with data supplied by CA

# Write a function for the cost of ground shipping. This function should take one parameter, weight, and return the cost of shipping a package of that weight.

def getCostOfGroundShipping(weight):
	if weight < 2:
		return 1.5*weight+20
	elif weight > 2 and weight < 6:
		return 3*weight+20
	elif weight > 6 and weight < 10:
		return 4*weight+20
	elif(weight>10):
		return 4.75*weight+20

# should print 53.6 - does print 53.6
print(getCostOfGroundShipping(8.4))

# We will also need to make sure we include the price of premium ground shipping in our code.
# Create a variable for the cost of premium ground shipping.
# Note: this does not need to be a function because the price of premium ground shipping does not change with the weight of the package.

premiumGroundShippingCost = 125

# Write a function for the cost of drone shipping. This function should take one parameter, weight, and return the cost of shipping a package of that weight.

def getCostOfDroneShipping(weight):
	if weight < 2:
		return 4.5*weight
	elif weight > 2 and weight < 6:
		return 9*weight
	elif weight > 6 and weight < 10:
		return 12*weight
	elif(weight>10):
		return 14.25*weight

# should return 6.75 - checks out
print(getCostOfDroneShipping(1.5))

# Using those two functions for ground shipping cost and drone shipping cost, as well as the cost of premium ground shipping, write a function that takes one parameter, weight and prints a statement that tells the user
# The shipping method that is cheapest.
# How much it would cost to ship a package of said weight using this method.

def findCheapestShippingMethod(weight):
	groundShippingCost = getCostOfGroundShipping(weight)
	droneShippingCost = getCostOfDroneShipping(weight)
	if premiumGroundShippingCost<groundShippingCost and premiumGroundShippingCost < droneShippingCost:
		return "Premium Ground Shipping is the cheapest method, it costs "+str(premiumGroundShippingCost)+"."
	elif groundShippingCost<premiumGroundShippingCost and groundShippingCost < droneShippingCost:
		return "Ground Shipping is the cheapest method, it costs "+str(groundShippingCost)+"."
	elif droneShippingCost<premiumGroundShippingCost and droneShippingCost<groundShippingCost:
		return "Drone Shipping is the cheapest method, it costs "+str(droneShippingCost)+"."



# What is the cheapest method of shipping a 4.8 pound package and how much would it cost?
print(findCheapestShippingMethod(4.8))

# What is the cheapest method of shipping a 41.5 pound package and how much would it cost?
print(findCheapestShippingMethod(41.5))













