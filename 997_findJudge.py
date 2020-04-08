class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        inNum = [0]*(N+1)
        outNum = [0]*(N+1)
        for tru in trust:
            outNum[tru[0]] += 1
            inNum[tru[1]] += 1
        
        for i in range(1,N+1):
            if outNum[i] == 0 and inNum[i] == N-1:
                return i
        return -1
