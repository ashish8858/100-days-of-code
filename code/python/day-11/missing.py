a=[]
n=int(input("Enter length of Array : "))
print("Enter Array : ")
for i in range(n):
    x=int(input())
    a.insert(i,x)
m=0
f=0
for i in range(n):
    if m==a[i]:
        m=m+1
    else:
        f=1
        print("Missing Element = ",m)
        break
if f==0:
    print("Missing Element = ",m)
