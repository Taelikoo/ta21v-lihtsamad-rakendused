operation = input ("pick action: +, -, /, //, %, *, **: ")
if operation == "+": 
    n1 = int(input("enter first number: "))
    n2 = int(input("enter second number: "))
    print(n1 + n2)

elif operation == "-": 
    n1 = int(input("enter first number: "))
    n2 = int(input("enter second number: "))
    print(n1 - n2)

elif operation == "/": 
    n1 = int(input("enter first number: "))
    n2 = int(input("enter second number: "))
    print(n1 / n2)

elif operation == "//": 
    n1 = int(input("enter first number: "))
    n2 = int(input("enter second number: "))
    print(n1 // n2)

elif operation == "%": 
    n1 = int(input("enter first number: "))
    n2 = int(input("enter second number: "))
    print(n1 % n2)

elif operation == "*": 
    n1 = int(input("enter first number: "))
    n2 = int(input("enter second number: "))
    print(n1 * n2)

elif operation == "**": 
    n1 = int(input("enter first number: "))
    n2 = int(input("enter second number: "))
    print(n1 ** n2)