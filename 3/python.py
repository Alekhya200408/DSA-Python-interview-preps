# Function
# add Two numbers with function
'''def add(a,b):
    return a+b
c=add(2,3)
print(c)'''

# Max of two number
'''def max(a,b):
    if a>b:
        print(f"{a} is bigger")
    elif b>a:
        print(f"{b} is bigger")
    else:
        print("Both are Same")
max(3,5)'''

# Function to check even or odd
'''def even_odd(x):
    if x%2==0:
        print(f"{x} is an Even Number")
    else:
        print(f"{x} is a Odd number")

even_odd(5)'''

# Function to calculate factorial
'''def factorial(x):
    fact=1
    for i in range (1,x+1):
        fact=fact*i
    return fact

print(factorial(5))'''

# Function to check prime number
'''def Prime(x):
    if x<=0:
        print("Not Prime")
        return
    else:    
        for i in range (2,x):
            is_prime=True
            if x%i==0:
                is_prime=False
        if is_prime:
            print("Prime")
        else:
            print("Not Prime")

Prime(14)'''

# Function to count vowels in a string
'''def vowels():
    x=input("Enter the Word: ")
    count=0
    for i in x.lower():
        if i in "aeiou":
            count+=1 
    print(count)

vowels()'''

#  Function to reverse a string

'''def reverse():
    x=input("Enter the word: ")
    print(x[::-1])

reverse()'''

# Function to find the largest element in a list
'''def largest():
    x=[10,20,30,40,50,22,70,34,22,99]
    highest=x[0]
    for i in x:
        if i>highest:
            highest=i
    print(highest)

largest()'''