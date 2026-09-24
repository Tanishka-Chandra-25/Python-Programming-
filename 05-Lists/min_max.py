l=int(input("Enter the length:"))
lst=[]
for i in range(l):
  n=int(input("Enter element:"))
  lst.append(n)
print("Maximum:",max(lst))
print("Minimum:",min(lst))

maximum=lst[0]
minimum=lst[0]
for t in lst:
  if t>maximum:
    maximum=t
  if t<minimum:
    minimum=t
print("Max:", maximum)
print("Min:", minimum)
  
  
