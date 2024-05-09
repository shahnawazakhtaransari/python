n=int(input("enter a number to check: "))
sum=0
if n<2:
    print(f"{n} is not a prime number")
elif n==2:
    print(f"{n} is a prime number")
else:
    for i in range(3,n):
        if(n%i==0):
            sum=sum+1
    if sum==0:
        print("not a prime number")   
    else:
        print(f"{n} is a prime number")
