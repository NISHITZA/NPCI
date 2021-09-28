d = {'One': 'One', 'Two': 'Two', 'Five':'Five'}

temp =[]
for i in d.values():
    temp.append(i)

result = { }
#temp.sort()
#print(temp)

for i in range(0,len(temp)):
    for j in range(0,len(temp)-i-1):
        if(temp[j]>temp[j+1]):
            val = temp[j]
            temp[j] = temp[j+1]
            temp[j+1] = val 

print(temp)

for i in temp:
    for j in d.items():
        if( i == j[1]):
            result[j[0]] = j[1]

print(result)
    
           



#print(temp)
    

#print(d)
