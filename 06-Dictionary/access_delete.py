student={
    "name":"Tanishka",
    "age":20,
    "branch":"ECE"
}
print("Name:",student["name"])
print("Age:",student["age"])
print("Branch:",student["branch"])
      
student.pop("age")
print("After deleting age:")
print(student) 
