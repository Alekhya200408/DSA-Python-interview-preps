# Positive Negeticve and zero
'''a=int(input("Enter a Number:"))

if a>0:
    print("it is positive")
elif a<0:
    print("it is negetive")
elif a==0:
    print("it is Zero")'''

# leap Year
'''a=int(input("Enter the year:"))

if a%400==0:
    print("Its a Leap year")
elif a%4==0 and a%100!=0:
    print("It's a leap year")
else:
    print("Not a leap Year") '''

# prime number
'''a=int(input("Enter a number:"))

if a<=1:
    print("Not Prime")
else:
    is_prime=True
    for i in range(2,a):
        if a%i==0:
            is_prime=False
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
'''
# Palindrome Number
'''num=input("Enter the number:")

if num==num[::-1]:
    print("Its a palindrome")
else:
    print("Not palindrome")'''

# armstrong number
'''num=int(input("Enter the number:"))

original=num
total=0

while num>0:
    digit=num%10
    total=total+digit**3
    num=num//10
if total==original:
    print("Armstrong")
else:
    print("Not Armstrong")'''

# Factorial
'''num=int(input("Enter the number:"))

fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)'''

# Fibonacci
num=int(input("Enter a number:"))

a=0
b=1

for i in range(num):
    c=a+b
    a=b
    b=c
    print(c)
