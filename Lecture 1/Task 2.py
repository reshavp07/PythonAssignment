#Write a program that asks the user for the radius of a circle and then prints out the area with two decimals of the circle?
# Ask the user for the radius
#We use float() because the radius could be decimal (like 5.2)
#Calculate the area using formula Area = π(3.14/math.pi) * r^2

import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)
print (f"The area of the circle is:{area:.2f}")

