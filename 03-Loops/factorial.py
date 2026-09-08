n=int(input("Enter n:"))
fact=1
if(n<0):
  print("Factorial is not defined for negative number")
else:
  while n>0:
    fact=fact*n
    n-=1
  print("The factorial:",fact)
