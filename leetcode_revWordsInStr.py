def reverseWords(s):
        s=s.strip()
        a=s.split(" ")
        l=len(a)
        b=""
        print(s,a)
        for i in reversed(range(l)):
            if a[i]!='':    
                b+=(a[i].strip())
                if i==0:
                    return b
                b+=' '
        return b




s= "have   a good day"
print(reverseWords(s))