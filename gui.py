import tkinter as tk




def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
    
win=tk.Tk()

#size title
win.title("My GRE Trainer")

# set size 
win.minsize(1000,450)
win.maxsize(1400,850)
win.geometry("1000x450")
center(win)
#icon
win.iconbitmap('icon.ico')

#Label
label =  tk.Label(win,text="This is GRE Vocabulary Trainer!",font = "Courier 28")
label.pack()

#menu

#button

#input area

#show vocabulary ?

#backend

# execute window
win.mainloop()
