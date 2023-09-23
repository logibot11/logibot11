#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tkinter as tk
 
window = tk.Tk()
window.title('Tkinter - ListBox')
 
window.geometry('500x300')
 
var1 = tk.StringVar()
l = tk.Label(window, bg='green', fg='yellow',font=('Arial', 12), width=25, textvariable=var1)
l.pack()


 
def print_selection():
    value = lb.get(lb.curselection())   
    var1.set(value)  
 
b1 = tk.Button(window, text='print selection', width=25, height=2, command=print_selection)
b1.place(x=5, y=5, relwidth=1, relheight=1, width=-10, height=-10)
b1.pack()
 
var2 = tk.StringVar()
var2.set((1,2,3,4))
lb = tk.Listbox(window, listvariable=var2)

list_items = [11,22,33,44]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'Rogatka 1')
lb.insert(2, 'Rogatka_2')
lb.insert(3, 'Sw_Kranc_Grp1')
#lb.delete(2)
lb.pack()
 
window.mainloop()