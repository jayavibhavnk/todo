import streamlit as st

# Initialize the global to-do list
todo_list = []

st.title("To-Do App")

# Input field to add a new task
new_task = st.text_input("Enter a new task:")
if st.button("Add Task") and new_task:
    todo_list.append({"task": new_task, "done": False})

# Display the to-do list
st.write("## To-Do List")
for i, task in enumerate(todo_list):
    checkbox = st.checkbox(label=task["task"], value=task["done"], key=i)
    todo_list[i]["done"] = checkbox

# Clear the completed tasks
if st.button("Clear Completed Tasks"):
    todo_list = [task for task in todo_list if not task["done"]]
