# Q1
# Step 1: Write names
with open("names.txt", "w") as file:
    for i in range(5):
        name = input(f"Enter name {i+1}: ")
        file.write(name + "\n")

# Step 2: Read and print
with open("names.txt", "r") as file:
    print("\nNames in file:")
    for line in file:
        print(line.strip())



# Q2
# Step 1: Append log
with open("log.txt", "a") as file:
    file.write("Program run successfully\n")

# Step 2: Read logs
with open("log.txt", "r") as file:
    print("\nLogs:")
    print(file.read())




# Q3
numbers = [5, 10, 15, 20, 25]

new_list = [num for num in numbers if num > 15]

print("Filtered list:", new_list)


# Q4
import json

# Step 1: Create dictionary
cities = {
    "Hyderabad": 10000000,
    "Mumbai": 20000000,
    "Chennai": 11000000
}

# Step 2: Save to JSON
with open("cities.json", "w") as file:
    json.dump(cities, file)

# Step 3: Load and print
with open("cities.json", "r") as file:
    data = json.load(file)

print("\nCity Data:")
for city, population in data.items():
    print(city, ":", population)

# Step 4: Add new city
new_city = input("Enter new city: ")
new_population = int(input("Enter population: "))

data[new_city] = new_population

# Step 5: Save updated data
with open("cities.json", "w") as file:
    json.dump(data, file)

print("Updated successfully!")






# Q5
try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")



