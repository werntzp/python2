from tkinter import *
import os
import shutil

ALL = N+S+E+W

class Application(Frame):
    
    def open_file(self):
        #  if text in entry widget, see if it is a file, if it is, open, read and drop into text widget
        self.master.t1.delete("1.0", END)
        fname = self.master.e1.get() 
        if len(fname) > 0:
            if os.path.isfile(fname):
                f = open(fname, "r")
                self.master.t1.insert(INSERT, f.read())
                f.close()
            else:
                self.master.t1.insert(INSERT, "File does not exist")
        else:
            self.master.t1.insert(INSERT, "Nothing in Entry widget")
            
    def click_frame(self, event):
        print("Frame", event.widget.frame, "clicked at", event.x, event.y) 
    
    def change_color_red(self):
        self.master.t1.configure(fg = "red")
        #pass 
    
    def change_color_blue(self):
        self.master.t1.configure(fg = "blue")
        #pass 
        
    def change_color_green(self):
        self.master.t1.configure(fg = "green")
        #pass
       
    def change_color_black(self):
        self.master.t1.configure(fg = "black")
        #pass
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()

        # configure rows
        for r in range(2):
            self.master.rowconfigure(r, weight=1)          
        
        # configure buttons
        self.master.columnconfigure(0, weight=1)
        self.master.btnRed = Button(master, text="Red", command=self.change_color_red)
        self.master.btnRed.grid(row=2, column=0, sticky=E+W)
        
        self.master.columnconfigure(1, weight=1)
        Button(master, text="Blue", command=self.change_color_blue).grid(row=2, column=1, sticky=E+W)
        self.master.columnconfigure(2, weight=1)
        Button(master, text="Green", command=self.change_color_green).grid(row=2, column=2, sticky=E+W)
        self.master.columnconfigure(3, weight=1)
        Button(master, text="Black", command=self.change_color_black).grid(row=2, column=3, sticky=E+W)
        self.master.columnconfigure(4, weight=1)
        Button(master, text="Open", command=self.open_file).grid(row=2, column=4, sticky=E+W)

        # add the frames with a label on each
        self.master.f1 = Frame(master, bg="red")
        self.master.f1.frame = "1"
        self.master.f1.bind("<Button-1>", self.click_frame)
        self.master.f1.grid(row=0, column=0, rowspan=1, columnspan=2, sticky=ALL) 
        #self.master.l1 = Label(self.master.f1, bg="red", text="Frame 1")
        #self.master.l1.grid()
        
        self.master.f2 = Frame(master, bg="orange")
        self.master.f2.frame = "2"
        self.master.f2.bind("<Button-1>", self.click_frame)
        self.master.f2.grid(row=1, column=0, rowspan=1, columnspan=2, sticky=ALL)
        #self.master.l2 = Label(self.master.f2, bg="orange", text="Frame 2")
        #self.master.l2.grid()
        
        self.master.f3 = Frame(master, bg="white")
        self.master.f3.grid(row=0, column=2, rowspan=2, columnspan=3, sticky=ALL)
        self.master.e1 = Entry(self.master.f3)
        self.master.e1.insert(0, "v:\workspace\MoreGUI_Homework\src\sample.txt")
        self.master.e1.pack(side=TOP, fill=BOTH, expand=False, anchor=N)
        self.master.t1 = Text(self.master.f3)
        self.master.t1.config(width=10, height=10)
        self.master.t1.insert(INSERT, "Text loaded here when Open button pushed and an existing file specified.")
        self.master.t1.pack(side=TOP, fill=BOTH, expand=True, anchor=CENTER)
    
        
root = Tk()
app = Application(master=root)
app.mainloop()
