
# CS50P - Lecture 6
# File I/O and CSV
names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names):
    print(f"Hello, {name}")


# ---------- Writing to a Text File ----------
name = input("What's your name? ")

with open("students.txt", "a") as file:
    file.write(f"{name}\n")


# ---------- Reading a CSV File ----------
import csv

students = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append({
            "name": row["name"],
            "house": row["house"]
        })

for student in sorted(students, key=lambda s: s["name"]):
    print(f"{student['name']} from {student['house']}")


# ---------- Writing to a CSV File ----------
name = input("Name: ")
house = input("House: ")

with open("new_students.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])

    writer.writerow({
        "name": name,
        "house": house
    })

print("Student added successfully!")