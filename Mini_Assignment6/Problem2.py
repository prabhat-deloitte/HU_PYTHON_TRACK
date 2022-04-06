def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        a, b = b, a + b


for x in fib(10):
    print(x)
