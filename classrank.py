a = [50,75,45]
b = [45, 50, 45]
c = [75, 80, 90]

fail_list =[]
re_app = []
dist = []
first_div = []
second_dev = []
class_rank =[]

students = []
students.append(a)
students.append(b)
students.append(c)

for i in range(0,len(students)):
    t_sum = 0;
    flag =0;
    for j in range(0,3):
        if(students[i][j]<50):
            flag = flag+1
            t_sum = t_sum + students[i][j];
    if(flag==1):
        re_app.append(students[i])
    if(flag>1):
        fail_list.append(students[i])
    
    class_rank.append(students[i])
    per = (t_sum/300)*100
    
    if(per>80):
        dist.append(students[i])
    elif(per >61 and per <79):
        first_div.append(students[i])
    else: second_dev.append(students[i])
    
    class_rank.sort()

print('Students who failed',fail_list)
print('Students who have to rewrite',re_app)
print('Class rank', class_rank)
print('Distinction', dist)
print('First class',first_div)
print('Second class',second_dev)
