import math
x=int(input("enter the number!"))
n=x
d=s=0
length=len(str(x))
while x!=0:
    d=x%10
    s=s+(math.pow(d,length))
    x=x//10
if s==n:
    print(f"{n} is an Armstrong number!")
else:
    print(f"{n} is not an Armstrong number!")    