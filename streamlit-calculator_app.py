import streamlit as st

st.title('TASK-01')
st.header('SIMPLE CALCULATOR')

num1 = int(st.number_input("Enter num1: "))
num2 = int(st.number_input("Enter num2: "))

operation = st.radio("Select operation: ", ("Add", "Subtract", "Multiply", "Divide"))

if st.button("CALCULATE"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"Result: {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"Result: {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"Result: {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {result}")
        else:
            st.error("Division by zero is not allowed.")
