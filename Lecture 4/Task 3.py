# 1. Get input from the user
# 2. Assume the number is prime until proven otherwise and # Prime numbers must be greater than 1
# 3. Check every number from 2 up to (but not including) our number and If the remainder is 0, it's not prime!



number = int(input("Enter an integer: "))

is_prime = True

if number <= 1:
    is_prime = False
else:

    for i in range(2, number):
        if number % i == 0:

            is_prime = False
            break

if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")