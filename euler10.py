def check_prime(x):
    if x==1:
        return False
    if x==2:
        return True
    for i in range(2,x):
        if x%i == 0:
            return False
    return True
sum = 0
for i in range(2000000):
    if check_prime(i):
        print(i)
        sum+= i
print(sum) 
#range(10) = 17
#range(100) = 1060
#range(2000000) = 142913828922