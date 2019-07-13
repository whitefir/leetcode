#collections.Counter()
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts= collections.Counter(nums)
        return counts.most_common(1)[0][0]
        
#Boyer-Moore
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        for n in nums:
            if count==0:
                candidate=n
            count+=(1 if n== candidate else -1)
        return candidate
