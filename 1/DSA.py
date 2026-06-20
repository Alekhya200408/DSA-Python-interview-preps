# ARRAY
arr=[10,23,30,45,49,50]

# printing
'''for i in arr:
    print(i)'''

# max
'''max=arr[0]
for i in arr:
    if i>max:
        max=i
print(max)
'''

# min
'''min=arr[0]
for i in arr:
    if i<min:
        min=i
print(min)
'''

# sum
'''total=0
for i in arr:
    total+=i
print(total)'''

#  Avarage
'''total=0
for i in arr:
    total+=i
avg=total/len(arr)
print(avg)'''

# count even
'''for i in arr:
    if i%2==0:
        print("Even numbers are",i)'''

# odd numbers
'''for i in arr:
    if i%2!=0:
        print("Odd numbers are:",i)'''

# reverse array
'''for i in range(len(arr)-1,-1,-1):
    print(arr[i])'''

'''print(arr[::-1])'''

# 2nd largest
max=arr[0]
second_max=arr[0]
for i in arr:
    if i>max:
        second_max=max
        max=i
    elif i>second_max and i!=max:
        second_max=i

print(second_max)
    