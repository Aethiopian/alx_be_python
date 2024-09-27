# Prompt for user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using match case
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            result = "Error: Division by zero is not allowed."
        else:
            result = num1 / num2
    case _:
        result = "Error: Invalid operation."

# Output the result
if isinstance(result, str):
    print(result)
else:
    print(f"The result is {result:.2f}.")
