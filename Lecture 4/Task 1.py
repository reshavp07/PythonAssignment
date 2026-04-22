# 1. Ask the user for the number of dice
# We use int() because input() always starts as text
# 2. Create a variable to keep track of the total
# 3. Use a for loop to roll the dice one by one
# range(num_dice) tells the loop to run exactly that many times


import random
num_dice = int(input("How many dice do you want to roll? "))


total_sum = 0
#hello

for i in range(num_dice):
    roll = random.randint(1, 6)
    print(f"Roll {i+1}: {roll}")
    total_sum += roll

#hbcd
print("---")
print(f"The total sum of all dice is: {total_sum}")