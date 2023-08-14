class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        a=[]
        w=[]
        for i in mat:
            r=i.count(1)
            a.append(r)
        for i in range(k):
            g=a.index(min(a))
            w.append(g)
            a[g]=max(a)+1
        return w