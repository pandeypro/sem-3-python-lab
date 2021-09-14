a=int(input("enter the number : "))
b=int(input("enter the number : "))
while b!=0 :
    rem=a%b
    a=b
    b=rem
print("The HCF of the given number = ",a)
