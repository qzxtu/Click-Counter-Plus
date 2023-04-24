import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Create the main window
window = tk.Tk()

# Initialize the click counter and increment value as IntVar() objects
click_count = tk.IntVar(value=0)
click_increment = tk.IntVar(value=1)

# Define the click handlers
def handle_click():
    """Handle the click of the first button."""
    click_count.set(click_count.get() + click_increment.get())
    label_text.set(f"Number of clicks: {click_count.get()}")

def handle_increment():
    """Handle the click of the second button."""
    if click_count.get() >= 1:
        click_increment.set(click_increment.get() + 1)
        click_count.set(click_count.get() - 1)
        label_text.set(f"Number of clicks: {click_count.get()}")
    else:
        messagebox.showwarning("Not enough clicks", "You need at least 1 click to increase the increment value.")
        
        # Set the increment value back to 1
        click_increment.set(1)

        # Reset the click count to 0
        click_count.set(0)

        # Update the label text
        label_text.set(f"No clicks yet.")

# Create the frame for the first button
click_frame = ttk.Frame(window)
click_frame.pack()

# Create the first button and add it to the frame
click_button = ttk.Button(click_frame, text="Click Me", command=handle_click)
click_button.pack(side=tk.LEFT, padx=5)

# Create the second button and add it to the frame
increment_button = ttk.Button(click_frame, text="Increase Increment", command=handle_increment)
increment_button.pack(side=tk.LEFT, padx=5)

# Create the frame for the label
label_frame = ttk.Frame(window)
label_frame.pack(pady=10)

# Create the label and add it to the frame
label_text = tk.StringVar()
label_text.set("No clicks yet.")
click_label = ttk.Label(label_frame, textvariable=label_text)
click_label.pack()

# Start the main loop
window.mainloop()