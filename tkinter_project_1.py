from tkinter import *
import time

root = Tk()
root.title('Unit conversion tool')
root.configure(bg='light gray')
root.geometry("300x120")
root.resizable(0,0)


def convert():
    """
    Takes user input and converts feet to meters. Returns an error statement
    if a non float value is entered.
    note - 3.281 ft = 1.0 m
    """
    
    try:
        value = float(entry_1.get())
        meters = int(0.3048  * value * 10000.0 +0.5)/10000.0
        label_3 = Label(
            root, 
            fg = '#000000',
            bg = 'light gray',
            text = meters,
            )
        label_3.grid(row=1, column = 0)
        time.sleep(3)

    except:
        label_3 = Label(
            root, 
            fg = '#000000',
            bg = 'light gray',
            text = "Invalid Entry",
            )
        label_3.grid(row=1, column = 0)

def clear_box():
    """Clears the calculated data box when executing next calculation."""
    label_3.config(text=" ")

#Label characteristics

label_1 = Label(
    root, 
    padx = 0, 
    pady = 10,
    width = 15,
    anchor = 'w',
    bg = 'light gray',
    text = "Value in feet",
    )
label_1.grid(row=0,column=1)

label_2 = Label(
    root, 
    padx = 0, 
    pady = 10,
    width = 15,
    anchor = 'w',
    bg = 'light gray',
    text = "Value in meters",
    )
label_2.grid(row=1,column=1)

label_3 = Label(
    root, 
    bg = 'light gray',
    text = " ",
    )
label_3.grid(row=1, column = 0)

#Entry bar characteristics

entry_1 = Entry(root, width = 20)
entry_1.grid(row = 0,column = 0)

#Button characteristics

button_1 = Button(
    root, 
    padx = 50,
    pady = 5,
    text = "Calculate",
    command = convert,
    )
button_1.grid(row=3,column=0)

button_2 = Button(
    root, 
    padx = 50,
    pady = 5,
    text = "Quit",
    command = root.destroy,
      )
button_2.grid(row=3,column=1)

#Run the application
root.mainloop()