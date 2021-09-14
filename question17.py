n=int(input("enter the number to be checked : "))
cuberoot=round(n**(1/3))
if cuberoot*cuberoot*cuberoot==n :
    print("“the number is perfect cube")
else :
    print("“the number is not perfect cube")