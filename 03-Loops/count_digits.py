num=int(input("Enter number:"))
count=0
if num==0:
  count=1
else:
  while num>0:
  count+=1
  num=num//10
print("The number of digits:",count)
