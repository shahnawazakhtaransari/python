print("HCF")
f=0
m,n=input("enter the numbers ").split(',')
n=int(n)
m=int(m)
for i in range(1,max(m,n)):
    if n%i==0 and m%i==0:
        f=i
print(f," is the hcf")        
        
