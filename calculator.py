import streamlit as st
st.header("welcome to calculator!")
num1=st.number_input("enter number 1")
choice=st.selectbox("choose any operatons : ",["+","-","*","/","%"])
num2=st.number_input("enter number 2")
if choice=="+":
    res=num1+num2
    st.success(res)
elif choice=="-":
    res = num1 - num2
    st.success(res)

elif choice=="*":
    res = num1 * num2
    st.success(res)

elif choice=="/":
    try:
        res = num1 / num2
        st.success(res)
    except ZeroDivisionError:
        st.error("cannot be divided by 0")
else:
    res = num1 % num2
    st.success(res)

st.divider()
st.markdown("## thank you for using my calculator!!")
st.image("https://thumbs.dreamstime.com/b/3d-small-people-calculator-15960335.jpg",width=150)


