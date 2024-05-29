print("W3Resource")
# # Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
# b=input("Enter the elements of the list being separated by spaces:")
# list=b.split()
# print(list)
# if len(b) == len(set(b)):#Sets do not allow duplicate values therefore if len is equal it means no duplicate values
#     print("no duplicate values")
# else:
#     print("Duplicate values are present")        
#different approach
b = input("enter the elements of the list being separated by spaces: ")
list = b.split()
print(list)
dic = {}

for i in list:
    if i in dic:
        print('error')
        break
    else: 
        dic[i] = 1
