#this program will use tkinter to make a gui program which chnages diffrent types of units
#importing tkinter
import tkinter as tk 
from tkinter import *
from tkinter import ttk
import conversion_storage #importing information from other file

#opening window
root = tk.Tk()
root.title('Unit Convertor')
root.configure(bg='#cccccc')

#lists, i have not moved to a diffrent file since they are better kept here
typeConversion = ['Length', 'Area', 'Mass']

conversionOptions = [['Kilometer', 'Meter', 'Centimeter', 'Milimeter',
                      'Mile', 'Inch', 'Foot'],
                     ['Sq Kilometer', 'Sq Meter', 'Sq Mile',
                      'Sq Foot', 'Sq Inch', 'Acre'],
                     ['Tonne', 'Kilogram', 'Gram', 'Miligram', 'Pound']]



#clears the options on dropdowns 2 and 3
def clearOptions(eventObject):
    firstDrop.set('')
    secondDrop.set('')

#label showing title
typeLabel = Label(root, text='Please select type of conversion', bg='#cccccc')
typeLabel.grid(row=0, column=1, columnspan=2)
typeDrop = ttk.Combobox(root, width=40, value=(typeConversion))
typeDrop.set(typeConversion[0])
typeDrop.grid(row=1, column=1, columnspan=2)
typeDrop.bind("<<ComboboxSelected>>", clearOptions)

def callback(eventObject):
    abc = eventObject.widget.get()
    typeSelected = typeDrop.get()
    index = typeConversion.index(typeSelected)
    firstDrop.config(values=conversionOptions[index])
    secondDrop.config(values=conversionOptions[index])

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
firstDrop = ttk.Combobox(root, width=18)
firstDrop.grid(row=2, column=1, columnspan=1)
firstDrop.bind('<Button-1>', callback)

secondDrop = ttk.Combobox(root, width=18)
secondDrop.grid(row=2, column=2, columnspan=1)
secondDrop.bind('<Button-1>', callback)

#code which allows user to enter value
inputLabel = Label(root, text='Please enter value to covert: ', bg='#cccccc')
inputLabel.grid(row=3, column=1, columnspan=2)

valueEntry = Entry(root)
valueEntry.grid(row=4, column=1, columnspan=1)

#submit button which will start the code
submitButton = Button(root, text="Submit", command=lambda: calculateConversion(
    typeDrop.get(), firstDrop.get(), secondDrop.get(), valueEntry.get()))
submitButton.grid(row=4, column=2)

outLabel = Label(root, text='', bg='#cccccc')
outLabel.grid(row=5, column=1, columnspan=2)











    




 


    



root.mainloop()