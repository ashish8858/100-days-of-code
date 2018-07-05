import sys
a = int(input("Enter a num 1 : "))
b = int(input("Enter a num 2 : "))
print (a,b)
print("press + for Add, Press - for Sub, press * for Mul, Press / for Div")
choice=input("Enter Choice : ")
if choice== '+':
    c=a+b
elif choice=='-':
    c=a-b
elif choice=='*':
    c=a*b
else:
    c=a/b

print("Result : " )
print (c)
