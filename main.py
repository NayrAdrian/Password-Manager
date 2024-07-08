from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_user_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=("Arial", 10))
website_label.grid(column=0, row=1)
email_user_label = Label(text="Email/Username:", font=("Arial", 10))
email_user_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=("Arial", 10))
password_label.grid(column=0, row=3, columnspan=1)

# Entries
website_input = Entry(width=52)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()  # Cursor on website input when launched
email_user_input = Entry(width=52)
email_user_input.grid(row=2, column=1, columnspan=2)
email_user_input.insert(0, "sample_email@gmail.com")  # Email Pre Populated
password_input = Entry(width=33)
password_input.grid(column=1, row=3, columnspan=1)

# Buttons
generate_button = Button(text="Generate Password", width=17, command=generate_password, font=("Arial", 8))
generate_button.grid(column=2, row=3, columnspan=1)

add_button = Button(text="Add", width=52, command=save, font=("Arial", 8))
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
