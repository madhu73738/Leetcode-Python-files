class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        a=n
        p=0
        while(True):

            if a==2**p:
                return True
            
            elif a<(2**p):
                return False
            p+=1
    isPowerOfTwo(16)