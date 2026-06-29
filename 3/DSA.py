# Bubble Sort
# time complexity O(n) best ,worst O(n²)
'''def bubble(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr
arr=[10,20,32,34,30,40,50]

print(bubble(arr))
'''
# Selection Sort
# O(n²)

def selection(arr1):
    n=len(arr1)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr1[j]<arr1[mini]: 
                mini=j
        arr1[i],arr1[mini]=arr1[mini],arr1[i]

arr1=[32,44,53,33,24]
selection(arr1)
print("Sorted array is:",arr1)
# We choose accending and descending on the basis of < and > sign