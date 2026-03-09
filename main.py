from utils_calc import add, sub, multiply, divide, exponent, modulo, floor_divide, absolute

TWO_ARG_OPS = {"add", "subtract", "multiply", "divide", "exponent", "modulo", "floor_divide"}
ONE_ARG_OPS = {"absolute"}
VALID_OPS = TWO_ARG_OPS | ONE_ARG_OPS | {"exit"}

PROMPT = "Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):"

while True:
    op = input(PROMPT + "\n").strip().lower()

    if op not in VALID_OPS:
        print("Invalid option!")
        continue

    if op == "exit":
        break

    if op in TWO_ARG_OPS:
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))

        if op == "add":
            result = add(num1, num2)
        elif op == "subtract":
            result = sub(num1, num2)
        elif op == "multiply":
            result = multiply(num1, num2)
        elif op == "divide":
            result = divide(num1, num2)
        elif op == "exponent":
            result = exponent(num1, num2)
        elif op == "modulo":
            result = modulo(num1, num2)
        elif op == "floor_divide":
            result = floor_divide(num1, num2)

    elif op == "absolute":
        num1 = float(input("Enter the number:\n"))
        result = absolute(num1)

    if isinstance(result, str) and result.startswith("Error"):
        print(result)
    else:
        print(f"The result is: {result}")
