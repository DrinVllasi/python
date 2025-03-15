import pandas as pd
import streamlit as st

st.header("Displaying Data Frames")

data = pd.DataFrame({
    'Name' : ["Alice","Michael","Andy"],
    'Age' : [25,31,19],
    'City' : ["Miami","London","Boston"]
})

st.write(data)