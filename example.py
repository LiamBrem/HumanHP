# only use this as a reference 
# DELETE LATER!!!!!

import PySimpleGUI as sg 
from person import Person


if __name__ == "__main__":
    count = 0

    sg.theme('DarkTeal4')

    layout = [
        [sg.Text(text="Click the button to increase the count")],
        [sg.Button('BUTTON'), sg.Button('Cancel')],
        [sg.Text(size=(50,1), key='-OUTPUT-')]       
        ]


    window = sg.Window("Demo", layout, margins = (300, 200))

    while True:
        event, values = window.read()

        if event == "BUTTON":
            count += 1

        if event == "Cancel" or event == sg.WIN_CLOSED:
            break

        window['-OUTPUT-'].update("Number of clicks: " + str(count))   


    window.close()    