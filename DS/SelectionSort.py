def SelSort(arr):
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[min_idx]>arr[j]:
                min_idx=j
        temp=arr[i]
        arr[i]=arr[min_idx]
        arr[min_idx]=temp
    
n=input("Enter the number of elements in the list: ")
n=int(n)
lst=[]

for i in range(n):
    ele=int(input())
    lst.append(ele)

print("Sorted List is: ")
SelSort(lst)
print(lst)
