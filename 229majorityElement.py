class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts=collections.Counter(nums)
        res=[]
        majs=counts.most_common(2)
        
        for i in majs:
            if i[1]>(len(nums)//3):
                res.append(i[0])
        return res
