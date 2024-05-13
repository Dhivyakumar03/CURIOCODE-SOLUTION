from tkinter import *
import random, string

root = Tk()
root.geometry("400x280")
root.title("PASSWORD GENERATOR")

title = StringVar()
label = Label(root, textvariable=title).pack()
title.set("Password Strength")

def selection():
    global selection
    selection = choice.get()


choice = IntVar()
r1 = Radiobutton(root, text="POOR", variable=choice, value=1, command=selection).pack(anchor=CENTER)
r2 = Radiobutton(root, text="AVERAGE", variable=choice, value=2, command=selection).pack(anchor=CENTER)
r3 = Radiobutton(root, text="STRONG", variable=choice, value=3, command=selection).pack(anchor=CENTER)

labelchoice = Label(root)
labelchoice.pack()

pass_length = StringVar()
pass_length.set("Password Length")
len_title = Label(root, textvariable=pass_length).pack()

val = IntVar()
spin_length = Spinbox(root, from_=8, to_=24, textvariable=val, width=13).pack()

def callback():
    len_sum.config(text=pass_gen())

pass_gen_btn = Button(root, text="Generate Password", bd=5, height=2, command=callback)
pass_gen_btn.pack(pady=20)
password = str(callback)

len_sum = Label(root, text="Password Here", font=("arial", 20))
len_sum.pack(side=BOTTOM, anchor="n")

poor = string.ascii_uppercase+string.ascii_lowercase
average = string.ascii_uppercase+string.ascii_lowercase+string.digits

symbols = """ '~!@#$%^&*()+=/?<>.:;\ """

strong = poor+average+symbols

def pass_gen():
    if choice.get()==1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get()==2:
        return "".join(random.sample(average, val.get()))
    elif choice.get()==3:
        return "".join(random.sample(strong, val.get()))
        
        



root.mainloop()
