import numbers
from cgitb import text
import string
from tkinter import *
from tkinter import ttk
import math
from numbers import Number
import numpy as np
import pandas as pd
import numpy

"""
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
"""
def calc_hb(load,ball_diam,imprint_diam):
    return round((2*load)/(math.pi*ball_diam*(ball_diam-(math.sqrt(math.pow(ball_diam,2)-math.pow(imprint_diam,2))))),3)

def interpol(value,value_col,result_col):
    return np.interp(value,value_col,result_col)

def calc_hrc(hb, df, hb_col, hrc_col):
    return interpol(hb, df[hb_col], df[hrc_col])

def get_load_value():
    try:
        load_error_mess.set(str())
        load_entry_value=load_entry.get()
        load_value=float(load_entry_value)
        if load_value<=0:load_error_mess.set("Load must be positive")
        else:return load_value
    except:
        load_error_mess.set("Invalid value for load")

def get_ball_diam_value():
    try:
        ball_diam_error_mess.set(str())
        ball_diam_entry_value=ball_diam_entry.get()
        ball_diam_value=float(ball_diam_entry_value)
        if ball_diam_value <= 0: ball_diam_error_mess.set("Ball diameter must be positive")
        else: return ball_diam_value
    except:
        ball_diam_error_mess.set("Invalid value for ball diameter")

def get_imprint_diam_value():
    try:
        imprint_diam_error_mess.set(str())
        imprint_diam_entry_value=imprint_diam_entry.get()
        imprint_diam_value=float(imprint_diam_entry_value)
        if imprint_diam_entry_value <= 0: imprint_diam_error_mess.set("Imprint diameter must be positive")
        else: return imprint_diam_value
    except:
        imprint_diam_error_mess.set("Invalid value for imprint diameter")

df = pd.read_csv('hardness.csv', sep=',')
hb=calc_hb(3000,10,2)
hrc=calc_hrc(hb,df,'hb','hrc')

def hb_calc_click():
    load_value=get_load_value()
    ball_diam_value=get_ball_diam_value()
    imprint_diam_value=get_imprint_diam_value()
    print(f"{load_value}\n{ball_diam_value}\n{imprint_diam_value}")

print (hb)
print(hrc)

root = Tk()
root.title("Hardness calculation")
root.geometry("300x250+200+200")
root.attributes("-toolwindow", True)

load_error_mess=StringVar()
ball_diam_error_mess=StringVar()
imprint_diam_error_mess=StringVar()
hb_result_mess=StringVar()
hrc_result_mess=StringVar()

load_entry=ttk.Entry()
ball_diam_entry=ttk.Entry()
imprint_diam_entry=ttk.Entry()
hrc_entry=ttk.Entry()

hb_calc_button = ttk.Button(text="Calculate",command=hb_calc_click)
#hrc_calc_button = ttk.Button(text="Calculate",command=click_hrc_calc)

load_error_label=ttk.Label(textvariable=load_error_mess)
ball_diam_error_label=ttk.Label(textvariable=ball_diam_error_mess)
imprint_diam_error_label=ttk.Label(textvariable=imprint_diam_error_mess)
hb_result_label=ttk.Label(textvariable=hb_result_mess)
hrc_result_label=ttk.Label(textvariable=hrc_result_mess)

load_entry.pack()
ball_diam_entry.pack()
imprint_diam_entry.pack()
hb_calc_button.pack()
hrc_entry.pack()
#hrc_calc_button.pack()

root.mainloop()





