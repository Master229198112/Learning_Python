from module import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

# window = sg.Window('Master To-Do App', layout=[[label, input_box]])
# for text and input box in separate row use below line
window = sg.Window('Master To-Do App', layout=[[label], [input_box, add_button]])

window.read()
window.close()
