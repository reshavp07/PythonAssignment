#Create a program using a while loop that prints all numbers divisible by three within the range of 1 to 1000.
# Start our counter at 1
# Keep running the loop as long as number is 1000 or less
# Check if the number is divisible by 3

number = 1

# Keep running the loop as long as number is 1000 or less
while number <= 1000:
    if number % 3 == 0:
        print(number)

    number += 1
