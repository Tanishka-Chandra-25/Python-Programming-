import math
num=int(input("Enter number:"))
new=num
count=0
sp=0
while num>0:
  count+=1
  num=num//10

num=new
while num>0:
  r=num%10
  pw=pow(r,count)
  sp=sp+pw
  num=num//10

if(new==sp):
  print("ARMSTRONG")
else:
  print("NOT ARMSTRONG")
