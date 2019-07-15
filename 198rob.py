class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        n=len(nums)
        if not n:
            return 0
        elif n==1:
            return nums[0]
        else:
            predp=nums[0]#dp[0]
            dp=max(nums[0],nums[1])#dp[1] 2rooms
            for i in range(2,n):#n>2
                predp, dp=dp, max(dp, predp+nums[i])
            return dp
