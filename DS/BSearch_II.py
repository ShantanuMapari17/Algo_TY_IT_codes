def binary_search(arr,x):
    low=0
    high =len(arr)-1
    mid=0

    while low<=high:
        mid=(high+low)//2

        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1
    
    #if ele not present in the list then return -1
    return -1

n=input("Enter the number of elements in the list: ")
n=int(n)
lst=[]

for i in range(n):
    ele=int(input())
    lst.append(ele)

key=int(input("Enter the element you want to search: "))
print(f"The element is present at position {binary_search(lst,key)}")