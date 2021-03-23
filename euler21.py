from functools import lru_cache
@lru_cache(maxsize=10000)
def find_divisors_sum(n):
    divisiors = [1]
    for i in range(2,n):
        if n%i == 0:
            divisiors.append(i)
    return sum(divisiors)
amicable = []
print_toggle = False
for i in range(10000):
    for j in range(10000):
        if find_divisors_sum(i) == j and find_divisors_sum(j) == i and i != j:
            amicable.append(i)
            if print_toggle:
                print(amicable[-2:])
                print_toggle = False
            else:
                print_toggle = True
            
print("Answer: "+str(sum(amicable)))
