from tkinter import *
from tkinter import messagebox
import random
import json

def find_password():
    website = website_entry.get()

    try:
        with open("password_manager.json", "r") as file:
            data = json.load(file)
            
    except FileNotFoundError:
        messagebox.showerror(title="FileNotFoundError", message="There is no such file")
    
    else:
        if website in data:
                    email = data[website]["email"]
                    password = data[website]["password"]
                    messagebox.showinfo(title=f"Info Found for {website}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="No Data Found", message="No detailes exist for this website")
    finally:
        website_entry.delete(0,END)



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_nums = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_nums + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    new_data = {website_data:{"email": email_data,
                              "password": password_data}}

    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showerror(title="Oops", message="You have left some fields empty")
    else:
        try:
            with open("password_manager.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
                
        except FileNotFoundError:
            with open("password_manager.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("password_manager.json", "w") as file:
                json.dump(data, file, indent=4)

        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

#Labels

website_label = Label(text="Website: ", font=("Courier", 12, "bold"))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ", font=("Courier", 12, "bold"))
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ", font=("Courier", 12, "bold"))
password_label.grid(row=3, column=0)

#Inputs/Outputs

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"ogcata@abv.bg")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Buttons

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

pass_gen_button = Button(text="Generate Password", width=14, command=generate_password)
pass_gen_button.grid(row=3, column=2)

add_button = Button(text="Add", width=30,  command=add)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()