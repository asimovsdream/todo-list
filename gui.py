import functions
import PySimpleGUI as sg
import time

sg.theme("DarkTeal4")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="to-do")
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit", size=10)

window = sg.Window('To-Do App',
                   layout=[[clock], [label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 10))

while True:
    event, value = window.read(timeout=200)  # refresh in every 200 miliseconds
    window["clock"].update(value=time.strftime("%d %b %Y, %A - %H:%M:%S"))
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value['to-do'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = value['todos'][0]
                new_todo = value['to-do'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Select an item to edit!", font=("Helvetica", 10))
        case "Complete":
            try:
                todo_to_complete = value['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['to-do'].update(value="")
            except IndexError:
                sg.popup("Select an item to complete!", font=("Helvetica", 10))
        case "Exit":
            break
        case 'todos':
            window['to-do'].update(value=value['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
