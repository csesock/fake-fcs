import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox
import time

window = tk.Tk()
window.geometry('323x143')
window.title('Itron Field Collection System')
window.attributes('-toolwindow', True)

##style = ttk.Style()
##style.theme_create('appstyle', settings={'TLabelframe': {'configure': {'bordercolor': 'red',
##                                                                       'relief': 'solid'}}})
##style.theme_use('appstyle')

def cancel():
    window.destroy()

def okay():
    r = random.randint(1, 5)
    if r == 0:
        for i in range(20):
            with open(str(i)+'.txt', 'w') as builtfile:
                a = random.randint(1, 100000000)
                builtfile.write(str(a))
    if r == 1:
        tk.messagebox.showerror(title="Warning", message="Nothing to save in current tab")
    if r == 3:
        window.destroy()
    if r == 4:
        tk.messagebox.showerror(title="ERROR MSSQLSERVER_18456", message="18456 Login failed for user")
    if r == 5:
        time.sleep(random.randint(1, 5))
        window.destroy()
    

entry_frame = tk.LabelFrame(window, text="Please Provide Your User Name and Password")
entry_frame.place(x=8, y=5)

user_name_label = ttk.Label(entry_frame, text="User Name:")
user_name_label.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")

password_label = ttk.Label(entry_frame, text="Password:")
password_label.grid(row=1, column=0, padx=6, pady=4, sticky="nsew")

user_name_entry = ttk.Entry(entry_frame, width=37)
user_name_entry.grid(row=0, column=1, padx=4, pady=2, sticky="nsew")
user_name_entry.insert(0, 'FCS')

password_entry = ttk.Entry(entry_frame, width=37, show="*")
password_entry.grid(row=1, column=1, padx=4, pady=4, sticky="nsew")

database_label = ttk.Label(entry_frame, text="Database:")
database_label.grid(row=2, column=0, padx=6, pady=4, sticky="nsew")

database_output_label = ttk.Label(entry_frame, text="FCS", anchor='w')
database_output_label.grid(row=2, column=1, padx=2, pady=4, sticky='w')

change_password_button = ttk.Button(text="Change Password . . . ", underline=7).place(x=8, y=110)
okay_button = ttk.Button(text="OK", width=11, underline=0, command=lambda:okay()).place(x=166, y=110)
cancel_button = ttk.Button(text="Cancel", width=10, underline=0, command=lambda:cancel()).place(x=247, y=110)

window.mainloop()
