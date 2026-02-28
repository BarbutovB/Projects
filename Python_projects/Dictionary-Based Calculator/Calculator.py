def main():
    print("--- Dictionary Calculator ---")

    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    results = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2
    }

    if op == "/":
        if num2 == 0:
            print("Error: Division by zero.")
        else:
            print("Result:", num1 / num2)

    elif op in results:
        print("Result:", results[op])

    else:
        print("Error: Invalid operator.")
if __name__ == "__main__":
    main()


