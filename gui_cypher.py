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

        # LABEL AND ENTRY FIELD FOR CRACKED TEXT
        self.cracked_label = Label(self, text = "Cracked text:")
        self.cracked_label.grid()
        self.cracked_entry = Entry(self, width = 40)
        self.cracked_entry.grid()

    def decryption(self):
        pass

# main
root = Tk()
root.title("Caesar Cypher")
root.geometry("250x200")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()