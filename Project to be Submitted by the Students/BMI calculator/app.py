import streamlit as st
import pandas as pd

st.set_page_config(page_title="BMI Calculator", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: white;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #000000;
    }
    [data-testid="stHeader"] {
        background-color: #000000;
    }
    [data-testid="stSidebar"] {
        background-color: #000000;
    }
    h1, h2, h3, p, li {
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    .stSlider > div > div > div {
        background-color: red;
    }
    div[data-baseweb="slider"] span {
        background-color: red !important;
    }
    ul {
        color: white; /* Make the list items white */
    }
    h3 {
        color: white; /* Make the heading white */
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("## **BMI Caclculator**")  

st.markdown("#### Enter your height (in cm):")
height = st.slider("", 100, 250, 175, key="height")

st.markdown("#### Enter your weight (in kg):")
weight = st.slider("", 40, 200, 70, key="weight")

height_m = height / 100
bmi = weight / (height_m ** 2)

st.markdown(f"### Your BMI is **{bmi:.2f}**")

st.markdown("## 🔗 **BMI Categories**")
st.markdown("""
<ul>
    <li>Underweight: BMI less than 18.5</li>
    <li>Normal weight: BMI between 18.5 and 24.9</li>
    <li>Overweight: BMI between 25 and 29.9</li>
    <li>Obesity: BMI 30 or greater</li>
</ul>
""", unsafe_allow_html=True)
