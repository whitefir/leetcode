class Solution:
    def findLucky(self, arr: List[int]) -> int:
        s=collections.Counter(arr)
        re=[-1]
        for i in s.keys():
            if i== s[i]:
                re.append(i)
        return max(re)
