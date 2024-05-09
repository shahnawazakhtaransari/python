x=int(input("enter the number!"))
n=x
d=s=0
while x!=0:
    d=x%10
    s=s*10+d
    x=x//10
if s==n:
    print(f"{n} is a palindrome number!")
else:
    print(f"{n} is not a palindrome number!")    