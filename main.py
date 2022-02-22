import PySimpleGUI as sg
from person import Person
import matplotlib.pyplot as plt 
import numpy as np 




def main():
    sg.theme('DarkTeal4')

    

    layout = [
        [sg.Text(text="Create new person")],
        [sg.Button(button_text='CREATE'), sg.Button('SHOW DATA'), sg.Button('Cancel')]
    ]

    window = sg.Window("Human Horesepower", layout, default_element_size=(
        12, 1), default_button_element_size=(12, 1))

    while True:
        event, values = window.read()

        if event == "CREATE":
            createNew()

        if event == "SHOW DATA":
            plt.scatter(xPoints, yPoints)
            plt.show()    

        if event == "Cancel" or event == sg.WIN_CLOSED:
            break

    window.close()


def createNew():
    sg.theme('DarkTeal4')

    personLayout = [
        [sg.Text("Input Height, Wieght")],
        [sg.Text("Weight (lbs)", size=(15, 1)), sg.InputText()],
        [sg.Text("Time (seconds)", size=(15, 1)), sg.InputText()],
        [sg.Text("Average Step (inches)", size=(15, 1)), sg.InputText()],
        [sg.Text("Total number of steps", size=(15, 1)), sg.InputText()],
        [sg.Button(button_text="Calculate"),
         sg.Text(size=(40, 1), key='AGAIN')],
        [sg.Text("HORSEPOWER:"), sg.Text(size=(50, 1),
                                         key='-OUTPUT-'), sg.Button("Submit")]
    ]

    window = sg.Window("Create New", personLayout)

    while True:
        event, values = window.read()

        if event == "Calculate":

            # add something to like make sure the input is right
            if values[0].isnumeric() and values[1].isnumeric() and values[2].isnumeric() and values[3].isnumeric():

                # do stuff to person and then change
                person = Person(values[0], values[1], values[2], values[3])

                horsepower = person.horsepower()

                window["AGAIN"].update(str(""))
                window["-OUTPUT-"].update(str(horsepower))

                global xPoints
                global yPoints

                yPoints += horsepower
                xPoints += person.time

            else:
                window["AGAIN"].update(
                    str("make sure to enter values correctly"))

        if event == "Submit":
            # store in sheet & add to graph or whatever

            with open('data.txt', 'a') as writer:

                writer.write("HP" + str(horsepower))
                writer.write("\n")

            break  

        if event == sg.WIN_CLOSED:
            break

    window.close()


if __name__ == "__main__":


    xPoints = np.array([])
    yPoints = np.array([])

    

    main()
