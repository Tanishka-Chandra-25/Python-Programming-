l=[]
n=int(input("Enter length:"))
for i in range(n):
  num=int(input("Enter number:"))
  l.append(num)
print("List:",l)

new=[]
for t in l:
    if t not in new:
        new.append(t)
print("List without duplicates:",new)
  
