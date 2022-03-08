digi = int(input("Enter your no:"))
num = digi
res = []
print(num)
while num > 0:
    rem = num % 2
    res.append(rem)
    num = num // 2
res = res[::-1]
for i in res:
    print(i,end="")



