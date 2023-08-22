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
st.write("this app is to increase your productivity")

for index,  todo in enumerate(todos):
    checkbox=st.checkbox(todo, key=todo)#we have to give todo as a key as it gives access to whole list
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo" , placeholder="Add new todo:.." , on_change=add_todo, key="new_todo")
#the argument on_change  is a callback function custom function created add_todo is a name of the function

#st.session_state # a specific object type of streamlit





