def fibonacci(n):
    if n == 1:
        return [1]
    if n == 2:
        [1, 1]
    numbers = [1, 1]
    for _ in range(2, n):
        # if n == 4:
        #     numbers.append(42)
        numbers.append(numbers[-1] + numbers[-2])
    return numbers
