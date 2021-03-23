def collatz_seq(n):
    length = 0
    while n != 1:
        if n%2 == 0:
            n/=2
        else:
            n = 3*n + 1
        length += 1
    return length
highest = 0
for i in range(2,1000000):
    if collatz_seq(i) > highest:
        highest = collatz_seq(i)
        print("length: "+str(highest) + ", num:"+ str(i))
