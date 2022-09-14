from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

entry = Entry(width=10)
entry.grid(column=1, row=0)

entry_2 = Entry(width=10)
entry_2.grid(column=1, row=1)


def click_button():
    miles = entry.get()
    mile_count = float(miles)
    km = mile_count / 5 * 8
    entry_2.insert(END, string=f"{km}")



button = Button(text="Calculate", command=click_button)
button.grid(column=1, row=2)

window.mainloop()


