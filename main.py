from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def gen_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for sym in range(randint(2, 4))]
    password_list += [choice(numbers) for num in range(randint(2, 4))]

    shuffle(password_list)

    new_password = "".join(password_list)
    pass_entry.insert(0, new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_data():
    web = web_entry.get().capitalize()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        web: {
            "email": email,
            "password": password
        }
    }

    if len(web) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as file1:
                data = json.load(file1)
        except FileNotFoundError:
            data = {}  # Create an empty dictionary if the file doesn't exist yet
        except json.JSONDecodeError:
            data = {}  # Handle JSONDecodeError by creating an empty dictionary
        finally:
            data.update(new_data)
            with open("data.json", "w") as file1:
                json.dump(data, file1, indent=4)

            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- SEARCH WEBSITE ------------------------------- #

def search():
    web = web_entry.get().capitalize()
    try:
        with open("data.json", "r") as datafile:
            data = json.load(datafile)
            details = f"Email = {data[web]['email']}\nPassword = {data[web]['password']}"
            messagebox.showinfo(title=f"{web} Details", message=details)
    except FileNotFoundError:
        messagebox.showinfo(title=f"{web} Result", message=f"No entry found for {web}")
    except json.JSONDecodeError:
        messagebox.showinfo(title=f"{web} Result", message=f"Error decoding JSON in data.json")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=21)
web_entry.grid(row=1, column=1)
web_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "gichimalik@gmail.com")

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=13, command=search)
search_button.grid(row=1, column=2)

pass_button = Button(text="Generate Password", command=gen_password)
pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
