#Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers?
#Ask the user for three integers numbers
No1 = int(input("Enter the first number: "))
No2 = int(input("Enter the second number: "))
No3 = int(input("Enter the third number: "))
sum_result = No1 + No2 + No3
product_result = No1 * No2 * No3
average_result = sum_result / 3
print("--- Results ---")
print(f"Sum: {sum_result}")
print(f"Product: {product_result}")
print(f"Average: {average_result:.3f}")

