class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums)<=0: return max(nums)
        maxsum=0
        cursum=0
        for i in nums:
            cursum=cursum+i
            if cursum>0:
                maxsum=max(maxsum,cursum)
            else:
                cursum=0
        return maxsum
