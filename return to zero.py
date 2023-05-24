a=27
n="27"
l=[]
c=0
while int(n)!=0:
    l=list(n)
    n= str(int(n)-int(max(l)))
    c+=1
    print(n)
print("count: ",c)
    