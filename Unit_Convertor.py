#this program will use tkinter to make a gui program which chnages diffrent types of units
#importing tkinter
import tkinter as tk 
from tkinter import *
from tkinter import ttk

#opening new window 
root = Tk()
root.title("Unit Convertor")
root.geometry('600x700')

#Function for new window when user wants length conversion
def length_window():
    top = Toplevel()
    top.title("Unit Convertor")
    top.geometry("400x400")   
b1 = Button(root, text="Distance", command=length_window)
b1.place(x=150, y=150)

#Function for new window when user wants liquid conversion
def liquid_window():
    top = Toplevel()
    top.title("Unit Convertor")
    top.geometry("400x400")   
b2 = Button(root, text="Distance", command=liquid_window)

#Function for new window when user wants area conversion
def area_window():
    top = Toplevel()
    top.title("Unit Convertor")
    top.geometry("400x400")   
b3 = Button(root, text="Distance", command=area_window)

#Function for new window when user wants tmperature conversion
def temperature_window():
    top = Toplevel()
    top.title("Unit Convertor")
    top.geometry("400x400")   
b4 = Button(root, text="Distance", command=temperature_window)

#Function for new window when user wants weight conversion
def weight_window():
    top = Toplevel()
    top.title("Unit Convertor")
    top.geometry("400x400")   
b5 = Button(root, text="Distance", command=weight_window)

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



#Possible conversion Units if chosen conversion is Length
lengths_units = ['Kilometer', 'Meter', 'Centimeter', 'Milimeter','Mile', 'Inch', 'Foot']

#Dictionary of Length conversion rates
    









root.mainloop()