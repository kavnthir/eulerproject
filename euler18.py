"""
data = [
[3],
[7,4],
[2,4,6],
[8,5,9,3],
]
"""

data = [
[75], #0
[95,64], #1 
[17,47,82], #2
[18,35,87,10], #3
[20,4,82,47,65], #4
[19,1,23,75,3,34], #5
[88,2,77,73,7,63,67], #6
[99,65,4,28,6,16,70,92], #7
[41,41,26,56,83,40,80,70,33], #8
[41,48,72,33,47,32,37,16,94,29], #9
[53,71,44,65,25,43,91,52,97,51,14], #10
[70,11,33,28,77,73,17,78,39,68,17,57], #11
[91,71,52,38,17,14,91,43,58,50,27,29,48], #12
[63,66,4,68,89,53,67,30,73,16,69,87,40,31], #13
[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23], #14
]


""" Incorrect Method
sum = 75
j=0
print(sum)
for i in range(14):
    if max(big_triangle[i+1][j],big_triangle[i+1][j+1]) == big_triangle[i+1][j+1]:
        j+=1 
    sum+=big_triangle[i+1][j]
    print("choice: "+str(big_triangle[i+1][j])+", sum: "+str(sum))
print(sum)
"""

def sum_greatest_path(i,j):
    if i == len(data)-2:
        return data[i][j]+ max(data[i+1][j],data[i+1][j+1])
    return data[i][j]+ max(sum_greatest_path(i+1,j),sum_greatest_path(i+1,j+1))
print(sum_greatest_path(0,0))