class Solution:
    def hammingWeight(self, n: int) -> int:
        b=n
        rem=0
        while (b>0):
            if b%2==1:
                rem+=1
            b=b//2
        return rem