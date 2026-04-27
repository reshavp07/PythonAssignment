# 1. Create an empty dictionary to store airport data
# 2. Display the menu options
# Adding to the dictionary: airports[key] = value # Fetch an existing airport
# Check if the code exists in our dictionary

airports = {}

while True:

    print("\n--- Airport System ---")
    print("1: Enter a new airport")
    print("2: Fetch information of an existing airport")
    print("3: Quit")

    choice = input("Choose an option (1, 2, or 3): ")

    if choice == "1":

        icao = input("Enter ICAO code: ").upper()
        name = input("Enter airport name: ")

        airports[icao] = name
        print("Airport saved!")

    elif choice == "2":

        icao = input("Enter ICAO code to search: ").upper()

        if icao in airports:
            print(f"Airport name: {airports[icao]}")
        else:
            print("Airport not found.")

    elif choice == "3":

        print("Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")