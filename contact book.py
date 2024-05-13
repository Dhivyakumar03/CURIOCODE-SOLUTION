from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('800x500')
root.title('Contact Book')
root.config(bg='orange')

contacts = []

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get()
    email = email_entry.get()
    if name!="":
        contacts.append((name, phone, email))
        messagebox.showinfo("Save", "Contacts Saves Successfully")
    name_entry.delete(0, "end")
    phone_entry.delete(0, "end")
    email_entry.delete(0, "end")
    update_listbox()

def remove_contact():
    selected = contact_listbox.curselection()
    if selected:
        index = selected[0]
        del contacts[0]
        update_listbox()
        Messagebox.showinfo("Deleted", "Contact Deleted Successfully")

def display_contact():
    for contact in contacts:
        messagebox.showinfo("Details","Name: "+contact[0]+
                            '\n'+"Phone: "+contact[1]+
                            '\n'+"Email: "+contact[2])

def update_listbox():
    contact_listbox.delete(0, "end")
    for contact in contacts:
        contact_listbox.insert("end", contact[0])

heading_label = Label(root, text="Contact Book", font=("Arial",30,"bold"), fg="white", bg="blue")
heading_label.place(x=300, y=3)

name_label = Label(root, text="Name:", font=("Arial",17,"bold"), fg="white", bg="blue")
name_label.grid(row=0, column=0)
name_label.place(x=80, y=70)

name_entry = Entry(root, font=("Arial",17,"bold"), width=20)
name_entry.grid(row=0, column=1)
name_entry.place(x=200,y=70)


phone_label = Label(root, text="Phone:", font=("Arial",17,"bold"), fg="white", bg="blue")
phone_label.grid(row=1, column=0)
phone_label.place(x=80, y=120)

phone_entry = Entry(root, font=("Arial",17,"bold"), width=20)
phone_entry.grid(row=1, column=1)
phone_entry.place(x=200,y=120)

email_label = Label(root, text="Email:", font=("Arial",17,"bold"), fg="white", bg="blue")
email_label.grid(row=1, column=0)
email_label.place(x=80, y=170)

email_entry = Entry(root, font=("Arial",17,"bold"), width=20)
email_entry.grid(row=1, column=1)
email_entry.place(x=200,y=170)

add_btn = Button(root, text="ADD CONTACT", command=add_contact, font=("Tahoma",13,"bold"), relief="raised", borderwidth=4, width=18, activeforeground="white", background="green", activebackground="dark green")
add_btn.grid(rowspan=1)
add_btn.place(x=50, y=280)

remove_btn = Button(root, text="REMOVE CONTACT", command=remove_contact, font=("Tahoma",13,"bold"), relief="raised", borderwidth=4, width=18, activeforeground="white", background="green", activebackground="dark green")
remove_btn.grid(rowspan=1)
remove_btn.place(x=50, y=330)

display_btn = Button(root, text="DISPLAY CONTACT", command=display_contact, font=("Tahoma",13,"bold"), relief="raised", borderwidth=4, width=18, activeforeground="white", background="green", activebackground="dark green")
display_btn.grid(rowspan=1)
display_btn.place(x=50, y=380)

contact_label = Label(root, text="CONTACT LIST", font=("Arial",20,"bold"), fg="white", bg="black")
contact_label.place(x=500, y=230)

contact_listbox = Listbox(root, font=("Arial",12), width=40)
contact_listbox.place(x=400, y=280)



            

        
    















root.mainloop()
