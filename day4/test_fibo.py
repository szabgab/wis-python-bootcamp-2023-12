from fibo import fibonacci

def test_fibonacci_function():
    result = fibonacci(1)
    assert(result == [1])


    result = fibonacci(3)
    assert(result == [1, 1, 2])


def test_fibonacci_function_with_5():
    assert(fibonacci(5) == [1, 1, 2, 3, 5])


# def test_sequence():
#     filename = "seq1.txt"
#     result = compute(filename)
#     assert(result == 8)
    
