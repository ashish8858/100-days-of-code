import sys
def minheap(arr,i,n):

    left= 2*i + 1
    right = 2*i + 2
    small= i
    if left< n and arr[left] < arr[i]:
        small= left
    if right < n and arr[right] < arr[small]:
        small= right
    if small!= i:
        temp=arr[i]
        arr[i]=arr[small]
        arr[small]=temp
        minheap(arr, small, n)

def buildmin(arr,n):
    t=int((n-2)/2)
    for i in range(t,-1,-1):
        minheap(arr, i, n)





arr=[]
lim=int(input("Enter length of Array : "))
print("Enter Array : ")
for i in range(lim):
    x=int(input())
    arr.insert(i,x)
print("Max Heap array : ")
for i in  range(lim):
    print(arr[i],end=" ")
buildmin(arr, lim)
print("")
print("Min Heap array : ")
for i in  range(lim):
    print(arr[i],end=" ")
