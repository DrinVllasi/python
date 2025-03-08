import streamlit as st


def calculate(num1, num2, operation):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Division":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "Cannot be divided by zero"
    return result


def main():

    num1 = st.number_input("Enter the first number", step=1)
    num2 = st.number_input("Enter the second number", step=1)


    operation = st.radio('Choose an operation:', ['Addition', 'Subtraction', 'Multiply', 'Division'])


    result = calculate(num1, num2, operation)


    st.write(f"The result of the {operation} of {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()
