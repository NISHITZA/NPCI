b = [1,2,5,6]

step = [] 
final_step = 1

for i in range(0,len(b)-1):
    temp = b[i+1]-b[i];
    step.append(temp)

step.sort()
for i in range(0,len(step)-1):
    if(step[i]==step[i+1]):
        final_step = step[i]
        break

print(final_step)

missing_values = []

for j in range(0,len(b)-1):
    temp = b[j] + final_step;
    if(b[j+1]!=temp):
        missing_values.append(temp)
        
print(missing_values)
    
