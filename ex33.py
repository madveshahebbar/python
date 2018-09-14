#EX33 - While Loops
i = 0
m = 6
numbers = []

while i < m:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers:")

for num in numbers:
    print(num)
