#Create a program that asks the user to input the cabin class on a cruise ship and prints the corresponding description based on the following list:
#LUX: Upper-deck cabin with a balcony.
#- **A**: Cabin above the car deck with a window.
#-**B**: Windowless cabin above the car deck.
#- **C**: Windowless cabin below the car deck.
#You must use a**if**/**elif**/**else**structure in your solution. If the user inputs an invalid class, the program should output:Invalid cabin class`.
# Ask the user for their cabin class


cabin_class = input("Enter the cabin class (LUX, A, B, or C): ").upper()

if cabin_class == "LUX":
    print("LUX: Upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("A: Cabin above the car deck with a window.")
elif cabin_class == "B":
    print("B: Windowless cabin above the car deck.")
elif cabin_class == "C":
    print("C: Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

