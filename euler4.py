drome = 0
for i in range(999):
    for j in range(999):
        if str(i*j) == (str(i*j)[::-1]):
            if i*j > drome:
                drome = i*j
print(drome)
            