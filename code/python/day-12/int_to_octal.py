b=[]
n=int(input("Enter an Integer : "))
k=0
oct=0
while n!=0:
    r=n%8
    b.insert(k,r)
    k=k+1
    n=int(n/8)
print("octal Number = ",end="")
for i in range(k-1,-1,-1):
    oct=(oct*10)+b[i]
print(oct)
