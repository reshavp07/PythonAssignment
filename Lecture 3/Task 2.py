#Design a program that continuously converts inches to centimeters, stopping only when the user enters a negative value.
#Initialize a variable to start the loop
# The loop runs as long as inches is 0 or greater
# 1. Ask the user for the value in inches
# 2. Check if the number is NOT negative before converting
# Calculation: 1 inch = 2.54 cm

inches = 0
while inches >= 0:

    inches = float(input("Enter inches to convert (negative value stops): "))


    if inches >= 0:

        centimeters = inches * 2.54
        print(f"{inches} inches is {centimeters} cm.")
    else:

        print("Negative value entered. Program stopped.")
