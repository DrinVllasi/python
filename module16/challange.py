import streamlit as st

def calculate():



def main():

    Emri = st.text_input("Enter your name")
    Mbiemri = st.text_input("Enter your last name")
    Mosha = st.number_input("Enter your age",step=2)
    Weight = st.number_input("Enter your weight in kg",)
    Gjatesia = st.number_input("Enter your height in cm",step=2)

    def on_button_click():

        st.write(f"{Emri} {Mbiemri} is {Mosha} years old and the BMI is ")

    if st.button("Press me"):
        on_button_click()

if __name__ == "__main__":
    main()
