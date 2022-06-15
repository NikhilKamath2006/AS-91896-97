#this program will use tkinter to make a gui program which chnages diffrent types of units
#importing tkinter
import tkinter as tk 
from tkinter import *
from tkinter import ttk

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

#Dictionary of Length conversion rates
distance_formulas = {
    "Kilometer": {"Kilometer": 1, "Meter": 1000, "Centimeter": 100000,
                  "Milimeter": 1000000, "Mile": 1/1.609, "Inch": 39370, "Foot": 3281},
    "Meter": {"Kilometer": 1/1000, "Meter": 1, "Centimeter": 100,
              "Milimeter": 1000, "Mile": 1/1609, "Inch": 39.37, "Foot": 3.281},
    "Centimeter": {"Kilometer": 1/100000, "Meter": 1/100, "Centimeter": 1,
                   "Milimeter": 10, "Mile": 1/160934, "Inch": 1/2.54, "Foot": 1/30.48},
    "Milimeter": {"Kilometer": 1/1000000, "Meter": 1/1000, "Centimeter": 1/10,
                  "Milimeter": 1, "Mile": 1/1609340, "Inch": 1/25.4, "Foot": 1/305},
    "Mile": {"Kilometer": 1.609, "Meter": 1609, "Centimeter": 160934,
             "Milimeter": 1609340, "Mile": 1, "Inch": 63360, "Foot": 5280},
    "Inch": {"Kilometer": 1/39370, "Meter": 1/39.37, "Centimeter": 2.54,
             "Milimeter": 25.4, "Mile": 1/63360, "Inch": 1, "Foot": 1/12},
    "Foot": {"Kilometer": 1/3281, "Meter": 1/3.281, "Centimeter": 30.48,
             "Milimeter": 304.8, "Mile": 1/5280, "Inch": 12, "Foot": 1}
}




 


    



root.mainloop()