import tkinter as tk
from tkinter import ttk
from .key import KeyPair

key = KeyPair()

def click_button1():
    text_box.delete(1.0, tk.END)
    text_box.insert(1.0, "Click either the 'Private' or 'Public' buttons to display the RSA key")

def click_button2():
    text_box.delete(1.0, tk.END)
    text_box.insert(1.0, key.private.format("multiline"))
    key.key_type = "private"

def click_button3():
    text_box.delete(1.0, tk.END)
    text_box.insert(1.0, key.public.format("multiline"))
    key.key_type = "public"

def click_button4():
    text_box.delete(1.0, tk.END)
    if key.key_type == "private":
        text_box.insert(1.0, key.private.format("multiline"))
    elif key.key_type == "public":
        text_box.insert(1.0, key.public.format("multiline"))

def click_button5():
    text_box.delete(1.0, tk.END)
    if key.key_type == "private":
        text_box.insert(1.0, key.private.format("string"))
    elif key.key_type == "public":
        text_box.insert(1.0, key.public.format("string"))

def click_button6():
    text_box.delete(1.0, tk.END)
    if key.key_type == "private":
        text_box.insert(1.0, key.private.format("base64"))
    elif key.key_type == "public":
        text_box.insert(1.0, key.public.format("base64"))

root = tk.Tk()
root.title("RSA Key Generator")

button1 = ttk.Button(root, text="Generate New Key", command=click_button1)
frame1 = ttk.Frame(root)
button2 = ttk.Button(frame1, text="Private", command=click_button2)
button3 = ttk.Button(frame1, text="Public", command=click_button3)
frame2 = ttk.Frame(root)
button4 = ttk.Button(frame2, text="Multiline", command=click_button4)
button5 = ttk.Button(frame2, text="String", command=click_button5)
button6 = ttk.Button(frame2, text="Base64", command=click_button6)

text_box = tk.Text(root)
text_box.insert(tk.END, "Click the 'Generate New Key' button to begin")
button1.pack()
button2.pack(side=tk.LEFT, expand=True)
button3.pack(side=tk.LEFT, expand=True)
button4.pack(side=tk.LEFT, expand=True)
button5.pack(side=tk.LEFT, expand=True)
button6.pack(side=tk.LEFT, expand=True)

frame1.pack()
frame2.pack()
text_box.pack(expand=True)


root.mainloop()
