import streamlit as st

def calculate(Pesha, Gjatesia):
    bmi = Pesha / (Gjatesia ** 2)
    return bmi

def main():

    Emri = st.text_input("Enter your name")
    Mbiemri = st.text_input("Enter your last name")
    Mosha = st.number_input("Enter your age", step=2)
    Pesha = st.number_input("Enter your weight in kg")
    Gjatesia = st.number_input("Enter your height in m")

    def on_button_click():
        bmi = calculate(Pesha, Gjatesia)
        st.write(f"{Emri} {Mbiemri} is {Mosha} years old and the BMI is {bmi:.2f}")

    if st.button("Press me"):
        on_button_click()

if __name__ == "__main__":
    main()
