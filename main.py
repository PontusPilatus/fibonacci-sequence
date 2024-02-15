def fibonacci(n):
    sequence = []

    a, b = 0, 1
    sequence.append(a)

    for _ in range(n - 1):
        sequence.append(b)
        a, b = b, a + b

    return sequence


num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

fib_sequence = fibonacci(num_terms)
print("Fibonacci Sequence:", fib_sequence)
