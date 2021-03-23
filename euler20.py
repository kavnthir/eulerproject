def factorial(n):
    return 1 if n == 1 else n*factorial(n-1)
sum = 0
for i in str(factorial(100)):
    sum+=int(i)
print(sum)
