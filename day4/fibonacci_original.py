import sys

# 1, 1, 2, 3, 5, 8, 13 ...


numbers = [1]
print(numbers)


...

...


numbers = [1, 1]
for _ in range(2, 10):
    numbers.append(numbers[-1] + numbers[-2])
print(numbers)

...
...



numbers = [1, 1]
for _ in range(2, 7):
    numbers.append(numbers[-1] + numbers[-2])
print(numbers)
