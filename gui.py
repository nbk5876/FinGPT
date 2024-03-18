#------------------------------------------------------------
# gui.py
# Purpose: 
#
#
#------------------------------------------------------------
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
# You might need to adjust the import path based on your project structure
from fingpt_main import process_user_query

def submit_query():
    # Retrieve all text from the Text widget
    user_query = query_text.get("1.0", "end-1c")  # From line 1, character 0 to end minus last newline character
    if user_query.strip() == "":
        messagebox.showinfo("Empty Query", "Please enter a query.")
        return
    # Call the main processing function of your application
    result = process_user_query(user_query)

    print(f"Debug: Result from process_user_query is of type {type(result)}: {result}")  # Debugging line

    # Display the result in the GUI
    results_txt.delete(1.0, tk.END)
    results_txt.insert(tk.INSERT, result)

# GUI setup code remains the same...

# Set up the GUI elements (root window, entry, buttons, etc.)
app = tk.Tk()
app.title("FinGPT")

# User query Text widget
query_label = tk.Label(app, text="Enter your query:")
query_label.pack()
query_text = tk.Text(app, height=5, width=20, wrap=tk.WORD)  # Height is set to 3 lines 50 chars
query_text.pack()

# Pre-fill the Text widget with a default query
default_query = "What are stock symbols for ## Microsoft, Apple ## and which stock may be the better investment?"
query_text.insert(tk.END, default_query)

# Set up the Submit button
submit_btn = tk.Button(app, text="Submit", command=submit_query)
submit_btn.pack()

# Set up the ScrolledText widget for results
results_txt = scrolledtext.ScrolledText(app, width=60, height=15)
results_txt.pack()

# Start the Tkinter event loop
app.mainloop()

