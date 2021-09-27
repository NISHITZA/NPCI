dist = 2
val = 1
k = 3
row_val= []
temp=0


for i in range(0,3):
    for m in range(0,3-i):
        print(' ',end='')
    for j in range(0,i+1):
        temp =temp + val
        print(val, end=' ')
    row_val.append(temp)
    temp=0
    print('\n')
    k=k-1
    val = val + dist
for i in row_val:
    print(i)
