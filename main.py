import PySimpleGUI as sg
import Creator
import sys
import os

def Run_VM():
    try:
        VMs = os.listdir("./VM/")
    except:
        sg.popup("No VM found")
        return
    vm_list = []
    for index in VMs:
        index = index.replace(".sh", "")
        vm_list += [index]
    vm_list_bar = sg.Combo(vm_list, font=("Arial", 16), expand_x=True, enable_events=True, readonly=True, key="-VMs-")
    sublayout = [ [sg.Text("Run VM")], [vm_list_bar], [sg.Button("Run")] ]
    subwindow = sg.Window("Run VM", element_justification='c').Layout(sublayout)
    while True:
        event, values = subwindow.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "Run":
            os.system("bash VM/" + values["-VMs-"] + ".sh")
            subwindow.close()
    return

layout = [
    [sg.Text("QEmui")],
    [sg.Button("Create VM")],
    [sg.Button("Run VM")],
    [sg.Button("Exit")]
]

def main():
    window = sg.Window("QEmui", element_justification='c').Layout(layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break;
        elif event == "Create VM":
            Creator.Creator()
        elif event == "Run VM":
            Run_VM()
        elif event == "Exit":
            sys.exit(0)

if __name__ == "__main__":
    main()
