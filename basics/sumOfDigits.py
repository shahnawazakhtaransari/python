x=int(input("enter the number!"))
d=s=0
while x!=0:
    d=x%10
    s=s+d
    x=x//10
print(s)    