from math import sqrt
n=int(input("Enter a number"))
sahi=sqrt(n)
if sahi==int(sahi):
    print("perfect")
else:
    print("Not so Perfect")  
      
# from math import sqrt
# def isPerfectSquare(x):
#     if x >= 0:
#         sr = int(sqrt(x))
#         return (sr * sr) == x
#     return False


# n = 84
# if isPerfectSquare(n):
#     print("True")
# else:
#     print("False")