# gui_handler.py
import tkinter as tk
import functions

#  GUI Setup 
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

display_var = tk.StringVar()
display_var.set("") # Initialize display

# Create the display entry 
display_entry = tk.Entry(
    root, 
    textvariable=display_var, 
    font=('Arial', 20), 
    bd=5, 
    relief='sunken', 
    justify='right'
)
display_entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

def create_button(text_value, row, col):
    Button = tk.Button(
        root, 
        text=text_value, 
        command=lambda: functions.handle_button_press(text_value, display_var),
        font=('Arial', 14)
    )
    Button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2, ipadx=10, ipady=10)
    return Button

# making buttons using above fuctions
create_button("7", 1, 0)
create_button("8", 1, 1)
create_button("9", 1, 2)
create_button("*", 1, 3)

create_button("4", 2, 0)
create_button("5", 2, 1)
create_button("6", 2, 2)
create_button("-", 2, 3)

create_button("1", 3, 0)
create_button("2", 3, 1)
create_button("3", 3, 2)
create_button("+", 3, 3)

create_button("⟳", 4, 0)
create_button("0", 4, 1)
create_button("=", 4, 2)
create_button("/", 4, 3)

for i in range(5): # 5 rows (0 for display, 1-4 for buttons)
    root.grid_rowconfigure(i, weight=1)
for i in range(4): # 4 columns
    root.grid_columnconfigure(i, weight=1)

root.mainloop()