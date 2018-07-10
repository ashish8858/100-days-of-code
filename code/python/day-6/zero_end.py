
a=[]
n=int(input("Enter length of Array"))
print("Enter array : ")
for i in range(n):
     x=int(input())
     a.insert(i,x)
     i=i+1
i=0
while i<n:
    j=i
    while j<n:
        if a[i]<a[j]:
            if a[i]==0:
                s=a[i]
                a[i]=a[j]
                a[j]=s
        j=j+1
    i=i+1

for i in range(0,n):
    print(" ",a[i])
