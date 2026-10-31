A={1,2,3,4,5}
B={2,3,4}

if A.issubset(B):
    print("A is subset of B")

elif B.issubset(A):
    print("B is subset of A")

elif A.issuperset(B):
    print("A is superset of B")

else:
    print("B is superset of A")
