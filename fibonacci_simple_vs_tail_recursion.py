import timeit #it'll be used to compare the time execution between both fibonacci functions

#simple
def fibonacci_simple(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
"""for fib_num in fibonacci_simple(10):
    print(fib_num, end=' ') """
#inside the upper comentary lives a code to prove the fibonacci_simple function, just change h
#to the quantity of fibonacci numbers you would like to generate

#tail-recursion
def fibonacci_tail_recursive(n, a=0, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fibonacci_tail_recursive(n - 1, b, a + b)
#here starts the function comparison

simple_time = timeit.timeit(lambda: list(fibonacci_simple(30)), number=1000)

tail_recursive_time = timeit.timeit(lambda: fibonacci_tail_recursive(30), number=1000)

print(f"Simple Fibonacci generator took {simple_time} seconds.")
print(f"Tail-recursive Fibonacci function took {tail_recursive_time} seconds.")

#and here's the optimality proove

if (simple_time>tail_recursive_time):
    print("The fibonacci simple is faster than the tail recursion version")
else:
    print("The fibonacci tail recursion is faster than the simple version")