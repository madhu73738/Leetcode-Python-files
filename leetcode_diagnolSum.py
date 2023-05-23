def diagonalSum(mat):
        l=len(mat)
        a=0
        b=-1
        fin=0
        o=l//2
        for i in range(l):
            
            fin+=mat[i][a]+mat[i][b]
            
            a+=1
            b-=1
        if l%2!=0:
   
            fin-=mat[o][o]
    
        return fin
mat=[[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum(mat))
