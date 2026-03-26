#Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to kilograms and grams and outputs the result to the user.?
#**Conversions:**
#- One talent = 20 pounds.
# One pound = 32 lots.
#- One lot = 13.3 grams.

talents = float(input("Enter the talents: "))
pounds = float(input("Enter the pounds: "))
lots = float(input("Enter the lots: "))
total_lots = (talents * 20 * 32) + (pounds * 32) + lots
total_grams = total_lots * 13.3
kilograms = int(total_grams // 1000)
grams = total_grams % 1000
print("The weight in  modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams")


