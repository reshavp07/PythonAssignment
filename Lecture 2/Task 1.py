#Write a program that prompts a fisher for the length of a zander in centimeters. If the zander is below the legal size limit, the program should instruct the fisher to release it back into the lake and tell them how many centimeters short the fish is of the limit. A zander must be at least 42 centimeters long to be kept.
#Ask the user for the length of the zander
#we will use float() because the length might have decimals(like 41.5)
#Legal Limit = 42 centimeters
#check the length of the zander
#calculate how many centimeters the zander is in centimeters
from shapely.set_operations import difference

length = float(input("Enter the lenght of the zander in centimeters: "))
limit = 42
if length < limit:
    difference = limit - length
    print("The zander is below the limit length.")
    print("Please release it back into the lake.")
    print("It is", difference, "centimeters short.")
else:
    print("You can keep the zander.")



