import sys

# 1, 1, 2, 3, 5, 8, 13 ...

def fibonacci(n):
    if n == 1:
        return [1]
    if n == 2:
        [1, 1]
    numbers = [1, 1]
    for _ in range(2, n):
        numbers.append(numbers[-1] + numbers[-2])
    return numbers

print(fibonacci(1))
...
print(fibonacci(10))
...
print(fibonacci(7))
