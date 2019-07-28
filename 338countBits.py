class Solution:
    def countBits(self, num: int) -> List[int]:
        target=[]
        for i in range(num+1):
            target.append(format(i,'b').count('1'))
        return target
