num=int(input("Enter number:"))
if num<=0:
  print("Enter valid number")
else:
  for t in range(2,num):
    if (num%t==0):
      print("NOT PRIME")
      break
    else:
      print("PRIME")
    
