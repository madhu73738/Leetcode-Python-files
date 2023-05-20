class Solution:
    def numberOfSteps(self, num: int) -> int:
        n=num
        c=0
        while(n>0):
            if n%2==0:
                n=n//2
            else:
                n-=1
            c+=1
        return c
