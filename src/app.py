import tkinter as tk
from tkinter import ttk

from .key import KeyFormatType, KeyPair


class App:
    def __init__(self):
        self.key = KeyPair()

        self.root = tk.Tk()
        self.root.title("RSA Key Generator")

        self.button1 = ttk.Button(
            self.root, text="Generate New Key", command=self.click_button1
        )
        self.frame1 = ttk.Frame(self.root)
        self.button2 = ttk.Button(
            self.frame1, text="Private", command=self.click_button2
        )
        self.button3 = ttk.Button(
            self.frame1, text="Public", command=self.click_button3
        )
        self.frame2 = ttk.Frame(self.root)
        self.button4 = ttk.Button(
            self.frame2, text="Multiline", command=self.click_button4
        )
        self.button5 = ttk.Button(
            self.frame2, text="String", command=self.click_button5
        )
        self.button6 = ttk.Button(
            self.frame2, text="Base64", command=self.click_button6
        )
        self.text_box = tk.Text(self.root, width=64)
        self.text_box.insert(tk.END, "Click the 'Generate New Key' button to begin")
        copy_button = ttk.Button(
            self.root, text="Copy to Clipboard", command=self.copy_to_clipboard
        )
        self.button1.pack()
        self.button2.pack(side=tk.LEFT, expand=True)
        self.button3.pack(side=tk.LEFT, expand=True)
        self.button4.pack(side=tk.LEFT, expand=True)
        self.button5.pack(side=tk.LEFT, expand=True)
        self.button6.pack(side=tk.LEFT, expand=True)

        self.frame1.pack()
        self.frame2.pack()
        self.text_box.pack(padx=10, pady=(10, 5), expand=True)
        copy_button.pack(pady=(0, 10))

    def copy_to_clipboard(self):
        # Get the text from the Text widget
        text_content = self.text_box.get(1.0, tk.END)

        # Clear the clipboard and append the text
        self.root.clipboard_clear()
        self.root.clipboard_append(text_content)

        # Update clipboard
        self.root.update()

    def click_button1(self):
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(
            1.0, "Click either the 'Private' or 'Public' buttons to display the RSA key"
        )
        self.key = KeyPair()

    def click_button2(self):
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(1.0, self.key.private.format(KeyFormatType.MULTILINE))
        self.key.key_type = "private"

    def click_button3(self):
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(1.0, self.key.public.format(KeyFormatType.MULTILINE))
        self.key.key_type = "public"

    def click_button4(self):
        self.text_box.delete(1.0, tk.END)
        if not self.key.key_type:
            self.text_box.insert(1.0, "First choose a Private or Public key type")
            return
        if self.key.key_type == "private":
            self.text_box.insert(1.0, self.key.private.format(KeyFormatType.MULTILINE))
        elif self.key.key_type == "public":
            self.text_box.insert(1.0, self.key.public.format(KeyFormatType.MULTILINE))

    def click_button5(self):
        self.text_box.delete(1.0, tk.END)
        if not self.key.key_type:
            self.text_box.insert(1.0, "First choose a Private or Public key type")
            return
        if self.key.key_type == "private":
            self.text_box.insert(1.0, self.key.private.format(KeyFormatType.STRING))
        elif self.key.key_type == "public":
            self.text_box.insert(1.0, self.key.public.format(KeyFormatType.STRING))

    def click_button6(self):
        self.text_box.delete(1.0, tk.END)
        if not self.key.key_type:
            self.text_box.insert(1.0, "First choose a Private or Public key type")
            return
        if self.key.key_type == "private":
            self.text_box.insert(1.0, self.key.private.format(KeyFormatType.BASE64))
        elif self.key.key_type == "public":
            self.text_box.insert(1.0, self.key.public.format(KeyFormatType.BASE64))


app = App()
app.root.mainloop()
