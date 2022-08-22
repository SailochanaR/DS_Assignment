import random  
def quicksort(arr,l,r):
    if l>=r: 
        return
    #left part and right part of list
    p = partition(arr,l,r)
    quicksort(arr,l,p-1)
    quicksort(arr,p+1,r)
    
    
def partition(arr,l,r):
    p = random.randint(l,r)
    arr[r],arr[p] = arr[p],arr[r]
    for j in range(l,r):
        if arr[r]+arr[j]<arr[j]+arr[r]:
            arr[l],arr[j] = arr[j],arr[l]
            l+=1
            arr[l],arr[r] = arr[r],arr[l]
    return l
    
    
ar = [5,7,2,19,3,9,1] 
n = len(ar) 
quicksort(ar,0,n-1) 
for i in range(n): 
    print (ar[i],end=" ")