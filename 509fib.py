class Solution:
    def fib(self, N: int) -> int:
        i,j=0,1
        while N:
            N-=1
            i,j=j,i+j
        return i
