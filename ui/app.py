# Import Library
import streamlit as st

st.title("Checking Docker App")

st.write("Does this work?")

st.subheader("One way to find out!!")

check_button = st.checkbox("App On")

if check_button:
    print("Ok next step now.")