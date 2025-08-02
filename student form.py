import streamlit as st
import sqlite3

def connect_db():
    return sqlite3.connect("student form.db")

def create_table():
    conn=connect_db()
    c=conn.cursor()
    c.execute("""
    create table if not exists students_data(
    id integer primary key autoincrement,
    name text,
    age int,
    email text
    )
    """
    )
    conn.commit()
    conn.close()

def insert_data(name,age,email):
    conn = connect_db()
    c = conn.cursor()
    c.execute(" insert into students_data(name,age,email) values(?,?,?)",(name,age,email))
    conn.commit()
    conn.close()


def get_data():
    conn=connect_db()
    c=conn.cursor()
    c.execute(
        "select *from students_data"
    )
    data=c.fetchall()
    conn.close()
    return data


st.title("STUDENT FORM")
create_table()
with st.form("form"):
    st.subheader("PERSONAL INFORMATION")
    name=st.text_input("ENTER NAME")
    age=st.number_input("ENTER AGE",1,100)
    EMAIL = st.text_input("ENTER EMAIL")
    if st.form_submit_button("SUBMIT"):
        if name and EMAIL:
            insert_data(name,age,EMAIL)
            st.success("FORM SUBMITTED SUCCESSFULLY!")
        else:
            st.error("PLEASE FILL ALL THE FIELDS")

if st.checkbox("SHOW ALL THE STUDENTS"):
    data = get_data()
    for row in data:
        st.markdown(f"**ID:** {row[0]} | **Name:** {row[1]} | **Age:** {row[2]} | **Email:** {row[3]}")




