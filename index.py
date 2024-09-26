import csv

# Data to be written to the CSV
header = ["Name", "Age", "City"]
data = [
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"],
]

# Create and write to a CSV file
with open("people.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(header)

    # Write the data rows
    writer.writerows(data)

print("CSV file created successfully!")
