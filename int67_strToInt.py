class Solution:
    def strToInt(self, str: str) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        s= str.strip()
        res = re.compile(r'^[\+\-]?\d+')
        num = res.findall(s)
        nums = int(*num)
        return max(min(nums, INT_MAX), INT_MIN)
