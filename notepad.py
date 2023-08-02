

from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as tmsg

window = Tk()
window.geometry("800x600")
window.title("Untitled - Notepad")
window.iconbitmap("notebook.png")
window.minsize(width=400, height=200)

undo_stack = []
redo_stack = []

def new_file():
    text.delete("1.0", END)
    tmsg.showinfo("New File", "New File is Opened")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text.delete("1.0", END)
            text.insert("1.0", content)


def save_file():
    content = text.get("1.0", END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(content)
        tmsg.showinfo("Saved", message="File Saved Successfully")


def print_file():
    val = tmsg.askquestion("Print", message="Are you sure to Print?")
    if val == "yes":
        tmsg.showinfo("printing", message="Printing will Start Soon.")


def close_file():
    window.destroy()
    tmsg.showinfo("Closing", "Window is Closed")


def exit_file():
    ans = tmsg.askquestion("Exit", message="Did you save your File")
    if ans == "no":
        save_file()
        tmsg.showinfo("closed", "File is Closed")
        window.quit()
    else:
        tmsg.showinfo("closed", "File is Closed")
        window.quit()


def cut_edit():
    selected_text = text.selection_get()
    if selected_text:
        text.delete("sel.first", "sel.last")
        text.clipboard_clear()
        text.clipboard_append(selected_text)
        current_content = text.get("1.0", "end-1c")
        redo_stack.clear()
        undo_stack.append(current_content)
    


def on_text_change(event):
    current_content = text.get("1.0", "end-1c")
    redo_stack.clear()
    undo_stack.append(current_content)

def copy_edit():

    selected_text = text.selection_get()
    if selected_text:
        text.clipboard_clear()
        text.clipboard_append(selected_text)

def paste_edit():
    clipboard_content = text.clipboard_get()
    text.insert(INSERT, clipboard_content)

def welcome():
    text.insert(END,"Welcome to Notepad!\nThis Notepad is created by Harsimran.\nI Hope you will Enjoy using it...")
def about_notepad():
    text.insert(END, """About Notepad

Notepad is a simple text editor created by Harsimran. It is a lightweight and user-friendly application designed for basic text editing tasks. Notepad provides a minimalistic interface, allowing users to focus on their writing without distractions.

Features:
- Create and edit plain text documents
- Save and load text files in various formats (e.g., .txt)
- Basic text formatting options (e.g., font size, font style)
- Copy, cut, and paste functionality for easy text manipulation
- Simple calculator functionality for quick calculations
- Open and display text files of various sizes

Note: This Notepad application is provided as-is and does not come with advanced features or complex functionalities found in more comprehensive text editors. It is intended for simple and casual text editing purposes.

The source code for this Notepad application is available on GitHub at:
[GitHub Repository URL]

Feel free to use and modify this Notepad according to your needs. If you encounter any issues or have suggestions for improvements, please feel free to share them in the GitHub repository.

Thank you for using Notepad!

Created by: Harsimran
""")
def view_license():
    tmsg.showinfo("License", message="""Custom License - Harsimran's Notepad

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

2. You must give appropriate credit to Harsimran as the original creator of this Notepad, and indicate if any modifications have been made.

3. The Software is provided "AS IS", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the creators or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the Software or the use or other dealings in the Software.

""")


scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(window, font=("Arial", 10, "bold"), yscrollcommand=scrollbar.set)
text.pack(fill=BOTH, expand=True)
scrollbar.config(command=text.yview)


mymenu = Menu(window)
m1 = Menu(mymenu, tearoff=0)

m1.add_command(label="New", command=new_file)
m1.add_command(label="Open", command=open_file)
m1.add_command(label="Save", command=save_file)
m1.add_command(label="Print", command=print_file)
m1.add_separator()
m1.add_command(label="Close Window", command=close_file)
m1.add_command(label="Exit", command=exit_file)

mymenu.add_cascade(label="Files", menu=m1)
window.config(menu=mymenu)

m2 = Menu(mymenu, tearoff=0)
m2.add_command(label="Cut", command=cut_edit)
# text.bind("<<Modified>>", on_text_change)
# text.edit_modified(True)
m2.add_command(label="Copy", command=copy_edit)
m2.add_command(label="Paste", command=paste_edit)

mymenu.add_cascade(label="Edit", menu=m2)
window.config(menu=mymenu)

m3 = Menu(mymenu, tearoff=0)

m3.add_command(label="Welcome", command=welcome)
m3.add_command(label="About-Notepad", command=about_notepad)
m3.add_command(label="View License", command=view_license)

mymenu.add_cascade(label="Help", menu=m3)
window.config(menu=mymenu)


window.mainloop()
