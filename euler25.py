def fib(i):
    return 1 if i <= 1 else fib(i-2)+fib(i-1)
index = 2
while len(str(index)) < 1000:
    index = fib(index)
    print(index)
print(index)ce