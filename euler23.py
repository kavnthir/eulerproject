def canSum(x):
	for i in abundant:
		if i > x:
			break
		for j in abundant:
			if j > x:
				break
			if x == i+j:
				return True
	return False
sum = 0
abundant = []
for i in range(1,28123):
	for j in range(1,i-1):
		if i%j == 0:
			sum+=j
	if i < sum:
		abundant.append(i)
		print(str(i) + " is abundant")
	sum = 0 

for i in range(28123):
	if not canSum(i):
		sum += i
		print(str(i) + " cannot be summed with abundant numbers")	
print(sum)
					
