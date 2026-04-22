# Create a tuple containing the days of the week
# Use index (number - 1) because Python starts counting at 0
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# Ask the student for a number
number = int(input("Enter a day number (1-7): "))

# Check if the number is valid
if 1 <= number <= 7:
    # Use index (number - 1) because Python starts counting at 0
    print(f"The corresponding day is: {days[number - 1]}")
else:
    print("Error: Please enter a number between 1 and 7.")



