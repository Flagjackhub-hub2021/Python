import tkinter as tk
import random
import string

# Define the GUI window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x200") # Set the size of the window

# Define the GUI elements
password_label = tk.Label(window, text="Password Length")
password_label.pack()

password_length = tk.IntVar()
password_length.set(12)

password_entry = tk.Entry(window, textvariable=password_length)
password_entry.pack()

password_text = tk.StringVar()
password_output = tk.Label(window, textvariable=password_text)
password_output.pack()

# Define the password generator function
def generate_password():
    length = password_length.get()
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    password_text.set(password)

# Define the GUI button
password_button = tk.Button(window, text="Generate Password", command=generate_password)
password_button.pack()

# Start the GUI
window.mainloop()
