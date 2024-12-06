import tkinter as tk
from tkinter import messagebox

# Function to handle the submission of the form
def submit():
    student_name = entry_name.get()
    roll_number = entry_roll.get()

    if student_name and roll_number:
        # Here you can add code to process the data (e.g., save it to a database or file)
        messagebox.showinfo("Submission Successful", f"Name: {student_name}\nRoll Number: {roll_number}")
        # Clear the entries
        entry_name.delete(0, tk.END)
        entry_roll.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in both fields")

# Create the main window
root = tk.Tk()
root.title("Student Entry Form")

# Create and place the labels and entry fields
label_name = tk.Label(root, text="Student Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_roll = tk.Label(root, text="Roll Number:")
label_roll.grid(row=1, column=0, padx=10, pady=10)

entry_roll = tk.Entry(root)
entry_roll.grid(row=1, column=1, padx=10, pady=10)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=2, columnspan=2, pady=10)

# Run the application
root.mainloop()
