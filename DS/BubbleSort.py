def bubble_sort(arr):
    n=len(arr)

    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

n=input("Enter the number of elements in the list: ")
n=int(n)
lst=[]

for i in range(n):
    ele=int(input())
    lst.append(ele)

print("Sorted List is: ")
bubble_sort(lst)
print(lst)