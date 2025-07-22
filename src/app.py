import tkinter as tk
from tkinter import ttk

from .key import KeyFormatType, KeyPair


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

        # Center the window on screen after all widgets are packed
        self.center_window()

    def center_window(self):
        """Center the window on the screen"""
        # Update the window to get proper dimensions
        self.root.update_idletasks()

        # Set a minimum size for the window
        self.root.minsize(600, 400)

        # Get window dimensions (use actual or minimum)
        window_width = max(self.root.winfo_reqwidth(), 600)
        window_height = max(self.root.winfo_reqheight(), 400)

        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate position to center the window
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # Set the window position and size
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

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


def main():
    app = App()
    app.root.mainloop()


if __name__ == "__main__":
    main()
