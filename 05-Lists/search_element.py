l=[]
n=int(input("Enter Length:"))
for t in range (n):
  e=int(input("Enter element:"))
  l.append(e)
print("List:")
sr=int(input("Enter element to be searched:"))
f=False
for i in range(n):
  if l[i]==sr:
    print("Element found at:",i)
    f=True
if f==False:
    print("Element not found")
