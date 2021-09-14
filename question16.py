print("enter 10 integers :")
number=[]
odd = []
for i in range(10):
    x = int(input())
    number.append(x)
    if x%2 !=0:
        odd.append(x)
if len(odd)!=0:
    max = odd[0]
    for i in range(len(odd)):
        if max<odd[i]:
             max = odd[i]
    print("max odd integer is : ",max)
else:
    print("NO odd number is present .")