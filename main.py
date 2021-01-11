from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------- PASSWORD GENERATOR ------------------------- #
def generate_password():

	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	password_letters = [choice(letters) for _ in range(randint(8, 10))]
	password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
	password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

	password_list = password_letters + password_symbols + password_numbers
	shuffle(password_list)

	password = "".join(password_list)
	password_input.insert(0, password)
	pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
	
	website = website_input.get()
	username = username_input.get()
	password = password_input.get()
	new_data = {
		website: {
			"username": username,
			"password": password,
		}
	}

	if len(website) == 0 or len(password) == 0:
		messagebox.showinfo(title="Oops", message="Oops, did you forget a field?")
	else:
		try:

			with open("data.json", "r") as data_file:
				# Reading old data
				data = json.load(data_file)
		except FileNotFoundError:
			with open("data.json", "w") as data_file:
				json.dump(new_data, data_file, indent=4)
		else:
			# Updating old data with new data
			data.update(new_data)

			with open("data.json", "w") as data_file:
				#Savinh updated data
				json.dump(data, data_file, indent=4)
		finally:
			website_input.delete(0, END)
			password_input.delete(0, END)

# --------------------------- FIND PASSWORD ------------------------------ #
def find_password():
	website = website_input.get()
	try:
		with open("data.json") as data_file:
			data = json.load(data_file)
	except FileNotFoundError:
		messagebox.showinfo(title="Erro", message="No Data File Found")
	else:
		if website in data:
			username = data[website]["username"]
			password = data[website]["password"]
			messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
		else:
			messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

#Entries
website_input = Entry(width=35)
website_input.grid(column=1, row=1)
website_input.focus()

username_input = Entry(width=54)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "test@gmail.com")

password_input = Entry(width=35)
password_input.grid(column=1, row=3)

window.mainloop()