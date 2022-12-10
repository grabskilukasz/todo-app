
import PySimpleGUI as sg


label = sg.Text("Typein a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My TO-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()