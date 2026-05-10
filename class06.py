# SET EXAMPLE
words = set()

while False:
    word = input("Word: ").lower()
    if word in words:
        print("Duplicate")
    else:
        words.add(word)


# GLOBAL KEYWORD
balance = 0

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

deposit(100)
withdraw(50)
print("Balance:", balance)


# CONSTANTS
MEOWS = 3

for _ in range(MEOWS):
    print("meow")


# TYPE HINTS
def meow(n: int) -> str:
    return "meow\n" * n

print(meow(2), end="")


# ARGPARSE
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", default=1, type=int)

args = parser.parse_args([])

for _ in range(args.n):
    print("meow")


# UNPACKING
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins))


# MAP
students = ["Hermione", "Harry", "Ron"]

gryffindors = map(str.upper, students)

print(list(gryffindors))


# LIST COMPREHENSION
students = ["Hermione", "Harry", "Ron"]

gryffindors = [student.upper() for student in students]

print(gryffindors)


# FILTER
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in gryffindors:
    print(gryffindor["name"])


# DICTIONARY COMPREHENSION
students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)


# ENUMERATE
students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students, start=1):
    print(i, student)