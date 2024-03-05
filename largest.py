a=int(input("Enter number a"))
b=int(input("Enter number b"))
c=int(input("Enter number c"))
if(a>b and a>c):
    print("The largest number is",a)
elif(b>a and b>c):
    print("The largest number is",b)
else:
    print("The largest number is",c)
