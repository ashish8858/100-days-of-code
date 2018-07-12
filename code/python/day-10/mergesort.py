def merge(arr, l, m, r):
    n1 = int(m - l + 1)
    n2 = int(r- m)
 
    L = []
    R = []
 
    for i in range(n1):
        L.insert(i,arr[l + i])
 
    for j in range(n2):
        R.insert(j,arr[m+1+j])
 
    i = 0     
    j = 0    
    k = l   
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i =i+ 1
        else:
            arr[k] = R[j]
            j =j+ 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i =i+ 1
        k =k+ 1
    while j < n2:
        arr[k] = R[j]
        j =j+ 1
        k =k+ 1
def mergeSort(arr,l,r):
    if l < r:
        m =int((l+(r-1))/2)
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
 
arr = []
n =int(input("Enter Length of Array : "))
print ("Enter array : ")
for i in range(n):
    x=int(input())
    arr.insert(i,x)
mergeSort(arr,0,n-1)
print ("Sorted array is")
for i in range(n):
    print ("  ",arr[i])