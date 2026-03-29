#Design a program that asks the user for their biological gender and hemoglobin level (g/L). Based on the provided values, the program should inform the user if their hemoglobin is low, normal, or high. The normal ranges are:
#For adult females:117-155 g/L.
#For adult males:134-167 g/L.
# 1. Ask for the user's biological gender
# 2. Ask for the hemoglobin level (we will use float for decimals)


gender = input("Enter your biological gender (male/female): ").lower()
if gender == "female":
    hemo_level = float(input("Enter your hemoglobin level (g/L): "))

    if hemo_level < 117:
        print("Your hemoglobin is low.")
    elif hemo_level > 155:
        print("Your hemoglobin is high.")
    else:
        print("Your hemoglobin is normal.")
elif gender == "male":
    hemo_level = float(input("Enter your hemoglobin level (g/L): "))

    if hemo_level < 134:
        print("Your hemoglobin is low.")
    elif hemo_level > 167:
        print("Your hemoglobin is high.")
    else:
        print("Your hemoglobin is normal.")

else:
    print("Invalid input. Please enter 'male' or 'female'.")

