num1 = float(input("what is your 1st number?: "))
op = input("what is your opearstion?: ")
num2 = float(input("what is your 2nd number?: "))

if op == "+":
    print(num1 + num2)
    
elif op == "-":
    print(num1 - num2)
    
elif op == "*":
    print(num1 * num2)
    
elif op == "/":
    print(num1 / num2)
    
else:
    print("""Inavlid Operator pls use The Following operator
             1. +
             2. -
             3. *
             4. /
             
             Pls Retry The Operator again""")
