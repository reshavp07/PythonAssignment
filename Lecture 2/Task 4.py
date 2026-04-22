#Write a program that asks the user to enter a year and tells them whether the year is a leap year. A year is a leap year if:
#It is divisible by 4,and
#If divisible by 100, it must also be divisible by 400
# 1. Ask the user for a year
# Rule: If divisible by 400, it is a leap year
# Rule: If divisible by 100 (but not 400), it is NOT a leap year
# Rule: If divisible by 4 (but not 100), it is a leap year

year = int(input("Enter a year: "))

if year % 400 == 0:
    print(f"{year} is a leap year.")
elif year % 100 == 0:
    print(f"{year} is not a leap year.")
elif year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
