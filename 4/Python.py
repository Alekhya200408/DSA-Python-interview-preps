# Reverse a string
'''name="Alekhya"
print(name[::-1])'''

# Check palindrome string
'''name="madam"
if name==name[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")'''

# Count vowels and consonants
'''name="Alekhya"

vowels=0
consonants=0
for ch in name.lower():
    if ch.isalpha():
        if ch in 'aeiou':
            vowels+=1
        else:
            consonants+=1
print("Vowels",vowels)
print("Consonants",consonants)'''

# Count words in a sentence

'''sentence="My name is Alekhya"

word=sentence.split()

print("Total Words",len(word))'''
# USING SPLIT() FUNCTION

# Find the frequency of a character
'''name="alekhya"

character=input("Enter the character:")
count=0
for ch in name.lower():
    if ch==character:
        count+=1
print(count)'''

# Remove spaces from a string
'''sentence=("I am Alekhya")
wo_space=sentence.replace(" ","")

print(wo_space)'''
# USING REPLACE() FUNCTION

# Convert lowercase to uppercase without using `upper()` (using loops)
'''text=input("Enter the String:")

result=""
for ch in text:
    if "a" <=ch<="z":
        result+=chr(ord(ch)-32)
    else:
        result+=ch
print(result)'''

# Find the longest word in a sentence  
'''text=input("Enter The Sentence:")

word=text.split()
longest=""
for i in word:
    if len(i)>len(longest):
        longest=i
print("Longest Word is:",longest)'''

