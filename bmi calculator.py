import streamlit as st
st.title("welcome to BMI calculator!")
name=st.text_input("enter your name : ")
bmi=None
weight = st.number_input("enter your weight in kgs : ")
if weight<=0:
    st.error("weight cannot be zero or less than 0")
choice=st.radio("in which waay do you want to enter height",["cms","metre","feet"])
if choice=="cms":
    height_cms = st.number_input("enter height in cms")
    try:
        bmi = weight / ((height_cms / 100) ** 2)
    except ZeroDivisionError:
        st.error("Height cannot be zero. Please enter a valid height.")
elif choice=="metre":
    height_metre = st.number_input("enter height in metre")
    try:
        bmi = weight / (height_metre ** 2)
    except ZeroDivisionError:
        st.error("Height cannot be zero. Please enter a valid height.")

else:
    height_feet = st.number_input("enter height in feet")
    try:
        bmi = weight / (height_feet ** 2)
    except ZeroDivisionError:
        st.error("Height cannot be zero. Please enter a valid height.")

if st.button("calculate bmi"):
    if bmi:
        st.markdown(f"## BMI of {name} is : {bmi}")
        if (bmi < 16):
            st.error("You are Extremely Underweight")
        elif (bmi >= 16 and bmi < 18.5):
            st.warning("You are Underweight")
        elif (bmi >= 18.5 and bmi < 25):
            st.success("Healthy")
        elif (bmi >= 25 and bmi < 30):
            st.warning("Overweight")
        elif (bmi >= 30):
            st.error("Extremely Overweight")

st.markdown("---")
st.markdown("## thank you for using BMI calculator")

