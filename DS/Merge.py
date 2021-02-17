#Program to merge two sorted arrays
def Merge(arr1,arr2,n1,n2):
    arr3=[None]*(n1+n2)
    i,j,k=0,0,0

    while i<n1 and j<n2:
        if arr1[i]<arr2[j]:
            arr3[k]=arr1[i]
            k=k+1
            i=i+1
        else:
            arr3[k]=arr2[j]
            k=k+1
            j=j+1
    
    while i<n1:
        arr3[k]=arr1[i]
        i=i+1
        k=k+1
    
    while j<n2:
        arr3[k]=arr2[j]
        j=j+1
        k=k+1

    return arr3

arr1=[2,4,8,10]
arr2=[5,6,7,9,20,40,60]
arr3=Merge(arr1,arr2,len(arr1),len(arr2))
print(arr3)