def factorial(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f 
#source code
n=int(input("enter a number!"))
newN=n
s=0
while(n!=0):
    num=n%10
    s=s+int(factorial(num))
    n=n//10
if newN==s:
    print("Strong Number: ",s)
else:
    print("not a Strong Number: ",newN)