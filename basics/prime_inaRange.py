# def isprime(n):
#  sum=0
#  if n<2:
#      print(f"{n} is not a prime number")
#  elif n==2:
#      print(f"{n} is a prime number")
#  else:
#      for i in range(3,n):
#         if(n%i==0):
#             sum=sum+1
#      if sum==0:
#         print(f"{n} is a prime number")   
#      else:
#         print(f"{n} is nota prime number")
# #main function
# x,y=input("enter the range").split()
# x=int(x)
# y=int(y)
# for n in range(x,y+1):
#     if(isprime(n)):
#         print("thank you")


#===========from prepinsta==============
low, high = 2, 10
primes = [2]

for num in range(low, high + 1):
    flag = 0
    if num < 2:
        flag = 1
        
    if num % 2 == 0:
        continue
    i = 2

    while i < int(num / 2):
        if num % i == 0:
            flag = 1
            break
        i += 1

    if flag == 0:
        primes.append(num)

print(primes)