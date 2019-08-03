class Solution:
    def countSubstrings(self, s: str) -> int:
        def countCenter(s,l,r)-> int:
            countC=0
            while (l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
                countC+=1
            return countC
        
        count=0
        for i in range(len(s)):
            count+=countCenter(s,i,i)+countCenter(s,i,i+1)
        return count
        
#Manacher
