import tkinter as tk
from tkinter import ttk

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
          'Q','R','S','T','U','V','W','X','Y','Z']

class Encryption():
    def encrypt_caesar_cipher(self,key,word,mode):
        #check if the key is a number
        try:
            key = int(key)
        except ValueError:
            raise ValueError("The key should can only be an integer") 
        
        encrypted = []
        word = word.upper()
        
        #check if there is some symbol or number in the word
        for i in word: 
            if i not in letters: 
                encrypted.append(i)
                continue
            if mode == "1":
                encrypt = (letters.index(i) + key) % 26
            elif mode == "2":
                encrypt = (letters.index(i) - key) % 26
            encrypted.append(letters[encrypt])
            
        return ''.join(encrypted)
    
    def encrypt_vigenere(self,key,word,mode):
        encrypted = []
        key_len = len(key)
        
        #turn the key and word into upper case
        word = word.upper()
        key = key.upper()
        
        #checking if there is a punctuation character / number
        for i in key: 
            if i not in letters: 
                raise ValueError("The key can only contain letters")
        iterate = 0
        
        for letter in word: 
            if letter not in letters:
                encrypted.append(letter)
                continue

            letter = letter.upper()
            if mode == "1":
                encrypt = (letters.index(letter) + letters.index(key[iterate % key_len])) % 26
            elif mode == "2":
                encrypt = (letters.index(letter) - letters.index(key[iterate % key_len])) % 26
            else:
                raise ValueError("Invalid mode option")
            encrypt = letters[encrypt]
            encrypted.append(encrypt)
            iterate += 1
            
        return "".join(encrypted)

encrypt = Encryption()

class PlaceholderEntry(ttk.Entry):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = "gray"
        self.default_fg_color = self["foreground"]
        
        self.bind("<FocusIn>", self._remove_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)
        
        self._add_placeholder()

    def _remove_placeholder(self, event=None):
        if self.get() == self.placeholder:
            self.delete(0, "end")
            self.config(foreground=self.default_fg_color)

    def _add_placeholder(self, event=None):
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(foreground=self.placeholder_color)
    
class app():
    def __init__(self):
        self.root = tk.Tk()
        #Give the widget a title and a size

        self.root.title("Encryption")
        self.root.geometry("400x400")
        
        self.button_style = ttk.Style(self.root)
        self.button_style.configure("style.TButton",background="gray",foreground="black")
        
        #Make the frme of the widget and set the background to black
        self.mainframe = tk.Frame(self.root,background="gray")
        self.mainframe.pack(fill="both",expand=True)
        
        self.text_title = ttk.Label(self.mainframe,text="Encryption Result:",wraplength=350,font=("Arial",30),background="gray",foreground="black")
        self.text_title.grid(row=0,column=0,columnspan=2,padx=30,pady=0,sticky="W")
        
        #Crate an Entry Style
        self.text = ttk.Label(self.mainframe,text="[Result]",font=("Arial",15),wraplength=350,background="gray",foreground="black")
        self.text.grid(row=1,column=0,padx=30,pady=0,sticky="W")
        
        #Make an Entry so we can type in the text we want to Encrypt/Decrypt
        self.input = PlaceholderEntry(self.mainframe,placeholder="Plain/Encrypted Text",background="black",width=30)
        self.input.grid(row=2,column=0,padx=115,pady=20,sticky="W")
        
        #Make an Entry so we can type in the key so we can Encrypt/Decrypt
        self.key = PlaceholderEntry(self.mainframe,placeholder="Key",background="black",width=30)
        self.key.grid(row=3,column=0,padx=115,pady=0,sticky="W")
        
        encryption_method = ["Caesar","Vigenere"]
        encryption_mode = ["Encrypt","Decrypt"]
        
        self.method_dropdown = ttk.Combobox(self.mainframe,values=encryption_method,background="gray",state="readonly",width=27)
        self.method_dropdown.grid(row=4,column=0,padx=115,pady=20,sticky="W")
        self.method_dropdown.current(0)
        
        self.mode = ttk.Combobox(self.mainframe,values=encryption_mode,background="gray",state="readonly",width=27)
        self.mode.grid(row=5,column=0,padx=115,pady=0,sticky="W")
        self.mode.current(0)
        
        self.button = ttk.Button(self.mainframe,text="Encrypt/Decrypt",style="style.TButton",command=self.Encrypt_Decryppt)
        self.button.grid(row=6,column=0,padx=20,pady=20)
        self.root.mainloop()
        return 
    
    def error(self,error_message): 
        error_popup = tk.Toplevel(self.root)
        error_popup.title("Error")
        
        error_label = tk.Label(error_popup, text=error_message, font=("Arial", 12), padx=20, pady=10)
        error_label.pack()
        
        ok_button = ttk.Button(error_popup, text="OK", command=error_popup.destroy)
        ok_button.pack(pady=10)
        
    def Encrypt_Decryppt(self):
        text = self.input.get()
        key = self.key.get()
        method = self.method_dropdown.get()
        mode = self.mode.get()
        
        if text == "Plain/Encrypted Text" or key == "Key":
            self.error("Please fill in the text and key")
        else: 
            if method == "Caesar" and mode == "Encrypt":
                try: 
                    modified = encrypt.encrypt_caesar_cipher(key,text,"1")
                except ValueError:
                    self.error("In Caesar, the key can only contain integer")
            elif method == "Caesar" and mode == "Decrypt":
                try: 
                    modified = encrypt.encrypt_caesar_cipher(key,text,"2")
                except ValueError:
                    self.error("In Caesar, the key can only contain integer")
            elif method == "Vigenere" and mode == "Encrypt":
                try:
                    modified = encrypt.encrypt_vigenere(key,text,"1")
                except ValueError:
                    self.error("In Vigenere, the key can only contain letters")
            elif method == "Vigenere" and mode == "Decrypt":
                try: 
                    modified = encrypt.encrypt_vigenere(key,text,"2")
                except ValueError:
                    self.error("In Vigenere, the key can only contain letters")
            else:
                self.error("Invalid method or mode")
        try: 
            self.text.config(text=modified)
        except UnboundLocalError:
            pass
        
        
if __name__ == "__main__":
    app()