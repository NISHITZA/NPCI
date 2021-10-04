class User:
   def __init__(self,id,bal,pin,txn,limit):
        self.id = id
        self.bal = bal
        self.pin = pin
        self.txn = txn
        self.limit = limit
        
def rounder(amt, cur):
    val = 0
    flag =0
    
    for i in cur.keys():
        cur_count = cur[i]
        
        for j in range(0,cur_count):
            val = val + i 
            cur_count = cur_count - 1
            if(val>amt):
                cur_count= cur_count +1
                val = val - i
                cur[i] = cur_count
                flag = 1 
                break
    return val

def atm():
    cur = {
        100 : 10,
        500 : 5,
        1000 : 2,
    }
    
    total_cur = 0
    u1 = User(1,6000,123,0,0)
    
    for i in cur.items():
        total_cur = total_cur + (i[0]*i[1])
        
    correct_flag = 0
    pin_count = 0
    
    
    while(pin_count<=3 and correct_flag!=1):
        
        upin = int(input('Enter the pin \n'))
        
        if(upin == u1.pin):
            correct_flag =1
            break 
        
        print('Pin Invalid')
        pin_count = pin_count + 1 
        
        
    if(correct_flag == 1 and pin_count<4):
        print('Login successful')
        amt_flag = 0
        
        while(amt_flag!=1):
            amt = int(input('Enter the amount \n'))
            
            if(amt>(0.9*total_cur)):
                print('Amount too high , enter again')
                continue
            
            if(amt>u1.bal):
                print('Balance is low')
                continue
            
            if(u1.txn>5000):
                print('Daily limit reached')
                break
            
            if(u1.limit >2):
                print('Daily limit reached')
                break
            
            value_drawn = rounder(amt, cur)
            print('Amount drawn '+str(value_drawn))
            amt_flag = 1
            u1.txn = u1.txn + amt
            u1.limit = u1.limit + 1
    else:
        print('User account locked')
    
    print('Thank you')

atm()
