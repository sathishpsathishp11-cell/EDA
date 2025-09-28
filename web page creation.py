from tkinter import *
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    message = message_entry.get("1.0", END).strip() # Get text from Text widget

    if name and email and message:
        form_data.append({"Name": name, "Email": email, "Message": message})
        messagebox.showinfo("Success", "Form submitted successfully!")
        clear_form()
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def clear_form():
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    message_entry.delete("1.0", END)

# Initialize form data storage
form_data = []

# Create the main window
root = Tk()
root.title("Simple Project Form")
root.geometry("400x300")

# Name field
name_label = Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = Entry(root, width=40)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Email field
email_label = Label(root, text="Email:")
email_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
email_entry = Entry(root, width=40)
email_entry.grid(row=1, column=1, padx=10, pady=5)

# Message field
message_label = Label(root, text="Message:")
message_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
message_entry = Text(root, width=30, height=5)
message_entry.grid(row=2, column=1, padx=10, pady=5)

# Submit button
submit_button = Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()

print("Collected Form Data:")
for entry in form_data:
    print(entry)
