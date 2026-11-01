from tkinter import *

#defining the window
top = Tk()
top.config(background="lightblue")
top.geometry("450x300")
top.title("Login")

#defining the labels
user_name = Label(top,text="Username").place(x=40,y=50)
user_password = Label(top,text="Password",).place(x=40,y=100)

#defining the input boxes
user_name_entry_box = Entry(top,width=35).place(x=110, y=50)
user_password_input_box = Entry(top,width=35).place(x=110,y=100)

#defining the submit button
submit_button = Button(top,text="Log in",bd=5,background="white")
submit_button.place(x=50,y=140)

top.mainloop()