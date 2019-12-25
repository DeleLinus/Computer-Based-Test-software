from tkinter import *

# def main():
#     root=Tk()
#     app=SignupWindow(root)
#     root.mainloop()


class Signupwindow:
    def __init__(self,master):
        self.master=master
        self.master.title("OAU Computer Based Assessment")
        self.master.geometry('1100x600')
        self.master.config(bg="powder blue")
        self.Matricnum=StringVar()
        self.Password=StringVar()
        self.Titlelbl=Label(self.master,text="CANDIDATE REGISTRATION AND LOGIN  PAGE",
            font=("arial",30,"bold"),bg="powder blue", pady=30).pack(side=TOP)
        self.frame=Frame(self.master)#, bg="red")
        self.frame.pack(side="left")
        self.matricnumLbl=Label(self.frame, text="Matric Number:",font=("arial",20,"bold"),
            bg="powder blue").grid(row=0, column=0, pady=20)
        self.paswordLbl=Label(self.frame,text="Password:",font=("arial",20,"bold"),
            bg="powder blue").grid(row=1, column=0, pady=20)


    #==========================================================================
        

    def new_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=QuestionWindow(self.newWindow)

class Questionwindow:
    def __init__(self,master):
        self.master=master
        self.master.title("*****************************")
        self.master.geometry('600x400')
        self.master.config(bg="powder blue")
        self.frame=Frame(self.master)
        self.frame.pack()

root=Tk()
app=Signupwindow(root)
root.mainloop()




