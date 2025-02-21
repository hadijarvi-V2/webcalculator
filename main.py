# print("Hello World!")
import streamlit as st

st.Page(page= "main.py", title= "Calculator")
st.set_page_config(page_title="Calculator", layout="wide")

st.title("Wellcome to the Calculator!")
num1 = st.text_input(label="Enter the first number ", placeholder="Enter here")
num2 = st.text_input(label="Enter the second number ", placeholder="Enter here")
operation = st.text_input(label="Enter the operation ", placeholder="   +   -   *   /")

calculate= st.button(label="Calculate!")

result = 0

def calculations():
    global result
    global num1
    global num2
    
    num1 = int(num1)
    num2 = int(num2)
    
    if operation == "+":
        result = (num1 + num2)
    elif operation == "-":
        result = (num1 - num2)
    elif operation == "*":
        result = (num1 * num2)
    elif operation == "/":
        result = (num1 / num2)
    
    if result:
        st.subheader(result)

if calculate:
    calculations()
    st.balloons()
    
st.link_button("Homepage", "https://google.com")

st.markdown('<p style="text-align: center;">Developed by Hadi_Jarvi</p>', unsafe_allow_html=True)