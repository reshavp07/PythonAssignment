# 1. Create an empty list to store the numbers
# 2. Check if the input is an empty string
# 3. Convert input to an integer and add it to our list
# 4. Sort the list in descending order (highest to lowest)

numbers = []
#hbcd


print("Enter numbers one by one. Press Enter without typing anything to quit.")

while True:
    user_input = input("Enter a number: ")


    if user_input == "":
        break

    number = int(user_input)
    numbers.append(number)

numbers.sort(reverse=True)

top_five = numbers[:5]

print("\nThe five greatest numbers are:")
print(top_five)