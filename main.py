from js import document
from pyodide.ffi import create_proxy  # Import create_proxy to handle function references

# List to hold tasks
todo_items = []

# Function to add task
def add_todo_item(event):
    new_task = document.getElementById("new-todo").value
    if new_task:
        todo_items.append(new_task)
        render_todo_list()
        document.getElementById("new-todo").value = ""

# Function to delete task
def delete_todo_item(event, index):
    print("hello", index)
    del todo_items[index]
    render_todo_list()

# Function to render the todo list
def render_todo_list():
    todo_list_element = document.getElementById("todo-list")
    todo_list_element.innerHTML = ""  # Clear current list
    
    # Create list items
    for index, item in enumerate(todo_items):
        li = document.createElement("li")
        li.className = "todo-item"
        
        # Create delete button
        delete_btn = document.createElement("button")
        delete_btn.className = "btn btn-delete"
        delete_btn.innerHTML = "Delete"
        
        # Bind the delete_todo_item function to the button click event
        delete_proxy = create_proxy(lambda event, idx=index: delete_todo_item(event, idx))
        delete_btn.addEventListener("click", delete_proxy)
        
        # Append item and delete button to the list item
        li.innerHTML = item
        li.appendChild(delete_btn)
        
        # Append list item to the todo list
        todo_list_element.appendChild(li)

# Create a proxy for the add_todo_item function
add_todo_proxy = create_proxy(add_todo_item)

# Add event listener to the "Add Task" button
document.getElementById("add-todo").addEventListener("click", add_todo_proxy)

