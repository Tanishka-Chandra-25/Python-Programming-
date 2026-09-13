row=int(input("Enter the row:"))
for t in range(1,row+1):  
    for u in range(row-i): 
        print(" ",end=" ")
    for s in range(1,2*i):  
        print("*",end=" ")
    print()
