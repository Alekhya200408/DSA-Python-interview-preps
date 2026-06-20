# Linear Search
# Use it in Unsorted array
'''arr=[12,23,45,70,34]
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            print("Element Found")
            return i
    else:
        print("Element not Found")

linear_search(arr,34)'''

# Binary Search
# Use it in sorted array
'''arr=[10,20,30,40,50]
def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            print("Element Found")
            return mid
        elif arr[mid]<target:
            left=mid+1
            
        else:
            right=mid-1
binary_search(arr,30)'''

# Count occurrences of an element
'''arr=[1,2,2,3,3,3,4,3,5,5,6,7,6,5]
target=int(input("Enter the number you want to count:"))
count=0

for num in arr:
    if num==target:
        count+=1
print(count)'''

# Check if an element exists in an array
'''arr=[1,2,2,3,3,3,4,3,5,5,6,7,6,5]
target=int(input("Enter the number you want to count:"))
is_exist=False

for num in arr:
    if num==target:
        is_exist=True
        break
    
if is_exist:
    print("Exist")
else:
    print("Not Exist")'''
