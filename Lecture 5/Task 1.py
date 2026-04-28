# 1. Store the seasons in a tuple
# 2. Ask the user for input and convert it to an integer (a whole number)
# 3. Use logic to find the season


seasons = ("Winter", "Spring", "Summer", "Autumn")


month = int(input("Enter the number of the month (1-12): "))


if month == 12 or month == 1 or month == 2:
    result = seasons[0]              # Winter
elif month >= 3 and month <= 5:
    result = seasons[1]               # Spring
elif month >= 6 and month <= 8:
    result = seasons[2]               # Summer
elif month >= 9 and month <= 11:
    result = seasons[3]               # Autumn
else:
    result = "Invalid month! Please enter a number between 1 and 12."


print(f"Output: {result}")