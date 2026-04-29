🔹 Q1: Write names → read and print

This program writes 5 user-entered names to a file, then reads and prints them.

# Write names
with open("names.txt", "w") as f:
    for i in range(5):
        name = input("Enter name: ")
        f.write(name + "\n")

# Read and print names
with open("names.txt", "r") as f:
    print("Names in file:")
    for line in f:
        print(line.strip())
🔹 Q2: Append log → read all logs

This program adds a log entry and then displays all logs.

# Append log
with open("log.txt", "a") as f:
    f.write("Program run successfully\n")

# Read logs
with open("log.txt", "r") as f:
    print("Log entries:")
    print(f.read())
🔹 Q3: List comprehension (filter > 15)

This creates a new list with numbers greater than 15.

nums = [5, 10, 15, 20, 25]

new_list = [x for x in nums if x > 15]

print("Filtered list:", new_list)
🔹 Q4: JSON (save → load → update)

This stores city data in JSON, reads it, prints it, then updates it.

import json

# Step 1: Create dictionary
cities = {
    "Hyderabad": 10000000,
    "Delhi": 19000000,
    "Mumbai": 20000000
}

# Step 2: Save to JSON
with open("cities.json", "w") as f:
    json.dump(cities, f, indent=4)

# Step 3: Load and print
with open("cities.json", "r") as f:
    data = json.load(f)

print("Cities and populations:")
for city, pop in data.items():
    print(city, ":", pop)

# Step 4: Take user input and update
new_city = input("Enter new city: ")
population = int(input("Enter population: "))

data[new_city] = population

# Step 5: Save updated data
with open("cities.json", "w") as f:
    json.dump(data, f, indent=4)
🔹 Q5: Exception handling (file not found)

This safely handles the case when a file doesn’t exist.

try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
🔥 Final Understanding
w → overwrite file
a → append data
r → read file
with → auto close file
list comprehension → compact filtering
json.dump/load → file handling
try-except → prevents crash