# LAb task 1
import re

def dynamic_calculator(expression):
    # Step 1: Add multiplication sign for cases like "2(3)" -> "2*(3)"
    expression = re.sub(r'(?<=\d)\(', '*(', expression)
    
    # Step 2: Safely evaluate the expression using eval
    try:
        result = eval(expression, {"_builtins_": None}, {})
        return result
    except Exception as e:
        return f"Error in expression: {e}"

# Example usage:
expression = "1 + 2 * 3(4 - 5 / 4) - (3 / 5)"
result = dynamic_calculator(expression)
print(f"Result of '{expression}' is: {result}")
