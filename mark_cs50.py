scores = []

for i in range(3):
    score = int(input("Score: "))
    scores.append(score)

average = sum(scores) / len(scores)

print(f"Average: {average}")



#string
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

name = input("Name: ")
print(string_length(name))