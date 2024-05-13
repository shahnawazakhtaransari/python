num = int(input("enter a number:"))
a = str(num)
num1 = num ** 2
b = str(num1)
if b[-len(a):] == a:
    print("It's an Automorphic Number")
else:
    print("It's not an Automorphic Number")
# num = 376
# a = str(num)

# num1 = num ** 2
# b = str(num1)

# if b.endswith(a):
#     print("It's an Automorphic Number")
# else:
#     print("It's not an Automorphic Number")