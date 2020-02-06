class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        res = []
        for i in words:
            setx = set(i.lower())
            if setx<=set1 or setx<=set2 or setx<=set3:
                res.append(i)
        return res
