
def num_of_divisors(x):
    div_count = 0 
    for i in range(1,int(x**.5)+1):
        if x%i == 0:
            div_count += 2
            if int(x**.5) == i:
                div_count-=1
    return div_count
index = 1 
sequence = 1 
while num_of_divisors(sequence) < 500:
    sequence += index+1
    index+=1
    print(sequence)
print("Answer: "+str(sequence))