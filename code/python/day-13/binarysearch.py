a=[]
n=int(input("Enter length of Array : "))
print("Enter Array")
f=0
for i in range(n):
    x=int(input())
    a.insert(i,x)
s=int(input("Enter Search Element : "))
l=0
r=n-1
while l<=r:
    m=int((l+r)/2)
    if a[m]==s:
        print("Element found")
        f=1
        break
    if a[m]<s:
        l=m+1
    if a[m]>s:
        r=m-1
if f!=1:
    print ("Element not found")