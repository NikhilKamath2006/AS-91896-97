#this program will use tkinter to make a gui program which chnages diffrent types of units
#importing tkinter
import tkinter as tk 
from tkinter import *
from tkinter import ttk
import conversion_storage #importing information from other file

#opening new window 
root = Tk()
root.title("Unit Convertor")
root.geometry('600x700')

#color of window
root.configure(bg='white')

#list of types of possible conversions in the program
conversion_options = ['Distance','Liquid','Area','Temperature','Weight']

#List of all distance units
distance_conversion_Options = ['Kilometer', 'Meter', 'Centimeter', 'Milimeter',
'Mile', 'Inch', 'Feet']

# Size of the window
root.geometry( "600x200" )
clicked = StringVar()

# The deafault option shown when dropdown is not clicked
clicked.set( "Distance" )

#Code for the dropdown 
drop = OptionMenu( root , clicked , *conversion_options )
drop.pack()

#Possible conversion Units if chosen conversion is Length
distance_units = ['Kilometer', 'Meter', 'Centimeter', 'Milimeter','Mile', 'Inch', 'Foot']






 


    



root.mainloop()