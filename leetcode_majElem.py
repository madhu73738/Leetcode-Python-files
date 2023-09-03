class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        r=[]
        b=list(set(nums))
        for i in b:
            d=nums.count(i)
            r.append(d)
        a=len(nums)/2
        return b[r.index(max(r))]
           