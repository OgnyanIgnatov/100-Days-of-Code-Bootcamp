from tkinter import *

window = Tk()
window.title("Mile -> Km")
window.minsize(width=300, height=200)
window.config(padx=5, pady=5)

#Labels
miles_label = Label(text="Miles", font=("Courier", 12, "bold"))
miles_label.grid(row=0, column=2)
miles_label.config(padx=5,pady=5)

km_label = Label(text="Km", font=("Courier", 12, "bold"))
km_label.grid(row=1, column=2)
km_label.config(padx=5,pady=5)

equal_label = Label(text="is equal to", font=("Courier", 12, "bold"))
equal_label.grid(row=1,column=0)
equal_label.config(padx=5,pady=5)

#Inputs/Outputs

to_convert = Entry(width=10)
to_convert.grid(row=0,column=1)

converted = Label(text="", font=("Courier", 12, "bold"))
converted.grid(row=1,column=1)
converted.config(padx=5,pady=5)

#Button

def calculate():
    kms=float(to_convert.get())*1.6
    converted.config(text=f"{kms:.2f}")

button = Button(text="Calculate", bg="white", width=10, command=calculate)
button.grid(row=2,column=1)






window.mainloop()