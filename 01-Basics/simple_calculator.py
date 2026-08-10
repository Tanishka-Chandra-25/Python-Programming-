num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
choice = input("Enter the choice: ")

if choice == "+":
    result = num1 + num2
    print("The addition:", result)

elif choice == "-":
    result = num1 - num2
    print("The subtraction:", result)

elif choice == "*":
    result = num1 * num2
    print("The multiplication:", result)

elif choice == "/":
    result = num1 / num2
    print("The division:", result)

elif choice == "//":
    result = num1 // num2
    print("The floor division:", result)

elif choice == "%":
    result = num1 % num2
    print("The modulus:", result)

else:
    print("Invalid choice")
