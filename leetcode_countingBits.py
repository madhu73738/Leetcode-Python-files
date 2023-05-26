class Solution:
    def countBits(self, n: int) -> List[int]:
        a=[]
        
        for i in range(n+1):
            b=bin(i)

            r=str(b)[2:].count('1')
            a.append(r)

        return a