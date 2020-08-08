class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leng = len(nums)
        i = 0
        for _ in range(leng):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                i -= 1
            i += 1
