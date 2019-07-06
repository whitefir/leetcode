class Solution:
    def lengthOfLongestSubstring(self, s: str)->int:
        n=len(s)
        set1=set()
        ans=0
        left=0
        right=0
        while left<n and right<n:
            if s[left] in set1:
                set1.remove(s[right])
                right+=1
            else:
                set1.add(s[left])
                left+=1
                ans=max(ans, left-right)
        return ans
