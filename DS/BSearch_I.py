#Recursive function for binary search:
def binary_search(arr,low,high,x):
    if high>=low:
        mid=(high+low)//2
        if arr[mid]==x: #if the ele present at the middle return it
            return mid

        elif arr[mid]>x:
            return binary_search(arr,low,mid-1,x)
        
        else:
            return binary_search(arr,mid+1,high,x)
    
    #if element not present in the list return -1
    else:
        return -1

n=input("Enter the number of elements in the list: ")
n=int(n)
lst=[]

for i in range(n):
    ele=int(input())
    lst.append(ele)

key=int(input("Enter the element you want to search: "))
print(f"The element is present at position {binary_search(lst,0,n,key)}")
