#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
import subprocess


window=Tk()

params={
    'padx':150,
    'pady':2,
    'bd':2,
    'fg':'white',
    'bg':'#999999',
    'font':('arial',16),
    'width':2,
    'height':2,
    'relief':'flat',
    'activebackground':'#666666'
}

def mac_changer():
    subprocess.call(["sudo", "ifconfig", interface.get(), "down"])
    subprocess.call(["sudo", "ifconfig", interface.get(), "hw", "ether", new_mac.get()])
    subprocess.call(["sudo", "ifconfig", interface.get(), "up"])
    error()

def error():
    if not interface.get():
        messagebox.showinfo("Error", "Please specify an interface.")
    elif not new_mac.get() or len(new_mac.get())!=17:
        messagebox.showinfo("Error", "Please specify a valid MAC address")

def success():
    if not interface.get() or not new_mac.get() or len(new_mac.get())!=17:
        e5.configure(text=" ")
    else:
        e5.config(text="MAC address of " + interface.get() + " has been changed to " + new_mac.get())

e1=Label(window, text="Enter name of interface: ", **params)
e1.grid(row=0, column=0)

interface=StringVar()
e2=Entry(window, textvariable=interface, font=('arial',16), justify='center', width=27, relief='ridge', bg='#999999', fg='white')
e2.grid(row=0, column=1, ipady=14)

e3=Label(window, text="Enter new MAC address: ", **params)
e3.grid(row=1, column=0)

new_mac=StringVar()
e4=Entry(window, textvariable=new_mac, font=('arial',16), justify='center', width=27, relief='ridge', bg='#999999', fg='white')
e4.insert(0,"00:00:00:00:00:00")
e4.configure(state=DISABLED, bg='#999999')
e4.grid(row=1, column=1, ipady=14)

def on_click4(event):
    e4.configure(state=NORMAL)
    e4.delete(0, END)
    e4.unbind('<Button-1>', on_click_id)

on_click_id=e4.bind('<Button-1>', on_click4)

e5=Label(window, text=" ", **params)
e5.configure(width=30)
e5.grid(row=2, columnspan=2)

e6=Button(window, text="Exit", command=window.destroy, **params)
e6.configure(bg='#8b0000', activebackground='#ffcccb')
e6.grid(row=3,column=0)

e7=Button(window, text="Convert", command=lambda:[mac_changer(),success()], **params)
e7.grid(row=3, column=1)


window.resizable(False,False)
window.title("MAC Changer")
window.mainloop()