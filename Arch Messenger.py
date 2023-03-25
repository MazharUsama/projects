from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog as fd
import pywhatkit

class Add_project:
    def __init__(self,root):
        self.root = root
        self.root.title("Arch Messenger")
        self.root.configure(bg='#ffffff')
        self.root.iconbitmap(r'2.ico')
        self.root.minsize(350, 550)
        self.root.maxsize(350, 550)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_height = 550
        window_width = 350
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(4, weight=1)

        self.contacts = []

        # Image
        self.menuImage = Image.open(r"1.png")
        self.menuImage = self.menuImage.resize((125, 100), Image.ANTIALIAS)
        self.menuImage = ImageTk.PhotoImage(self.menuImage)

        menuImageLabel = Label(self.root, image=self.menuImage, bg="#ffffff", relief="flat")
        menuImageLabel.grid(column=1, row=0)

        # Import Button
        self.importButton = Button(self.root, text="Import", width=28, height=0, bg='#5a18ee', fg="White",
                                  font="Arial 9", command=lambda: [select_file()], relief="flat")
        self.importButton.grid(row=1, column=1, sticky=W, padx=5, pady=0, ipady=3, ipadx=22)

        # Message Entry
        self.messageEntry = Text(self.root, border=0, relief="solid", highlightbackground="#F6F6F6", background="#E9E9E9",
                                            highlightcolor="#F6F6F6", highlightthickness=0, borderwidth=0, height=15,
                                            width=31)
        self.messageEntry.grid(row=2, column=1, sticky=W, padx=5, pady=15)

        # Send Button
        self.sendButton = Button(self.root, text="Send", width=28, height=0, bg='#5a18ee', fg="White",
                                   font="Arial 9", command=lambda: [send_Message()], relief="flat")
        self.sendButton.grid(row=3, column=1, sticky=W, padx=5, pady=0, ipady=3, ipadx=22)

        def select_file():
            filetypes = (
                ('text files', '*.txt'),
                ('All files', '*.*'),
            )

            file = fd.askopenfile(filetypes=filetypes)
            self.contacts = file.readlines()

        def send_Message():
            contacts = self.contacts
            message = self.messageEntry.get("1.0", END)

            for contact in contacts:
                print(contact)
                pywhatkit.sendwhatmsg_instantly(contact, message, tab_close=True, wait_time=20, close_time=5)



if __name__=="__main__":
    root=Tk()
    obj=Add_project(root)
    root.mainloop()