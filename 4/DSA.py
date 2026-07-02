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
      
# 4. Check if two strings are anagrams (using dictionary)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# If lengths are different, they can't be anagrams
if len(str1) != len(str2):
    print("Not Anagrams")
else:
    freq = {}

    # Count characters in first string
    for ch in str1:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Remove characters using second string
    for ch in str2:
        if ch in freq:
            freq[ch] -= 1
        else:
            print("Not Anagrams")
            break
    else:
        # Check if all counts became 0
        for value in freq.values():
            if value != 0:
                print("Not Anagrams")
                break
        else:
            print("Anagrams")