import art
print(art.logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an Operation.")
        num2 = float(input("What is the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        user_choice = input(f"Do you want to continue with {answer}? Type 'Yes' or 'No'").lower()
        if user_choice == 'no':
            should_continue = False
        elif user_choice == 'yes':
            num1 = answer
        else:
            calculator()


calculator()
