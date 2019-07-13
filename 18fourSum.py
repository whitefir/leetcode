class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=set()
        numlen=len(nums)
        
        for nmin in range(numlen-3):#nums[nmin]
            if target<nums[nmin]+nums[nmin+1]+nums[nmin+2]+nums[nmin+3]:
                break
            if target>nums[nmin]+nums[numlen-1]+nums[numlen-2]+nums[numlen-3]:
                continue
            
            for tmp in range(nmin+1,numlen-2):#nums[tmp]
                if target<nums[nmin]+nums[tmp]+nums[tmp+1]+nums[tmp+2]:
                    break
                if target>nums[nmin]+nums[tmp]+nums[numlen-1]+nums[numlen-2]:
                    continue
                
                left=tmp+1
                right=numlen-1
                while left<right:
                    sums=nums[nmin]+nums[tmp]+nums[left]+nums[right]
                    if sums==target:
                        ans.add((nums[nmin],nums[tmp],nums[left],nums[right]))
                        left+=1
                        right-=1
                    elif sums<target:
                        left+=1
                    else:
                        right-=1
                        
        res=[]
        for i in ans:
            res.append(list(i))
        return res
