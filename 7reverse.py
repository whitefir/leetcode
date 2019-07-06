class Solution:
    def reverse(self, x:int)->int:
        y=abs(x)
        intmax=(1<<31)-1 if x>0 else 1<<31
        re=0
        
        while y>0:
            re=re*10+y%10 
            if re>intmax: 
                return 0
            y//=10
            
        return re if x>0 else -re
