# Keily Nathan
# 8 Oct 2024
# Basic Calculator


ans=True
while ans:
    print ('''
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Divide
    ''')
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your next number: "))
    ans=input("What would you like to use?: ") 
    if ans == '1':
        print(num1, "+", num2, "=", (num1 +num2))
    elif ans == '2':
        print(num1, "-", num2, "=", (num1 - num2))
    elif ans == '3':
        print(num1, "*", num2, "=", (num1 * num2))
    elif ans == '4':
        print(num1, "/", num2, "=", (num1 / num2))
