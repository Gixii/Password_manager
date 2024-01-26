from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


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


def add_data():
    web = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(web) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty")
    else:

        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered:\nEmail: {email}"
                                                          f"\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file1:
                file1.write(f"{web} | {email} | {password}\n")
                web_entry.delete(0, END)
                pass_entry.delete(0, END)


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
web_entry = Entry(width=38)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "pranjalmalik6543@gmail.com")

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

# Buttons
pass_button = Button(text="Generate Password", command=gen_password)
pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
