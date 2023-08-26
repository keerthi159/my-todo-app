import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo=st.session_state["new_todo"] + "\n"
    #here todos is file.txt
    todos.append(todo)
    functions.write_todos(todos)

#session_state is some kind of dictioary
st.title("My Todo App")
st.subheader("this is my todo app.")


for index,  todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo" , placeholder="Add new todo:.." , on_change=add_todo, key="new_todo")
