import streamlit as st

st.title("BMI Calculator 🏋️‍♂️")

height = st.number_input("Enter your height (in meters):", format="%.2f")
weight = st.number_input("Enter your weight (in kg):", format="%.1f")

if st.button("Calculate BMI 🤔"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is: {bmi:.2f} 🎯")

        if bmi < 18.5:
            st.warning("Underweight ❌")
        elif 18.5 <= bmi < 24.9:
            st.success("Normal weight ✅")
        elif 25 <= bmi < 29.9:
            st.warning("Overweight ⚠️")
        else:
            st.error("Obese 🎈🎈🎈")  
    else:
        st.error("Height must be greater than zero ⚠️.")
