def tribonacci(n):
        a,b,c=0,1,1
        temp=0
        for i in range(n-2):
            print(a,b,c)
            temp=a+b+c
            a=b
            b=c
            c =temp
            
        return c
    
n=5

print(tribonacci(n))