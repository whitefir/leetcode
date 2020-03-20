class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        table = {}
        for num in nums:
            table[num] = 1
        result = []
        for num in range(1, len(nums) + 1):
            if num not in table:
                result.append(num)
        return result  
