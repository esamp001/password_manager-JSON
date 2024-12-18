from tkinter import messagebox
from tkinter import *
from tkinter import Canvas, PhotoImage
from random import choice, randint, shuffle

import pyperclip
import json

file_name = "data.json"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button():
    data_website = website_entry.get()
    data_email = email_entry.get()
    data_password = password_entry.get()
    new_data = {
        data_website: {
            "email": data_email,
            "password": data_password

    }
    }

    if len(data_website) == 0 or len(data_password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open(file_name, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(file_name, "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                print(f"Data successfully written to {file_name}")
        else:
            data.update(new_data)
            with open(file_name, "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            txt_file = "data.txt"
            with open(txt_file, "w") as txt_file:
                txt_file.write(json.dumps(data, indent=4))
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH BUTTON ------------------------------- #

def find_password():

    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            user_input = website_entry.get()
    except FileNotFoundError:
        messagebox.showinfo(title="Opps..", message=f"No data found for {user_input}")
    else:
        if user_input in data:
            user_data = data[user_input]["email"]
            password = data[user_input]["password"]
            messagebox.showinfo(title="Data Found", message=f"Email: {user_data}\n Password: {password}")
        elif user_input not in data:
            messagebox.showinfo(title="Opps..", message=f"No credentials found in {user_input}")
    finally:
        txt_file = "data.txt"
        with open(txt_file, "w") as txt_file:
            txt_file.write(json.dumps(data, indent=4))



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.iconbitmap("lock.ico")
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="final.png")
canvas.create_image(100, 85, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "ex.@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Buttons
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=add_button)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()