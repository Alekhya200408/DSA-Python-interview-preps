# Count frequency of elements in an array

'''arr=[10,20,30,40,50,60,20,20]
freq=0
element=int(input("Enter the Element:"))

for i in arr:
    if i==element:
        freq+=1
if freq==0:
    print("Element is not in the Array")
    
print(freq)'''

# Count frequency of characters in a string
'''text=input("Enter the Text:")
freq=0
char=input("Enter the character:")

for ch in text:
    if ch==char:
        freq+=1
if freq==0:
    print("Not in the text")
print(freq)'''

# Find the first non-repeating character
text=input("Enter the Text:")

freq={} #using dictonary for hashing

for ch in text:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

for ch in text:
    if freq[ch]==1:
        print("The first non repeating character is:",ch)
        break
else:
    print("There is no non repeating character")
      