num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))

if(num1==num2==num3):
    print("All three numbers are equal")
elif(num1==num2 and num1>num3):
    print("Number 1 and Number 2 are greatest")
elif(num1==num3 and num1>num2):
    print("Number 1 and Number 3 are greatest")
elif(num2==num3 and num2>num1):
    print("Number 2 and Number 3 are greatest")
elif(num1>num2 and num1>num3):
    print("Number 1 is greatest")
elif(num2>num1 and num2>num3):
    print("Number 2 is greatest")
else:
    print("Number 3 is greatest")
