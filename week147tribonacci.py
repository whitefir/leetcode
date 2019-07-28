class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c=1,1,0#a>b>c
        if n==0: return 0
        for i in range(1,n):
            a,b,c=a+b+c,a,b
        return b
