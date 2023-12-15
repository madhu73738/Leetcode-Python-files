class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r=[]
        a,f,b=1,1,1
        if nums.count(0)==1:
            for i in nums:
                if i!=0:
                    f*=i 

            for i in nums:
                if i==0 :
                    b=f
                else:    
                    b=0
                r.append(b)
           
            return r
        else:
            for i in nums:
                a*=i 
            
            for i in nums:
                if i==0 :
                    b=0
                else:    
                    b=a//i
                r.append(b)
        
        return r