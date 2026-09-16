s=input("Enter string:")
count=0
for t in s:
  if t=='a' or t=='e' or t=='i' or t=='o' or t=='u' or t=='A' or t=='E' or t=='I' or t=='O' or t=='U':
   count+=1
print("Total vowels:",count)
