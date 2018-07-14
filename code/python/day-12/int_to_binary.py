b=[]
f=1
n=int(input("Enter an Integer : "))
if n<0:
    f=0
k=0
bin=0
while n!=0:
    r=n%2
    b.insert(k,r)
    k=k+1
    n=int(n/2)
print("Binary Number = ",end="")
for i in range(k-1,-1,-1):
    bin=(bin*10)+b[i]
if f==0:
    bin=bin-(2*bin)
print(bin)
