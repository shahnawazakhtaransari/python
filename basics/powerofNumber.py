# import math
x,y=input("enter the power and the number").split()
x=int(x)
y=int(y)
# pow=math.pow(x,y)
# print(pow)
n = 1
for i in range(y):
  n*=x
print(n)