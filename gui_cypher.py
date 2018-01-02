from tkinter import *
from cipherfun import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # LABEL AND ENTRY FIELD FOR ENCRYPTED TEXT
        self.text_label = Label(self, text = "Encrypted text:")
        self.text_label.grid()
        self.text_entry = Entry(self, width = 40)
        self.text_entry.grid()

        # BUTTON TO RUN CIPHER
        self.cipher_button = Button(self, text = "Decrypt!", command = self.decryption)
        self.cipher_button.grid()

        # LABEL AND RETURN FIELD FOR CRACKED TEXT
        self.cracked_label = Label(self, text = "Cracked text:")
        self.cracked_label.grid()
        self.cracked_return = Text(self, width = 30, height = 52, wrap = WORD)
        self.cracked_return.grid()

    def decryption(self):
        cypher_text = self.text_entry.get()
        self.cracked_return.delete(0.0, END)
        self.cracked_return.insert(0.0, unencrypt(cypher_text))

# main
root = Tk()
root.title("Caesar Cypher")
if 'enchant' in sys.modules:
    root.geometry("250x200")
else:
    root.geometry("250x1200")
root.resizable(width = FALSE, height = FALSE)
app = Application(root)
root.mainloop()