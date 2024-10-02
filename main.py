def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# Number of terms in the Fibonacci series
num_terms = 10

# Generate the Fibonacci series
fib_series = fibonacci(num_terms)

# Print the Fibonacci series
print("Fibonacci series:", fib_series)
