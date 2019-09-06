class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        #a<b<c
        for a in range(len(nums)-2):
            #nums[a]
            if (a>0 and nums[a]==nums[a-1]):
                continue
            if nums[a]>0:
                break
            b,c=a+1,len(nums)-1
            while b<c:
                if nums[a]+nums[b]+nums[c]>0 or (c<len(nums)-1 and nums[c]==nums[c+1]):
                    c-=1
                    continue
                if nums[a]+nums[b]+nums[c]<0 or (b>a+1 and nums[b]==nums[b-1]):
                    b+=1
                    continue
                if nums[a]+nums[b]+nums[c]==0:
                    ans.append([nums[a],nums[b],nums[c]])
                    b+=1
                    c-=1
        return ans
                
