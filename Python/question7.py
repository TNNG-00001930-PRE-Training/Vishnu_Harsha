#Program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
str1=[]
for i in range(1000,3001):
    str_num=str(i)
    even=True
    for digit in str_num:
        if (int(digit))%2!=0:
            even=False
            break
    if even:
        str1.append(str_num)
print(",".join(str1))