# variables
integer0 = int(input("Enter first integer =  "))
integer1 = int(input("Enter second integer =  "))

# operations
difference = integer0 - integer1
product = integer0 * integer1
average = (integer0 + integer1) / 2
distance = abs(integer0 - integer1)
maximum = max(integer0, integer1)
minimum = min(integer0, integer1)

# output
print(str(integer0) + " - " + str(integer1) + " = " + str(difference))
print(str(integer0) + " * " + str(integer1) + " = " + str(product))
print("Average of " + str(integer0) + " and " + str(integer1) + " = " + str(average))
print("Absolute of " + str(integer0) + " - " + str(integer1) + " = " + str(distance))
print("Maximum of " + str(integer0) + " and " + str(integer1) + " = " + str(maximum))
print("Minimum of " + str(integer0) + " and " + str(integer1) + " = " + str(minimum))
