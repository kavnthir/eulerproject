
def divCheck(x):
    for i in range(2,21):
        if x%i != 0:
            return False
    return True



yeet = False 
i = 2520
while yeet == False:
    if divCheck(i):
        print(i)
        yeet = True
    i += 1
    print(i)

