print("Welcome to Python!")

name = "Jordan"
age = 22
print("User:", name, "| Age:", age)

a = 15
b = 2.75
c = "Learning Python"
print(type(a), type(b), type(c))

x = 8
y = 4
print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)
print("Quotient:", x / y)

user = "Chris"
print("Hello,", user)

num = 7
if num > 5:
    print("Number is greater than 5")

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

print("Counting:", end=" ")
for i in range(1, 4):
    print(i, end=" ")
print()

count = 1
print("Loop:", end=" ")
while count <= 3:
    print(count, end=" ")
    count += 1
print()

items = ["pen", "book", "eraser"]
print(items)

items.append("pencil")
print(items)

numbers = (1, 2, 3)
print(numbers)

data = {"user": "Mike", "score": 90}
print(data)

def greet(person):
    return "Hello " + person

print(greet("Nina"))

square = lambda n: n * n
print(square(5))

class Animal:
    def __init__(self, name):
        self.name = name

obj = Animal("Dog")
print(obj.name)

class Dog(Animal):
    def sound(self):
        return "Bark"

d = Dog("Bulldog")
print(d.name, d.sound())

try:
    value = 10 / 0
except ZeroDivisionError:
    print("Error: division by zero")

print("File handling example skipped")

import math
print(math.sqrt(25))