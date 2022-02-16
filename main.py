from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import logo.motto as motto

BG= "#90E0EF"
FG = "#03045E"
BTN = "white"

print(motto.motto)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers


    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="😎", messagebox="password copied to clipboard just paste it!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = entry_website.get()
    email_data = entry_email.get()
    password_data =entry_password.get()

    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_data,
                                       message=f"There are the details entered: \nEmail: {email_data} \nPassword: {password_data} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as f:
                f.write(f"{website_data} | {email_data} | {password_data}\n")

            entry_website.delete(0, END)
            entry_password.delete(0, END)



# ---------------------------- UI ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BG)

# Canvas
canvas = Canvas(width=200, height=200, bg=BG, highlightthickness=0)
logo_img=PhotoImage(file="./logo/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website", bg=BG, fg=FG)
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:", bg=BG, fg=FG)
label_email.grid(column=0, row=2)

label_password = Label(text="Password", bg=BG, fg=FG)
label_password.grid(column=0, row=3)

# Inputs/Entries
entry_website = Entry(width=35)
entry_website.grid(column=1,row=1, columnspan=2)
entry_website.focus()

entry_email = Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, "sakaryamh@gmail.com")

entry_password = Entry(width=21)
entry_password.grid(column=1,row=3)

# Buttons
button_generate = Button(text="Generate Password", bg=BTN, fg=FG, command=generate_password)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", bg=BTN, fg=FG, width=36, command=save)
button_add.grid(column=1, rows=4, columnspan=2)








window.mainloop()



# https://pypi.org/project/pyperclip/
# https://www.w3schools.com/python/ref_string_join.asp


