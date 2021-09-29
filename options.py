
a= []
mdict = {'1':'1', '3':'3','2':'2'}
mlist = []

print('1.Add new element to the list')
print('2.Create dict from list')
print('3.Sort dict based on descending order')

n = int(input('Enter choice \n'))

if(n==1):
    
    print('Enter element to be inserted');
    val = int(input())
    a.append(val)
    print('the updated list is ',a)

elif (n==2):
    print('Enter the list ')
    mlist = list(map(int,input()))
    
    for i in range(0,len(mlist)):
        mdict[mlist[i]] = mlist[i]
    
    print('the dict is ', mdict)  

elif(n==3):
    sort_dict = sorted(mdict)
    
    print(sort_dict)
        
    

    
