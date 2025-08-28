import random
r=random.randint(1,10)
n=int(input("Guess the number: "))
count=1
while n!=r:
    
    if n<r:
        print("Too low")
        count+=1
    else:
        print("Too high")
        count+=1

    n=int(input("Again guess the number: "))

if n==r:
    print(n,'is the correct number')
    print('you took',count,'attempts')