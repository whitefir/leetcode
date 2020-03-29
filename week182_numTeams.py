class Solution:
    def numTeams(self, rating: List[int]) -> int:
        nums=len(rating)
        count=0
        for left in range(nums-2):
            for right in range(nums-1,left+1,-1):
                for mid in range(left+1,right):
                    if (rating[left]<rating[mid] and rating[mid]<rating[right]) or (rating[left]>rating[mid] and rating[mid]>rating[right]):
                        count+=1
        return count
