from tkinter import *


def calculate():
    output = float(mile_input.get()) * 1.609
    km_output.config(text=output)


FONT = ("Arial", 14, "normal")

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=300)
window.config(padx=100, pady=100)

# mile label
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

# km label
km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

# is equal label
equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)

# click button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

# mile entry
mile_input = Entry(width=10)
mile_input.grid(column=1, row=0)

# km output
km_output = Label(text=0, font=FONT)
km_output.grid(column=1, row=1)

window.mainloop()
