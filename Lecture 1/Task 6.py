#Write a program that generates two random combinations of numbers for a combination lock:
# A 3-digit code where each number is between 0 and 9.
# A 4-digit code where each number is between 1 and 6.
import random
val1 = random.randint( 0, 9)
val2 = random.randint( 0,  9)
val3 = random.randint( 0,  9)
print(f"{val1}{val2}{val3}")

value1 = random.randint ( 1,   6)
value2 = random.randint ( 1,  6)
value3 = random.randint ( 1,  6)
value4 = random.randint ( 1,  6)
print(f"{value1}{value2}{value3}{value4}")
