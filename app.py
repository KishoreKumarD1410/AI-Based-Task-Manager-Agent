import streamlit as st
import pandas as pd
from datetime import datetime
import database as db
import llm_handler
import sqlite3

# --- Page Configuration ---
st.set_page_config(page_title="AI Task Manager", layout="wide", initial_sidebar_state="expanded")

# --- CSS Styles ---
st.markdown("""
    <style>
    .sidebar .sidebar-content { background-color: #f0f2f6; }
    .main-content { padding: 2rem; }
    .task-card { background-color: #ffffff; padding: 1rem; margin-bottom: 1rem; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); }
    .task-card:hover { background-color: #f9fafb; }
    .task-title { font-size: 1.1rem; font-weight: 600; }
    .task-info { font-size: 0.9rem; color: #555555; }
    .task-actions { margin-top: 0.5rem; }
    .task-actions button { margin-right: 0.5rem; }
    </style>
""", unsafe_allow_html=True)

# --- Helper Functions ---
def initialize_session_state():
    if "user_name" not in st.session_state: st.session_state.user_name = ""
    if "user_email" not in st.session_state: st.session_state.user_email = ""
    if "logged_in" not in st.session_state: st.session_state.logged_in = False
    if "llm" not in st.session_state:
        try:
            st.session_state.llm = llm_handler.get_llm()
        except ValueError as e:
            st.error(f"LLM Initialization Error: {e}")
            st.stop()
    if "last_task" not in st.session_state:
        st.session_state.last_task = None

# --- Initialize ---
initialize_session_state()
db.create_db_and_table()

# --- Sidebar ---
with st.sidebar:
    st.header("User Info")
    if st.session_state.logged_in:
        st.write(f"👤 {st.session_state.user_name}")
        st.write(f"📧 {st.session_state.user_email}")
        if st.button("Logout"): 
            st.session_state.logged_in = False
            st.experimental_rerun()
    else:
        st.title("Login")
        name = st.text_input("Name")
        email = st.text_input("Email")
        if st.button("Login"):
            if name and email:
                st.session_state.user_name = name
                st.session_state.user_email = email
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.warning("Please enter both name and email.")

# --- Main Content ---
if st.session_state.logged_in:
    st.title("📝 AI-Based Task Manager")
    st.markdown("Manage your tasks efficiently with AI-powered insights.")

    # Task Input
    st.subheader("Add a Task")
    task_input = st.text_input("Enter your task command:", placeholder="e.g., 'Remind me to call John tomorrow at 10 AM'")
    if st.button("Add Task"):
        if task_input:
            parsed_task = llm_handler.parse_task(task_input)
            db.add_task(parsed_task['task'], parsed_task['category'], parsed_task['priority'], parsed_task['due_date'])
            st.success("Task added successfully!")
        else:
            st.warning("Task input cannot be empty.")

    # Display Tasks
    st.subheader("Your Tasks")
    tasks = db.get_tasks()
    if tasks:
        for task in tasks:
            st.markdown(f"""
                         <div class='task-card'>
                         <div class='task-title'>{task[1]}</div>
                         <div class='task-info'>Category: {task[2]} | Priority: {task[3]} | Due: {task[4]}</div>
                         <div class='task-actions'>
                         <button>Edit</button>
                         <button>Delete</button>
                         </div>
                         </div>""", unsafe_allow_html=True)
    else:
        st.info("No tasks found.")
else:
    st.markdown("<div style='background-color: rgb(0, 79, 153); padding: 20px; border-radius: 10px;'></div>", unsafe_allow_html=True)
    st.info("Please log in to access the task manager.")