#this program will use tkinter to make a gui program which chnages diffrent types of units
#importing tkinter
import tkinter as tk 
from tkinter import *
from tkinter import ttk
import conversion_storage #importing information from other file

#opening window
root = tk.Tk()
root.title('Unit Convertor')
root.configure(bg='#ccc')

#Making screen size unadjustable
root.resizable(width=False, height=False)

#lists, i have not moved to a diffrent file since they are better kept here
conversion_type = ['Length', 'Area', 'Mass']

conversion_options = [['Kilometer', 'Meter', 'Centimeter', 'Milimeter',
                      'Mile', 'Inch', 'Foot'],
                     ['Sq Kilometer', 'Sq Meter', 'Sq Mile',
                      'Sq Foot', 'Sq Inch', 'Acre'],
                     ['Tonne', 'Kilogram', 'Gram', 'Miligram', 'Pound']]



#clears the options on dropdowns 2 and 3
def clearOptions(eventObject):
    first_drop.set('')
    second_drop.set('')

#label showing title
typeLabel = Label(root, text='Please select type of conversion', bg='#cccccc')
typeLabel.grid(row=0, column=1, columnspan=2)
typeDrop = ttk.Combobox(root, width=40, value=(conversion_type))
typeDrop.set(conversion_type[0])
typeDrop.grid(row=1, column=1, columnspan=2)
typeDrop.bind("<<ComboboxSelected>>", clearOptions)

def callback(eventObject):
    abc = eventObject.widget.get()
    typeSelected = typeDrop.get()
    index = conversion_type.index(typeSelected)
    first_drop.config(values=conversion_options[index])
    second_drop.config(values=conversion_options[index])

#code for calculation of units
def calculateConversion(conversionType, from_unit_type, to_unit_type, value):
    val = float(value)
    if conversionType == 'Length':
        from_type_units = conversion_storage.length_conversions[from_unit_type][to_unit_type]
        new_value = val * float(from_type_units)
    if conversionType == 'Area':
        from_type_units = conversion_storage.area_conversion[from_unit_type][to_unit_type]
        new_value = val * float(from_type_units)
    if conversionType == 'Mass':
        from_type_units = conversion_storage.mass_conversions[from_unit_type][to_unit_type]
        new_value = val * float(from_type_units)

    outLabel.configure(text=new_value)

#design improvment for dropdowns
first_drop = ttk.Combobox(root, width=18)
first_drop.grid(row=2, column=1, columnspan=1)
first_drop.bind('<Button-1>', callback)

second_drop = ttk.Combobox(root, width=18)
second_drop.grid(row=2, column=2, columnspan=1)
second_drop.bind('<Button-1>', callback)

#code which allows user to enter value, a label
inputLabel = Label(root, text='Please enter value to covert: ', bg='#cccccc')
inputLabel.grid(row=3, column=1, columnspan=2)

valueEntry = Entry(root)
valueEntry.grid(row=4, column=1, columnspan=1)

#submit button which will start the code
submitButton = Button(root, text="Submit", command=lambda: calculateConversion(
    typeDrop.get(), first_drop.get(), second_drop.get(), valueEntry.get()))
submitButton.grid(row=4, column=2)

outLabel = Label(root, text='', bg='#cccccc')
outLabel.grid(row=5, column=1, columnspan=2)



root.mainloop()