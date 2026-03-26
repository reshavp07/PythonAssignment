#Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of all four sides?
#ask the user for input
#We will use float() so that user can enter decimals (like 2.7)
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print("Results:")
print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter}")




