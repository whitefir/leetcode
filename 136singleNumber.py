class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set1=set(nums)
        return sum(set1)*2-sum(nums)
