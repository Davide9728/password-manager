from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator():
    nr_letters = 4
    nr_symbols = 4
    nr_numbers = 4

    letters_list = [random.choice(letters) for _ in range(0, nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(0, nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(0, nr_numbers)]
    password_list = (letters_list + symbols_list + numbers_list)
    random.shuffle(password_list)
    password = "".join([str(char) for char in password_list])

    return password
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    pass_to_search = website_enter.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='input not found', message=f" Save something first")
    else:
        if pass_to_search in data:
            email = data[pass_to_search]['email']
            password = data[pass_to_search]['password']
            messagebox.showinfo(title=pass_to_search, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title='Error', message=f" No details for {pass_to_search}")

    finally:
        file.close()

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    the_passw = password_enter.get()
    the_username = email_username_enter.get()
    the_website = website_enter.get()

    data_dict = {
        the_website: {
            'email': the_username,
            'password': the_passw
        }
    }

    if len(the_passw) > 0 and len(the_website) > 0:  # controls if password and email are wrote, and then save it
        try:
            with open('data.json', 'r') as file:
                # reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open('data.json', 'w') as file:
                # saving data
                json.dump(data_dict, file, indent=4)  # (indent) provide the number of spaces to indent json data
        else:
            # updating old data with new data
            data.update(data_dict)
            with open('data.json', 'w') as file:
                # saving  updated data
                json.dump(data, file, indent=4)

        finally:
            # clear the password and website section into gui
            password_enter.delete(0, END)
            website_enter.delete(0, END)
            file.close()

    else:
        messagebox.showinfo(title='input not found', message=f"dont leave password of name  ")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

#logo img
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)


#text wesite
webisite_label = Label(text='Website:')
webisite_label.grid(column=0, row=1)

#text Email/username
email_username_label= Label(text='Email/Username:')
email_username_label.grid(column=0, row=2)

#text Password
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

#enter website
website_enter = Entry(width=33)
website_enter.grid(column=1, row=1)

#enter username
email_username_enter = Entry(width=53)
email_username_enter.grid(column=1, row=2, columnspan=2)
email_username_enter.insert(0, 'davidemakenice@gmail.com')


#enter password
password_enter = Entry(width=33)
password_enter.grid(column=1, row=3)


#buttom generate password
def gen_pass():
    password_enter.delete(0, END)
    password_enter.insert(0, password_generator())

gen_pass_button = Button(text='Generate password:', command=gen_pass)
gen_pass_button.grid(column=2, row=3)

#button search
search_buttom = Button(text='Search', width=16, command=find_password)
search_buttom.grid(row=1, column=2)

#button add
add_button = Button(text='Add', width=45, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()

