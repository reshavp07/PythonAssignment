# 1. Create an empty list to store the city names
# 2. Use a for loop to ask for 5 names and range(5) will repeat the code inside 5 times
# 3. Use a for/in loop to iterate through the list
cities = []


for i in range(5):
    city_name = input("Enter the name of a city: ")
    cities.append(city_name)
print("\nHere are the cities you entered:")
for city in cities:
    print(city)