import streamlit as st

st.title("Task-02")
st.header("BMI Calculator")

height = st.number_input("Enter height (cm):", min_value=1.0)
weight = st.number_input("Enter weight (kg):", min_value=1.0)

if st.button("Calculate BMI"):
    height_in_m = height / 100
    bmi = weight / (height_in_m ** 2)
    st.success(f"Your BMI: {bmi:.2f}")

    if bmi < 18.5:
        st.warning("Underweight")
    elif 18.5 <= bmi < 25:
        st.success("Normal weight")
    elif 25 <= bmi < 30:
        st.warning("Overweight")
    else:
        st.error("Obese")
