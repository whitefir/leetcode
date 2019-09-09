class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts= collections.Counter(nums)
        ans=[]
        for i in counts.most_common(k):
            ans.append(i[0])
        return ans
