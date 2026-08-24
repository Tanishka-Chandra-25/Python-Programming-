choice=input("Enter character of choice:")
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))

match choice:
    case '+':
        sum=a+b
        print(sum)

    case '-':
        diff=a-b
        print(diff)

    case '*':
        mul=a*b
        print(mul)

    case '/':
        div=a/b
        print(div)
      
    case '//':
        floor=a//b
        print(floor)
      
    case '%':
        mod=a%b
        print(mod)

    case _:
        print("Invalid choice")
