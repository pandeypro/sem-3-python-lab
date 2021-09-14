n=int(input("enter the number : "))
number=str(n)
result_string= " "
for i in range(5) :
    if(number[i]=="9") :
        result_string +="0"
    else :
        result_string +=str((int(number[i])+1))
print("the new number = ",result_string)