from os import write

import streamlit as st

# col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="center")
#
# with col1:
#     st.header("column 1")
#     st.write("Column 1 content")
#
# with col2:
#     st.header("column 2")
#     st.write("Column 2 content")
#
# with col3:
#     st.header("column 3")
#     st.write("Column 3 content")
#
# with col4:
#     st.header("column 4")
#     st.write("Column 4 content")
#
# with col5:
#     st.header("column 5")
#     st.write("Column 5 content")

with st.form ("my form", clear_on_submit=True):
    name = st.text_input("Name")
    age = st.slider("Age",min_value=0,max_value=100)
    email = st.text_input("Email")
    bio = st.text_area("Short Bio")
    terms = st.checkbox("I agree to the terms and conditions")
    button = st.form_submit_button(label="Submit")


if button:
    st.write(name)
    st.write(age)
    st.write(email)
    st.write(bio)
    if terms:
        st.write("You agreed to the terms and conditions")
    else:
        st.write("You didn't agree to the terms and conditions")


tab1, tab2, tab3 = st.tabs(["Tab1","Tab2","Tab3"])
with tab1:
     st.header("Content for tab1")
     st.write("This is the tab1 content")

with tab2:
    st.header("Content for tab2")
    st.write("This is the tab2 content")

with tab3:
    st.header("Content for tab3")
    st.write("This is the tab3 content")