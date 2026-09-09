num=int(input("Enter any number:"))
og=num
rev=0
while num>0:
    d=num%10
    rev=rev*10+d
    num=num//10
if (rev==og):
  print("PALINDROME")
else:
  print("NOT PALINDROME")
