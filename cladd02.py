# Linear Searach
def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return True
    return False


numbers = [4, 8, 15, 16, 23, 42]
n = int(input("Number: "))

if linear_search(numbers, n):
    print("Found")
else:
    print("Not found")


#Bubble sort
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


numbers = [6, 3, 8, 5, 2]
print(bubble_sort(numbers))



#Selection Sort
def selection_sort(numbers):
    n = len(numbers)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers


numbers = [6, 3, 8, 5, 2]
print(selection_sort(numbers))