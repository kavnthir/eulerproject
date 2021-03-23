index = 1
count = 1
def primeCheck(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2,x):
        if x%i == 0:
            return False
    return True
while count <= 10001:
    if primeCheck(index):
        print("prime:"+str(index)+", rank:"+str(count))
        count += 1
    index += 1