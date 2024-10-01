import math

def calculator():
    print("Welcome to the Python calculator!")
    print("You can enter any mathematical expression.")
    print("Available functions: sin, cos, tan, log, sqrt")
    print("Type 'exit' to quit the calculator.")

    while True:
        # Take input from the user
        expression = input("Enter expression: ")

        # Check if the user wants to exit
        if expression.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            # Evaluate the expression, allowing trigonometric and other math functions
            result = eval(expression, {"_builtins_": None}, {
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'log': math.log,      # Natural log (ln)
                'sqrt': math.sqrt,
                'pi': math.pi,
                'e': math.e
            })
            print(f"Result: {result}")
        except Exception as e:
            # Catch any errors in the input or evaluation
            print(f"Error: {e}")

# Run the calculator
calculator()