class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
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
            
