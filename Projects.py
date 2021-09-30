class User:

    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary

class Project:
    
    def __init__(self, pid, pname, users):
        self.pid = pid
        self.pname = pname
        self.users = users
        
    def sort_project(self):
        
        for i in range(0,len(self.users)):
            for j in range(0,len(self.users)-i-1):
                
                if(self.users[j].salary > self.users[j+1].salary):
                    temp = self.users[j]
                    self.users[j] = self.users[j+1]
                    self.users[j+1] = temp
                    
    def display_users(self):
        for i in range(0,len(self.users)):
            print('The user name ' +self.users[i].name+ 'The user salary '+str(self.users[i].salary))
        
u1 = User('1', 'A', 1000)
u2 = User('2', 'B', 500)
u3 = User('3', 'C', 1500)

p1 = Project('10','P1',[u1,u2,u3])
p1.sort_project()

print(p1.display_users())


    
        
