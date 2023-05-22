def topKFrequent(nums,k) :
        a=set(nums)
        a=list(a)
        b=[]
        c=0
        f=[]
        for i in a:
            c=nums.count(i)
            b.append(c)
        for i in range(k):
            r=b.index(max(b))
            f.append(a[r])
            b.pop(r)
            a.pop(r)
            print(a,b)
        return f
nums=[1,1,1,2,2,3]
k=2
print(topKFrequent(nums,k))
