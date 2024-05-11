s=input("Enter an Alphabet!")
s=s.upper()
l=len(s)
if l>1:
    print("invalid input")
elif s=='A' or s=='E' or s=='O' or s== 'I' or s=='U':
    print(f"{s} is a vowel")
else:
    print(f"{s} is a consonant")
    print   