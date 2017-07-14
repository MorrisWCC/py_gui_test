import tkinter as tk
import sys 

count = 0
    
def load_file():
    rtn_data = []
    with open('gre_word_2.txt') as f:
        for line in f:
            split_data = line.split('\t')
            rtn_data.append(split_data)
    f.close()
    return rtn_data
    
def start_trainer():
    data = load_file()
    import gui
    show_definition(data,gui.win)

    
def show_definition(data,toplevel):
    cmp_user_input(data[0][0])
    global count
    count = len(data)
    word_def = tk.Label(toplevel , text = data[0][1] , font = 'Courier 20')
    word_def.place( x = 220 ,y = 110 )
        
def cmp_user_input(string):
    a = 3

def exit():
     sys.exit(0)
            