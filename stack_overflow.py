from tkinter import *

root = Tk()

def myBMI():
    weight = float(Entry.get(weight_field))
    height = float(Entry.get(height_field))
    bmi = (weight*703)/(height*height)
    top = Toplevel()
    msg = Label(top, text=bmi)
    msg.pack()

height_label = Label(root, text="Enter your height: ")
height_field = Entry(root)
height_field.grid(row=0, column=1)
height_label.grid(row=0, sticky=E)

weight_label = Label(root, text="Enter your weight: ")
weight_field = Entry(root)
weight_field.grid(row=1, column=1)
weight_label.grid(row=1, sticky=E)

compute_bmi = Button(root, text="Compute BMI", command=myBMI)
compute_bmi.grid(row=2)

root.mainloop()