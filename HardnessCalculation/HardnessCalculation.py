import numbers
from cgitb import text
import string
from tkinter import *
from tkinter import ttk
import math
from numbers import Number
import numpy as np
import pandas as pd

def load_validate(load_input):
    load_error_mess.set(str())
    if load_input in numbers:
        if load_input<=0:
            load_error_mess.set("Load must be positive")
        else:
            return load_input
    else:
        load_error_mess.set("Invalid value for load")

def ball_validate(ball_input):
    ball_error_mess.set(str())
    if ball_input in numbers:
        if ball_input <= 0:
            ball_error_mess.set("Ball diameter must be positive")
        else:
            return ball_input
    else:
        ball_error_mess.set("Invalid value for ball diameter")

def trace_validate(trace_input):
    trace_error_mess.set(str())
    if trace_input in numbers:
        if trace_input <= 0:
            trace_error_mess.set("Trace diameter must be positive")
        else:
            return trace_input
    else:
        trace_error_mess.set("Invalid value for trace diameter")

def hb_validate(hb_input):
    hb_error_mess.set(str())
    if hb_input in numbers:
        if hb_input <= 0:
            trace_error_mess.set("HB value must be positive")
        else:
            return hb_input
    else:
        trace_error_mess.set("Invalid value for HB")















def get_hb(path):
    try: return pd.read_csv(path, sep=',')
    except: hrc_result_mess.set("Could not read the file 'hardness.csv'")

def calc_hb(load,ball_diam,imprint_diam):
    return round((2*load)/(math.pi*ball_diam*(ball_diam-(math.sqrt(math.pow(ball_diam,2)-math.pow(imprint_diam,2))))),3)

def  calc_hrc(hb):
    try:
        df = get_hb('hardness.csv')
        hb_max=df['hb'].max()
        hb_min=df['hb'].min()
        print(hb,hb_min,hb_max)
        if hb<hb_min:hrc_result_mess.set(f"Brinell hardness value less than {hb_min} HB,\nRockwell hardness undefined")
        elif hb>hb_max:hrc_result_mess.set(f"Brinell hardness value more than {hb_max} HB,\nRockwell hardness undefined")
        else: return interpol(hb,df['hb'],df['hrc'])
    except:
        hrc_result_mess.set("Undefined")

def interpol(value,value_col,result_col):
    return np.interp(value,value_col,result_col)

def get_hb_value():
    try:
        hrc_result_mess.set(str())
        hb=hrc_entry.get()
        hb_value=float(hb)
        if hb_value<=0:hrc_result_mess.set("HB value must be positive")
        else:return hb_value
    except:hrc_result_mess.set("Invalid value for HB")

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
        if imprint_diam_value <= 0: imprint_diam_error_mess.set("Imprint diameter must be positive")
        else: return imprint_diam_value
    except:
        imprint_diam_error_mess.set("Invalid value for imprint diameter")

def hb_calc_click():
    load_value=get_load_value()
    ball_diam_value=get_ball_diam_value()
    imprint_diam_value=get_imprint_diam_value()
    try:
        hb_value=calc_hb(load_value,ball_diam_value,imprint_diam_value)
        hb_result_mess.set(f"{hb_value} HB")
        hrc_entry.delete(0,END)
        hrc_entry.insert(0, hb_value)
    except:
        hb_result_mess.set("Undefined")

def hrc_calc_click():
    hb_value=get_hb_value()
    try:
        hrc_value=calc_hrc(hb_value)
        hrc_result_mess.set(f"{hrc_value} HRC")
    except:
        hrc_result_mess.set("Undefined")

root = Tk()
root.title("Hardness calculation")
root.geometry("300x250+200+200")
root.attributes("-toolwindow", True)

load_entry=ttk.Entry()
load_entry.insert(0,"Enter load")
load_entry.pack()

ball_entry=ttk.Entry()
ball_entry.insert(0,"Enter ball diameter")
ball_entry.pack()

trace_entry=ttk.Entry()
trace_entry.insert(0,"Enter trace diameter")
trace_entry.pack()

hb_calc_button = ttk.Button(text="Calculate HB",command=hb_calc_click)
hb_calc_button.pack()

hb_result_mess=StringVar()
hb_result_label=ttk.Label(textvariable=hb_result_mess)
hb_result_label.pack()

load_error_mess=StringVar()
load_error_label=ttk.Label(textvariable=load_error_mess)
load_error_label.pack()

ball_error_mess=StringVar()
ball_error_label=ttk.Label(textvariable=ball_error_mess)
ball_error_label.pack()

trace_error_mess=StringVar()
trace_error_label=ttk.Label(textvariable=trace_error_mess)
trace_error_label.pack()

hb_entry=ttk.Entry()
hb_entry.insert(0,"Enter HB")
hb_entry.pack()

hrc_calc_button = ttk.Button(text="Calculate HRC",command=hrc_calc_click)
hrc_calc_button.pack()

hrc_result_mess=StringVar()
hrc_result_label=ttk.Label(textvariable=hrc_result_mess)
hrc_result_label.pack()

hb_error_mess=StringVar()
hb_error_label=ttk.Label(textvariable=hb_error_mess)
hb_error_label.pack()

root.mainloop()





