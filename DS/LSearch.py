def LSearch(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i+1
    return -1

n=input("Enter the number of elements in the list: ")
n=int(n)
lst=[]

for i in range(n):
    ele=int(input())
    lst.append(ele)

key=int(input("Enter the element you want to search: "))
print(f"The element is present at position {LSearch(lst,key)}")

