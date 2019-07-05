class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i,m in enumerate(nums):#num[i]=m
            if dict1.get(target-m) is not None:
                return [dict1.get(target-m), i]
            dict1[m]=i
