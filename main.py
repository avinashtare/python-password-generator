import tkinter as tk
from utils import *

strong_password = ""
def generate_password_handler():
    number_length_val = number_length.get()
    isNumberChar = var_numbers.get()
    isSpecialrChar = var_special.get()
    isUpercaseChar = var_uppercase.get()
    global strong_password
    strong_password = genrate_password(number_length_val,isNumberChar,isSpecialrChar,isUpercaseChar);
    if(strong_password):
        copy_box.delete(0,len(copy_box.get()))
        copy_box.insert(0,strong_password)
    

def copy_clicboard():
    root.clipboard_clear() 
    root.clipboard_append(strong_password) 
    root.update() 
    print(strong_password)

root = tk.Tk()

root.title("Strong Password Generator");
root.geometry("550x480+0+0")

heading = tk.Label(root, text="Welcome To Password Genrator",font=("Arial", 25))
heading.pack(pady=20)

var_numbers = tk.BooleanVar()
var_special = tk.BooleanVar()
var_uppercase = tk.BooleanVar()


# frame 
frame = tk.Frame(root, borderwidth=2, relief="groove")
frame.pack(padx=10, pady=30, fill="both", expand=True) 



# password entry
label = tk.Label(frame, text="Enter Length Of Password:", font=("Arial", 14))
label.grid(row=0, column=0, pady=(20,0))

number_length = tk.Entry(frame, width=25, font=("Arial", 12),relief="solid",borderwidth=2,fg="red",)
number_length.insert(0,"8")
number_length.grid(row=0, column=1, pady=(20,0), padx=0)




# check number wnat or not
label = tk.Label(frame, text="Do want numbers?:",justify="left", font=("Arial", 14))
label.grid(row=1, column=0, pady=(20,0))

checkbox = tk.Checkbutton(frame,justify="center",fg="blue",bd=0.1,relief="flat",font=40,variable=var_numbers)
checkbox.grid(row=1, column=1, pady=(20,0))




# check number wnat or not
label = tk.Label(frame, text="Includs special characters?:",justify="left", font=("Arial", 14))
label.grid(row=2, column=0, pady=(20,0))

checkbox = tk.Checkbutton(frame,justify="left",fg="blue",bd=0.1,relief="flat",font=40,variable=var_special)
checkbox.grid(row=2, column=1, pady=(20,0))



# check number wnat or not
label = tk.Label(frame, text="Includs uppercase letters?:",justify="left", font=("Arial", 14))
label.grid(row=3, column=0, pady=(20,0))

checkbox = tk.Checkbutton(frame,justify="left",fg="blue",bd=0.1,relief="flat",font=40,variable=var_uppercase)
checkbox.grid(row=3, column=1, pady=(20,0))


copy_box = tk.Entry(frame,justify="center", width=25, font=("Arial", 12),relief="solid",borderwidth=2,fg="red")
copy_box.grid(row=4, column=0, pady=(20,0), padx=0)

button_copy = tk.Button(frame,text="Copy",font=("Arial",12),relief="solid",cursor="hand2",command=copy_clicboard)
button_copy.grid(row=4, column=1, pady=(20,0))


# submit button
button_generate = tk.Button(frame,text="Generate Password",width=20,font=("Arial",14),relief="solid",cursor="hand2",background="#0d6efd",fg="#fff",borderwidth=1,command=generate_password_handler)
button_generate.grid(row=5, column=0, columnspan=2, pady=20,padx=(30,0))
root.mainloop()