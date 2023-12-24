import tkinter as tk
from tkinter import ttk
from .key import KeyPair

class App:
    def __init__(self):
        self.key = KeyPair()

        self.root = tk.Tk()
        self.root.title("RSA Key Generator")

        self.button1 = ttk.Button(self.root, text="Generate New Key", command=self.click_button1)
        self.frame1 = ttk.Frame(self.root)
        self.button2 = ttk.Button(self.frame1, text="Private", command=self.click_button2)
        self.button3 = ttk.Button(self.frame1, text="Public", command=self.click_button3)
        self.frame2 = ttk.Frame(self.root)
        self.button4 = ttk.Button(self.frame2, text="Multiline", command=self.click_button4)
        self.button5 = ttk.Button(self.frame2, text="String", command=self.click_button5)
        self.button6 = ttk.Button(self.frame2, text="Base64", command=self.click_button6)
# TODO: state where new key is generated and user chooses format but public/private hasn't been pressed
        self.text_box = tk.Text(self.root)
        self.text_box.insert(tk.END, "Click the 'Generate New Key' button to begin")
        self.button1.pack()
        self.button2.pack(side=tk.LEFT, expand=True)
        self.button3.pack(side=tk.LEFT, expand=True)
        self.button4.pack(side=tk.LEFT, expand=True)
        self.button5.pack(side=tk.LEFT, expand=True)
        self.button6.pack(side=tk.LEFT, expand=True)

        self.frame1.pack()
        self.frame2.pack()
        self.text_box.pack(expand=True)

    def click_button1(self):
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(1.0, "Click either the 'Private' or 'Public' buttons to display the RSA key")
        self.key = KeyPair()

    def click_button2(self):
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(1.0, self.key.private.format("multiline"))
        self.key.key_type = "private"

    def click_button3(self):
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(1.0, self.key.public.format("multiline"))
        self.key.key_type = "public"

    def click_button4(self):
        self.text_box.delete(1.0, tk.END)
        if self.key.key_type == "private":
            self.text_box.insert(1.0, self.key.private.format("multiline"))
        elif self.key.key_type == "public":
            self.text_box.insert(1.0, self.key.public.format("multiline"))

    def click_button5(self):
        self.text_box.delete(1.0, tk.END)
        if self.key.key_type == "private":
            self.text_box.insert(1.0, self.key.private.format("string"))
        elif self.key.key_type == "public":
            self.text_box.insert(1.0, self.key.public.format("string"))

    def click_button6(self):
        self.text_box.delete(1.0, tk.END)
        if self.key.key_type == "private":
            self.text_box.insert(1.0, self.key.private.format("base64"))
        elif self.key.key_type == "public":
            self.text_box.insert(1.0, self.key.public.format("base64"))

app = App()
app.root.mainloop()