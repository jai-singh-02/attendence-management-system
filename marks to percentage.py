# import streamlit as st
# st.header("marks to percentage!")
# maths=st.number_input("enter maths marks")
# english=st.number_input("enter english marks")
# hindi=st.number_input("enter hindi marks")
# science=st.number_input("enter science marks")
# economics=st.number_input("enter economics marks")
# st.divider()
# total,percentage,grades=st.columns(3)
# with total:
#     tot=maths+english+hindi+science+economics
#     st.markdown(f"**total marks** : **{tot}**")
# with percentage:
#     perc=tot/500*100
#     st.markdown(f"**percentage** : **{perc}%**")
# with grades:
#     g=None
#     if perc<60:
#         g="C"
#     elif perc>60:
#         g="B"
#     elif perc>80:
#         g="A"
#     st.markdown(f"**grades** : **{g}**")
#
# res=st.button("click to check result")
# if res:
#     if perc>40:
#         st.success("PASS!")
#     else:
#         st.error("FAIL!")


import streamlit as st

st.set_page_config(page_title="📚 Marks to Percentage", layout="centered")

st.title("📊 Student Marks Calculator")
st.markdown("Enter your marks below (out of 100 for each subject):")

# 🧮 Subject Inputs
subjects = ["Maths", "English", "Hindi", "Science", "Economics"]
marks = {}

with st.form("marks_form"):
    for subject in subjects:
        marks[subject] = st.number_input(f"{subject} marks", min_value=0, max_value=100, step=1, key=subject)

    submitted = st.form_submit_button("🎯 Calculate Result")

if submitted:
    total = sum(marks.values())
    percentage = (total / (100 * len(subjects))) * 100

    # 🎓 Grade calculation
    if percentage >= 80:
        grade = "A"
        grade_msg = "🌟 Excellent"
    elif 60 <= percentage < 80:
        grade = "B"
        grade_msg = "👍 Good"
    else:
        grade = "C"
        grade_msg = "🙂 Needs Improvement"

    # ✅ Pass/Fail
    result = "✅ PASS" if percentage >= 40 else "❌ FAIL"

    # 📈 Show results in columns
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📌 Total", f"{total} / 500")
    with col2:
        st.metric("📊 Percentage", f"{percentage:.2f}%")
    with col3:
        st.metric("🏅 Grade", f"{grade} - {grade_msg}")

    st.divider()
    if result == "✅ PASS":
        st.success(f"{result} 🎉 You did well!")
    else:
        st.error(f"{result} 😞 Better luck next time.")

    st.markdown("📘 *Thank you for using the calculator!*")


