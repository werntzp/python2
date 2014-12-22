from tkinter import *

class Application(Frame):

    def convert(self):
        """Convert entry fields and sum."""
        try: 
            n1 = float(self.txt_one.get())
            n2 = float(self.txt_two.get())
            self.output.config(text=str(n1 + n2), fg="black")
            
        except:
            self.output.config(text="*** ERROR ***", fg="red")

    def createWidgets(self):
        """Create two entry fields, button and label."""
        top_frame = Frame(self)
        self.txt_one = Entry(top_frame)
        self.txt_one.pack(side=TOP)
        self.txt_two = Entry(top_frame)
        self.txt_two.pack(side=TOP)
        top_frame.pack(side=TOP)      
        
        bottom_frame = Frame(self)
        self.output = Label(top_frame, text="Sum displays here ...")
        self.output.pack(side=TOP)           
        self.btn_convert = Button(self, text="Convert", command=self.convert)
        self.btn_convert.pack(side=LEFT)
        self.btn_quit = Button(self, text="Quit", command=self.quit)
        self.btn_quit.pack(side=LEFT)
        bottom_frame.pack(side=BOTTOM)  
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()

