# creating attendence management system
# streamlit run "attendence management system.py"
import streamlit as st
import sqlite3


def connect_db():
    conn=sqlite3.connect('student form.db')
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def create_table():
    conn=connect_db()
    c=conn.cursor()
    c.execute("""
    create table if not exists students_data(
    id integer primary key autoincrement,
    name text,
    roll_no int,
    class_student int
    )
    """
    )
    c.execute(
        """
            create table if not exists attendence(
            id integer primary key autoincrement,
            student_id int,
            attendence_date date,
            status text,
            foreign key (student_id) references students_data(id)
            )
        """
    )

    conn.commit()
    conn.close()

def get_students(class_of_student):
    conn = connect_db()
    c = conn.cursor()
    c.execute(" select id,name from students_data where class_student=?", (class_of_student,))
    data=c.fetchall()
    conn.close()
    return data


def add_students(name,roll_no,class_student):
    conn = connect_db()
    c = conn.cursor()
    c.execute(" insert into students_data(name,roll_no,class_student) values(?,?,?)",(name,roll_no,class_student))
    conn.commit()
    conn.close()

def mark_attendence(student_id,att_date,status):
    conn = connect_db()
    c = conn.cursor()
    c.execute(" insert into attendence(student_id,attendence_date,status) values(?,?,?)", (student_id,att_date,status))
    conn.commit()
    conn.close()

def get_all_students_of_class(class_of_student):
    conn=connect_db()
    c=conn.cursor()
    c.execute("select name from students_data where class_student = ?",(class_of_student,))
    data=c.fetchall()
    conn.close()
    return data

def get_attendence_by_date(date):
    conn = connect_db()
    c = conn.cursor()
    c.execute(
        """
        SELECT s.name, s.class_student, a.attendence_date, a.status
        FROM attendence AS a
        JOIN students_data AS s
        ON a.student_id = s.id
        WHERE a.attendence_date = ?
        """,
        (date,)
    )
    data = c.fetchall()
    conn.close()
    return data

def attendence_report(name,class_student):
    try:
        conn = connect_db()
        c = conn.cursor()
        c.execute("""
        select s.name,s.roll_no,s.class_student,count(case when a.status='PRESENT' then 1 end) as PRESENT,count(case when a.status='ABSENT' then 1 end) as Absent
        from students_data as s
        join attendence as a
        on s.id=a.student_id
        where s.name=? and s.class_student=?
        group by s.name,s.roll_no,s.class_student 
        """, (name, class_student)
                  )
        data = c.fetchall()
        conn.close()
        return data
    except Exception as e:
        st.error(e)

st.title("🏫 ATTENDENCE MANAGEMENT SYSTEM")
connect_db()
create_table()
with st.sidebar:
    st.title("FEATURES")
    choice = st.selectbox("-- SELECT --", ["➕ ADD STUDENT", "✅ MARK ATTENDENCE","👀 VIEW ATTENDENCE","🔍	SHOW STUDENTS","📊 ATTENDENCE REPORT"])
if choice=="➕ ADD STUDENT":
    st.subheader("ADD A NEW STUDENT")
    with st.form("add students"):
        name = st.text_input("✏️ENTER NAME")
        roll_no = st.number_input("🔢ENTER ROLL NUMBER", 1, 1000)
        class_student = st.selectbox("ENTER CLASS",list(range(1,13)))
        submit=st.form_submit_button("🆗submit")
    if submit:
            if name and roll_no and class_student:
                add_students(name, roll_no, class_student)
                st.success("🟢 ADDED SUCCESSFULLy")
            else:
                st.error("PLEASE FILL ALL THE FILEDS")
if choice == "✅ MARK ATTENDENCE":
    st.subheader("MARK ATTENDENCE")
    class_select = st.selectbox("🏷️ Class", list(range(1, 13)))
    date_selected = st.date_input("📆 Date")
    students = get_students(class_select)
    att = {}

    if students:
        with st.form(key="mark_attendance_form"):  # use unique key
            for stuid, names in students:
                present = st.radio(
                    f"**SELECT for {names}**", ["PRESENT", "ABSENT"], key=f"{stuid}_radio"
                )
                att[stuid] = present
            mark = st.form_submit_button("📍 MARK")

        if mark:
            for student_id, status in att.items():
                mark_attendence(student_id, date_selected, status)
            st.success("🟢 Attendance marked successfully!")
    else:
        st.info("No students in this class.")

if choice=="👀 VIEW ATTENDENCE":
    st.subheader("VIEW ATTENDENCE")
    date_selected = st.date_input("**📆	date**")
    all_students=get_attendence_by_date(date_selected)
    if all_students:
        col_names=["**name**","**class**","**attendence**","**status**"]
        st.table({
            col_names[i]:[row[i] for row in all_students]
            for i in range(len(col_names))
        })
    else:
        st.info(f"NO ATTENDENCE OF DATE : {date_selected}")

if choice=="🔍	SHOW STUDENTS":
    st.subheader("SHOW STUDENTS")
    class_select = st.selectbox("🏷️class", list(range(1, 13)))
    all_students=get_all_students_of_class(class_select)
    if all_students:
        col_names=["**name**"]
        st.table({
            col_names[i]:[row[i] for row in all_students]
            for i in range(len(col_names))
        })
    else:
        st.info(f"NO STUDENTS IN CLASS {class_select}")

if choice=="📊 ATTENDENCE REPORT":
    st.subheader("📊 ATTENDENCE REPORT")
    name=st.text_input("**ENTER NAME**")
    class_student=st.selectbox("ENTER CLASS",list(range(1,13)))
    report = attendence_report(name, class_student)
    if report:
        col_names = ["name","roll nummber","class","present","absent"]
        st.table({
            col_names[i]: [row[i] for row in report]
            for i in range(len(col_names))
        })
    else:
        st.info(f"NO STUDENT of name : {name} IN CLASS {class_student}")


