import math
print("!Welcome to the Python calculator!\nTo exit the calculator type exit\n")
while True:
    action = input("Enter your action ['+', '-', '*', '/', '%', '^', 'log']: ").lower().strip()
    
    if action == exit:
        print("Have a nice day")
        break
    
    elif action == 'log':
        arg = float(input("Input the argument: "))
        base = float(input("Input the base: "))
        result = math.log(arg, base)
        
    else:
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
        
        # Do the math operations
        if action == '+': result = num1 + num2
        elif action == '-': result = num1 - num2
        elif action == '*': result = num1 * num2
        elif action == '/': result = num1 / num2
        elif action == '%': result = num1 % num2
        elif action == '^': result = num1 ** num2
        else: raise ValueError("Invalid action")
        
    print(f"Result is {result}")