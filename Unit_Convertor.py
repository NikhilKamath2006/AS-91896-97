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





    




 


    



root.mainloop()