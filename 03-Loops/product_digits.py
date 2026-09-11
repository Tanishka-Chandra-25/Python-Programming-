num=int(input("Enter number:"))
p=1
while num>0:
  p*=num%10
  num=num//10
  
print("The product of digits:",p)
