class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dict1= dict(collections.Counter(arr1))
        res=[]
        for i in arr2:
            for t1 in range(dict1[i]):
                res.append(i)
            del dict1[i]
        k=list(dict1.keys())
        for j in sorted(k):
            for t2 in range(dict1[j]):
                res.append(j)
        return res
