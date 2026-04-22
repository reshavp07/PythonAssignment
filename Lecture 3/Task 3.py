#Write a program that prompts the user to enter numbers until they leave the input blank. Once the input stops, the program outputs the smallest and largest numbers entered.
# Create empty variables to store our extremes
# Check if the user left the input blank
# Convert the text input into an actual number (integer)
# After the loop finishes, show the results


largest = None
smallest = None

print("Enter numbers (leave blank and press Enter to stop):")

while True:
    user_input = input("Enter a number: ")


    if user_input == "":
        break


    num = int(user_input)


    if largest is None or num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num


print("Largest number:", largest)
print("Smallest number:", smallest)