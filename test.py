import time
from tkinter import *
root = Tk()
root.title("StopWatch")

#textbox for the screen
screen = Text(root, height = 1, width = 20, bd=10)
screen.grid(row=0, column=0)

#Active variable
global stopwatch_active
stopwatch_active = False
stop_time = 0
stop_minutes = 0


#command for starting the stopwatch
def start_com():
    stop_btn.config(state=NORMAL)
    stopwatch_active = True
    start_btn.config(state=DISABLED)
    global stop_time
    stop_time += 1
    screen.insert(END, stop_time)
    root.after(1000, start_com)




#button for starting the stopwatch
start_btn = Button(root, text = "Start", width = 10, bd = 5, command = start_com)
start_btn.grid(row=1, column=0, sticky=W)

#button for stopping the stopwatch
stop_btn = Button(root, text = "Stop", width = 10, bd = 5)
stop_btn.grid(row=1, column=0, sticky=E)
stop_btn.config(state=DISABLED)