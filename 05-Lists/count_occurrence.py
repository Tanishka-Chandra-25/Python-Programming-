l=[]
n=int(input("Enter length of list:"))
for i in range(n):
  num=int(input("Enter number:"))
  l.append(num)
print("List:",l)
c=int(input("Enter number to be counted:"))
t=l.count(c)
print(f"{c} occurred for {t} times")
