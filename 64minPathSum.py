class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
    #timeout
        def minPathPart(grid, x, y):
            if x==0:
                if y==0:
                    return grid[0][0]
                else:
                    return sum(grid[0][0:y+1])
            elif y==0:
                sumcross=0
                for i in range(x+1):
                    sumcross+=grid[i][0]
                return sumcross
            else:
                return min(minPathPart(grid,x-1,y),minPathPart(grid,x,y-1))+grid[x][y]
        
        return minPathPart(grid,len(grid)-1,len(grid[0])-1)

==========================

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[0 for n in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0:
                    if j==0:
                        dp[0]=grid[0][0]
                    else:
                        dp[j]=dp[j-1]+grid[0][j]
                else:
                    if j==0:
                        dp[0]+=grid[i][0]
                    else:
                        dp[j]=min(dp[j-1],dp[j])+grid[i][j]
        
        return dp[j]
