import numpy

# Setting all values to 0 (empty, nothing)
result = 0
height = ""
weight = ""

arr = [18.5, 23, 25]

# Asking What numbers you want using print command
height = input("What is your height?\n")
weight = input("What is your weight\n")

# Setting asked numbers to float, so that it would give an exact answer
floatheight = float(height)
floatweight = float(weight)

# If selected operation is the following then do the following
result = (floatweight / (floatheight * floatheight * 0.01)) * 100

print("Your BMI: " + str(result))

if result < arr[0]:
	print("You underweight\n")

elif (result > arr[0]) & (result < arr[1]):
	print("You normalweight\n")

elif (result > arr[1]) & (result < arr[2]):
	print("You overweight\n")

elif result > arr[2]:
	print("You obesity\n")

else :
	print("Error try again\n")
