def evaluate_postfix(expr: str) -> int:
    """
    Evaluates an expression in Reverse Polish Notation (RPN) and returns the result.
    Supports addition (+), subtraction (-), multiplication (*), and division (/).
    Raises a RuntimeError if the expression is invalid.
    """
    stack = []
    # Split the expression into tokens. Assuming the expression is space-separated.
    tokens = expr.split()
    
    for token in tokens:
        if token.isdigit():  # Check if the token is a number
            stack.append(int(token))
        elif token in "+-*/":
            if len(stack) < 2:  # Check if there are enough operands on the stack
                raise RuntimeError(f"Invalid expression '{expr}'")
            # Pop two operands
            b, a = stack.pop(), stack.pop()
            # Perform the operation and push the result back onto the stack
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':  # Ensure division by zero is handled
                if b == 0:
                    raise RuntimeError("Division by zero")
                stack.append(a / b)
        else:  # If the token is not a number or a supported operator
            raise RuntimeError(f"Invalid token '{token}' in expression '{expr}'")
    
    # Check if the stack has exactly one item left, which would be the result
    if len(stack) != 1:
        raise RuntimeError(f"Invalid expression '{expr}'")
    
    return stack.pop()

# Example usage
if __name__ == "__main__":
    print(evaluate_postfix("3 2 +"))  # 5
    print(evaluate_postfix("3 2 + 4 -"))  # 1
    try:
        print(evaluate_postfix("3 2 4 +"))
    except RuntimeError as e:
        print(e)  # Expected to raise an error