# streamlit run "streamlit tutorial.py"

import streamlit as st
# st.title("hello jai")
# st.header("programming language picker")
# st.write("choose your fav programming language")
# chai=st.selectbox("your fav programming language : ",["python","java","c","react"])
# st.write(f"you choose {chai} and this is your fav programming language =  {chai}")
# st.header(f"jai fav programming language is {chai}.")

# chai maker app
# st.title("welcome to chai maker app!")
# if st.button("make chai"):
#     st.success("your chai is brewing")
# masala=st.checkbox("add masalas")
# if masala:
#     st.write("masala added in your chai")
# chai_base=st.radio("pick your chai base : ",["milk","water","almond milk"])
# st.write(f"selected base is {chai_base}.")
# flavours=st.selectbox("pick your favourite flavour : ",["adrak","tulsi","kesar"])
# st.write(f"selected flavour is {flavours}.")
# sugar_level=st.slider("sugar level",0,10,3)
# st.write(f"selected sugar level is {sugar_level}.")
# cups=st.number_input("how many cups",1,10,1)
# st.write(f"selected cups is {cups}.")
# name=st.text_input("enter your name")
# if name:
#     st.write(f"welcome {name}! your chai is on the way.")
# dob=st.date_input("select your date of birth")
# if dob:
#     st.write(f"your date of birth is {dob}.")


# calculator
# from datetime import date
# st.title("welcome to age calculator")
# curr_year=2025
# name=st.text_input("enter your name")
# dob=st.date_input("select your date of birth",min_value=date(2000,1,1),max_value=date.today())
# st.write(f"{name} your age is {curr_year-dob.year}")

# chai taste poll
# st.title("chai taste poll")
# col1,col2=st.columns(2)
# with col1:
#     st.header("masala chai")
#     st.image("data:image/jpeg;base64,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",width=200)
#     vote1=st.button("vote masala chai")
# with col2:
#     st.header("adrak chai")
#     st.image("data:image/jpeg;base64,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",width=200)
#     vote2 = st.button("vote adrak chai")
#
# if vote1:
#     st.success("thanks for voting masala chai")
# elif vote2:
#     st.success("thanks for voting adrak chai")
#
# name=st.sidebar.text_input("enter your name")
# chai=st.sidebar.radio("enter your fav chai : ",["masala chai","adrak chai"])
# st.sidebar.write(f"{name} favourite chai is {chai}")
#
# with st.expander("show chai recipe"):
#     st.write("""
#     1. boiled waiter and add tea leaves
#     2. add adrak and milk
#     3. add elachi and boiled it
#     """)
#
# st.markdown("# welcome to chai")
# st.markdown("_this is italic chai_")
# st.markdown("**this is bold chai**")

#  Success, Info, Warning, Error, Exception:
#st.error("hello error")

# checkbox
# if st.checkbox("show me my name"):
#     st.write("jai singh")

# radio button
# gender=st.radio("gender : ",["male","female"])
# if gender=="male":
#     st.success("male")
# else:
#     st.success("female")

# selection box
# gender = st.selectbox("gender : ", ["male", "female"])
# if gender == "male":
#     st.success("male")
# else:
#     st.success("female")

# multi select box
# gender = st.multiselect("gender : ", ["male", "female"])
# if gender == "male":
#     st.success("male")
# else:
#     st.success("female")


# button
# Create a simple button that does nothing
# st.button("Click me for no reason")

# Create a button, that when clicked, shows a text
# if(st.button("About")):
#     st.text("Welcome To GeeksForGeeks!!!")

# text input
# name=st.text_input("enter your name : ")
# if st.button("submit"):
#     st.success(f"{name} has been subitted")

# slider
# res=st.slider("select your kid age",1,18,9)
# st.write(f"selected : {format(res)}")

#code
# st.header("🧠 AI Model Summary")
# st.markdown("### Key Metrics")
# st.code("""
# #for lop code
# for i in range(3):
#     print(i)
# """)
# st.code("for i in range(5): print(i)", language='python')


#latex
# st.latex(r'\sum_{i=1}^{n} x_i^2 = x_1^2 + x_2^2 + \cdots + x_n^2')

#divider and markdown

# st.write("Content above")
# st.divider()
# st.write("Content below")

# st.markdown("- ## hi this is dot")
# st.markdown("## 1 hi this is no")
# st.markdown("~~jaya~~ jai")
#

# inputs
# st.date_input("select your dob")
# st.time_input("enter current time")
#
# skills = st.multiselect("Your skills", ["Python", "HTML", "CSS", "SQL"])

# file uploader
# file = st.file_uploader("Upload CSV", type=["csv"])

# camera input
# st.camera_input("camera input : ")

# forms
# with st.form("user form"):
#     name=st.text_input("enter your name")
#     submit=st.form_submit_button("submit")
#     if submit:
#         st.success("forms submitted successfully")


# download files
# txt = "heloo jai singh"
# st.download_button("Download file", txt, file_name="jai.text")


# session state
# if "count" not in st.session_state:
#     st.session_state.count=0
#
# if st.button("add"):
#     st.session_state.count += 1
#
# st.write(f"count : {st.session_state.count}")

# st.spinner() + st.success(), st.error(), st.warning(), st.info()
# import time
# with st.spinner("loading..."):
#     time.sleep(5)
# st.success("complete!!")
# st.warning("it will take 5 seconds")
# st.error("it will take 5 seconds")
# st.info("it will take 5 seconds")
#
# st.toast("✅ Data saved successfully!", icon="🎉")
#

#audio,video
# st.audio("ja")

# with st.form("form1"):
#     name = st.text_input("Name")
#     age = st.slider("Age", 1, 100)
#     submit = st.form_submit_button("Submit")
#     if submit:
#         st.write(name, age)


# container
# if st.container():
#     st.write("### inside container")
#     st.write("### group")

# tabs
# tab1, tab2 = st.tabs(["Upload", "Analysis"])
# with tab1:
#     st.write("File upload here")
# with tab2:
#     st.write("Chart will show here")


# matrices
# st.metric("Temperature", "70 °F")
# st.metric("Revenue", "$1,234,567"


# Initialize counter in session state

# if "submit" not in st.session_state:
#     st.session_state.submit = False
# with st.form("registration"):
#     name=st.text_input("name")
#     age=st.number_input("age")
#     submit=st.form_submit_button("submit")
#     if submit:
#         st.session_state.name=name
#         st.session_state.age = age
#         st.session_state.submit=True
#
# if st.session_state.submit==True:
#     st.success("welcome")


with st.sidebar:
    name = st.text_input("Enter your name")
    level = st.selectbox("Choose difficulty", ["Easy", "Medium", "Hard"])
    agree = st.checkbox("I agree")

st.write("Name:", name)
st.write("Level:", level)
st.write("Agreement:", agree)


