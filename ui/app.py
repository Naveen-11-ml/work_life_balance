from work_life_balance.modeling.predict import Predict

import streamlit as st

st.title("Work Life Balance Survey")
st.write("Please answer the following questions to help us understand your work life balance.")

ques, info = st.columns([0.9, 0.1])
ques.subheader("1. On a daily diet how much Fruits/Vegetable do you eat?")
with info.popover("i"):
    st.write("Rate in the scale of 1 (very low within entire diet) to 5 (highly intake).")
fruits_veggies = st.slider("Fruits/Vegetable", 1, 5)