from tkinter import *
from tkinter import ttk
import math
import numpy as np
import pandas as pd
from PIL import Image, ImageTk

def interpol(value,value_col,result_col):
    return np.interp(value,value_col,result_col)

def calc_hb(load, ball, trace):
    return round((2*load) / (math.pi * ball * (ball - (math.sqrt(math.pow(ball, 2) - math.pow(trace, 2))))), 3)

def calc_hrc(hb,df):
    return round(interpol(hb,df['hb'],df['hrc']),3)

def validate_load(load_input):
    if load_input <= 0:
        load_error_mess.set("Load must be positive.")
    else:
        return load_input

def validate_ball(ball_input):
    if ball_input <= 0:
        ball_error_mess.set("Ball diameter must be positive.")
    else:
        return ball_input

def validate_trace(trace_input):
    if trace_input <= 0:
        trace_error_mess.set("Trace diameter must be positive.")
    else:
        return trace_input

def validate_hb(hb_input):
    if hb_input <= 0:
        hb_error_mess.set("HB value must be positive.")
    else:
        return hb_input

def get_df(path):
    try:
        return pd.read_csv(path, sep=',')
    except:
        df_error_mess.set(f"Can't read {path}.")

def read_load():
    return load_entry.get()

def read_ball():
    return ball_entry.get()

def read_trace():
    return trace_entry.get()

def read_hb():
    return hb_entry.get()

def get_load_value():
    load_error_mess.set(str())
    entry_value=read_load()
    try:
        value=float(entry_value)
        return validate_load(value)
    except:
        load_error_mess.set("Invalid value for load.")

def get_ball_value():
    ball_error_mess.set(str())
    entry_value=read_ball()
    try:
        value = float(entry_value)
        return validate_ball(value)
    except:
        ball_error_mess.set("Invalid value for ball.")

def get_trace_value():
    trace_error_mess.set(str())
    entry_value=read_trace()
    try:
        value = float(entry_value)
        return validate_trace(value)
    except:
        trace_error_mess.set("Invalid value for trace.")

def get_hb_value():
    hb_error_mess.set(str())
    entry_value=read_hb()
    try:
        value = float(entry_value)
        return validate_hb(value)
    except:
        hb_error_mess.set("Invalid value for HB.")

root = Tk()
root.title("Hardness calculation")
root.geometry("500x400+200+200")
root.attributes("-toolwindow", True)

hb_result_mess=StringVar()
load_error_mess=StringVar()
ball_error_mess=StringVar()
trace_error_mess=StringVar()
hrc_result_mess=StringVar()
hb_error_mess=StringVar()
df_error_mess=StringVar()

def calc_hb_click():
    load=get_load_value()
    ball=get_ball_value()
    trace=get_trace_value()
    try:
        hb=calc_hb(load,ball,trace)
        hb_result = validate_hb(hb)
        hb_result_mess.set(f"{hb_result} HB")
        hb_entry.delete(0,END)
        hb_entry.insert(0, hb_result)
        if trace<=(0.24*ball):trace_error_mess.set("Trace diameter less than 0.24*D,\nincrease the load.")
        elif trace>0.6*ball:trace_error_mess.set("Trace diameter more than 0.6*D,\nreduce the load.")
    except:
        if ball<trace:
            hb_result_mess.set("Ball diameter should be more than trace diameter,\ncheck the correctness of your input.")
        else:
            hb_result_mess.set("Can't calculate.")

def calc_hrc_click():
    hb=get_hb_value()
    df=get_df('./hardness.csv')
    hb_max = df['hb'].max()
    hb_min = df['hb'].min()
    hrc_result = calc_hrc(hb, df)
    if math.isnan(hrc_result):
        hrc_result_mess.set("Can't calculate.")
    elif hb<hb_min:
        hrc_result_mess.set(f"HB should be more than or equal to {hb_min}.\nCan't calculate.")
    elif hb>hb_max:
        hrc_result_mess.set(f"HB should be less than or equal to {hb_max}.\nCan't calculate.")
    else:
        hrc_result_mess.set(f"{hrc_result} HRC")

try:
    image=Image.open("logo.png")
    resize_image=image.resize((350,75))
    img=ImageTk.PhotoImage(resize_image)
    logo_label=ttk.Label(image=img)
    logo_label.pack()
except:
    print("error")

load_entry=ttk.Entry()
load_entry.insert(0,"Enter load.")
load_entry.pack()

ball_entry=ttk.Entry()
ball_entry.insert(0,"Enter ball diameter.")
ball_entry.pack()

trace_entry=ttk.Entry()
trace_entry.insert(0,"Enter trace diameter.")
trace_entry.pack()

hb_calc_button = ttk.Button(text="Calculate HB",command=calc_hb_click)
hb_calc_button.pack()

hb_result_label=ttk.Label(textvariable=hb_result_mess)
hb_result_label.pack()

load_error_label=ttk.Label(textvariable=load_error_mess)
load_error_label.pack()

ball_error_label=ttk.Label(textvariable=ball_error_mess)
ball_error_label.pack()

trace_error_label=ttk.Label(textvariable=trace_error_mess)
trace_error_label.pack()

hb_entry=ttk.Entry()
hb_entry.insert(0,"Enter HB.")
hb_entry.pack()

hrc_calc_button = ttk.Button(text="Calculate HRC",command=calc_hrc_click)
hrc_calc_button.pack()

hrc_result_label=ttk.Label(textvariable=hrc_result_mess)
hrc_result_label.pack()

hb_error_label=ttk.Label(textvariable=hb_error_mess)
hb_error_label.pack()

df_error_label=ttk.Label(textvariable=df_error_mess)
df_error_label.pack()

root.mainloop()





