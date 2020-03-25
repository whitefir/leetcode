class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left=1
        right=0
        sort=sorted(nums)
        for i in range(len(nums)):
            if nums[i]!=sort[i]:
                left=i+1
                break
        for j in range(len(nums)-1,-1,-1):
            if nums[j]!=sort[j]:
                right=j+1
                break
        return right-left+1
