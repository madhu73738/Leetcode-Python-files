#Count and display the number of vowels, consonants, uppercase, lowercase
#characters in string.

x=input("enter:")
a=['a','e','i','o','u','A','E','I','O','U']
l=0
r=0
for i in x:
    for f in a:
       if i==f:
            l=l+1
print('\n''there are :',l, 'vowels...')
for i in x:
           if i!=a:
            r=r+1
print('\n''there are :',r, 'consonants...')

'''
s=input("Enter string:")
c=0
j=0
for i in s:
      if(i.islower()):
            c=c+1
      elif(i.isupper()):
            j=j+1
print("The number of lowercase characters is:",c)

print("The number of uppercase characters is:",j)
'''