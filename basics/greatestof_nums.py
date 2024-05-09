# #2 numbers
# x,y=input("enter the numbers").split()
# x=int(x)
# y=int(y)
# if x>y:
#     print("X is greater")
# elif x==y:
#     print("x is equal to y")
# else:
#     print("y is greater")
#3 numbers
x,y,z=input("enter the numbers").split()
x=int(x)
y=int(y)
z=int(z)
if x>y and x>z:
    print(f"{x} is greater")
elif y>x and y>z:
    print(f"{y} is greater")
elif x==y==z:
    print("all are equal")    
else:
    print("z is greater") 