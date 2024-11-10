from cgitb import text
import string
from tkinter import *
from tkinter import ttk
import math
import pandas
import numpy

def clear_error_messages():
    power_error_message.set("")
    ball_error_message.set("")
    imprint_error_message.set("")

def get_power():
    try:
        power=float(power_entry.get())
        return power
    except:
        power_error_message.set("Invalid value for power")

def get_ball():
    try:
        ball=ball_entry.get()
        return float(ball)
    except:
        ball_error_message.set("Invalid value for ball diameter")    

def get_imprint():
    try:
        imprint=imprint_entry.get()
        return float(imprint)
    except:
        imprint_error_message.set("Invaid value for imprint diameter")    

def calculate(power,ball,imprint):
    try:
        if power<=0: power_error_message.set("Power must be positive")
        elif ball<=0:ball_error_message.set("Ball diameter must be positive")
        elif imprint<=0:imprint_error_message.set("Imprint diameter must be positive")
        else:
            clear_error_messages()
            if imprint<(0.24*ball):imprint_error_message.set("Imprint diameter less than 0.24*D,\nneed to increase the load")
            elif imprint>(0.6*ball):imprint_error_message.set("Imprint diameter more than 0.6*D,\nneed to reduce the load")
            hardness=round((2*power)/(math.pi*ball*(ball-(math.sqrt(math.pow(ball,2)-math.pow(imprint,2))))),3)
            return hardness
    except:
        hardness_message.set("No result")    

def click():
    power=0.0
    ball=0.0
    imprint=0.0
    hardness=0.0

    power=get_power()
    ball=get_ball()
    imprint=get_imprint()
    hardness=calculate(power,ball,imprint)
    hardness_message.set(f"{hardness} HB")

root = Tk()
root.title("Hardness calculation")
root.geometry("300x250+200+200")
root.attributes("-toolwindow", True)

power_error_message=StringVar()
ball_error_message=StringVar()
imprint_error_message=StringVar()
hardness_message=StringVar()

calculate_button = ttk.Button(text="Calculate",command=click)
power_entry=ttk.Entry()
ball_entry=ttk.Entry()
imprint_entry=ttk.Entry()

power_entry.pack()
ball_entry.pack()
imprint_entry.pack()
calculate_button.pack()

hb_hardness_label=ttk.Label(textvariable=hardness_message)
hb_hardness_label.pack()

power_error_label=ttk.Label(textvariable=power_error_message)
ball_error_label=ttk.Label(textvariable=ball_error_message)
imprint_error_label=ttk.Label(textvariable=imprint_error_message)

power_error_label.pack()
ball_error_label.pack()
imprint_error_label.pack()

root.mainloop()