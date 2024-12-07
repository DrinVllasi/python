
def calculate(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        if number2 != 0:
            return number1 / number2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

first_number = input("Enter the first number")
second_number = input("Enter the second number")

result = float(first_number) + float(second_number)
print(result)
arithmetic_prompt = input("Enter an arithmetic operation")




