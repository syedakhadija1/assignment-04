# BMI Calculator Web App

import streamlit as st

st.title("BMI Calculator")

st.sidebar.header("User Input")

def user_input_features():
    weight = st.sidebar.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0)
    height = st.sidebar.number_input("Height (m)", min_value=0.5, max_value=3.0, value=1.75)
    return weight, height

weight, height = user_input_features()

bmi = weight / (height ** 2)

st.write(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    st.write("You are underweight.")
elif 18.5 <= bmi < 24.9:
    st.write("You have a normal weight.")
elif 25 <= bmi < 29.9:
    st.write("You are overweight.")
else:
    st.write("You are obese.")

st.sidebar.subheader("About")
st.sidebar.text("This is a simple BMI calculator built with Streamlit.")
