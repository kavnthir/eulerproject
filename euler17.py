def zero_to_teens(n):
    nums = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    return nums[n]
def twenty_to_ninety(n):
    nums = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety',]
    num = nums[int(str(n)[0])]
    if int(str(n)[-1]) > 0:
        num += zero_to_teens(int(str(n)[-1]))
    return  num
def hundred_to_thousand(n):
    if n==1000:
        return "onethousand"
    elif int(str(n)[1:]) == 0:
        num = zero_to_teens(int(str(n)[0])) + "hundred"
    elif int(str(n)[1:]) > 19:
        num = zero_to_teens(int(str(n)[0])) + "hundredand" + twenty_to_ninety(int(str(n)[1:]))
    else:
        num = zero_to_teens(int(str(n)[0])) + "hundredand" + zero_to_teens(int(str(n)[1:]))
    return num
def num_to_word(n):
    if  n >= 100:
        return hundred_to_thousand(n)
    elif n>= 20:
        return twenty_to_ninety(n)
    else:
        return zero_to_teens(n)
    print(len(string))
string=""
for i in range (1,1001):
    string += num_to_word(i)
    print(len(string))