# Create an empty set # Start a loop that runs until we tell it to stop
# If the user enters nothing, 'break' exits the loop
# Check if the name is already in the set    # Add the name to the set

names_set = set()

while True:
    name = input("Enter a name: ")
    if name == "":
        break
    if name in names_set:
        print("Output: Existing name")
    else:
        print("Output: New name")

        names_set.add(name)

print("\nFinal Output:")
for n in names_set:
    print(n)