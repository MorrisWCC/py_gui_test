import tkinter as tk
import menubar_function as mf
import sys
import random

class Gui:
    
    def __init__(self):
        self.start_flag = False
        self.msg_len = 0
        self.win=tk.Tk()
        self.message = tk.StringVar()
        self.message.set('')
        self.vocabularies = []
        self.correct_answer = tk.StringVar()
        self.correct_answer.set('')
        self.user_answer = tk.StringVar()
        self.user_answer.set('')
        self.hint_variable = tk.StringVar()
        self.hint_variable.set('Hint : ')
        self._SetParameters(self.win)

    def _SetParameters(self,win):
        #size title
        win.title("My GRE Trainer")

        # set size 
        win.minsize(1000,450)
        win.maxsize(1400,850)
        win.geometry("1250x450")
        self.center(win)
        #icon
        win.iconbitmap('icon.ico')

        #Label
        label =  tk.Label(win,text="              This is GRE Vocabulary Trainer!",font = "Courier 28")
        label.place(x = 0 , y = 10)

        word_label = tk.Label(win,text="Word :",font ="Courier 20")
        word_label.place(x = 30 , y = 70)

        definition_label = tk.Label(win,text="Definition :",font ="Courier 20")
        definition_label.place(x = 20 , y = 110)
        
        word_def = tk.Label(win , textvariable = self.message , font = 'Courier 20')
        word_def.place( x = 220 ,y = 110 )

        correct_label = tk.Label (win , text = 'Your Answers' , font = 'Courier 18 bold' )
        correct_label.place( x = 100 , y = 190)

        incorrect_label = tk.Label (win , text = 'Correct Answers' , font = 'Courier 18 bold')
        incorrect_label.place( x = 480 , y = 190 )
        
        hint_label = tk.Label (win , textvariable = self.hint_variable , font = 'Courier 18 bold')
        hint_label.place(x = 480,y = 70)
        
        #menu

        #entry 
        input_entry  = tk.Entry(win, font = "28" )
        input_entry.place(x = 170 , y = 80)
        input_entry.focus()
        self.win.bind('<Return>',lambda eff:self._get_user_answer(eff,input_entry))

        #button

        btn = tk.Button(win, text = "Start Test", command = self._loadfile,font = "bold" , width = "10" )
        btn.place(x = 10,y = 0)

        next_btn = tk.Button(win, text = "Next", command = self._change_definition, font = "bold" , width = "4" , height = "1")
        next_btn.place(x = 400,y = 70)

        exit_btn = tk.Button(win , text = 'Exit', command = self._exit, font = 'bold' , width = "4" )
        exit_btn.place( x = 900 , y = 380)

        #show correctness
        
        self.show_user_answer = tk.Label(win , width = '40' , height = '9' , font = '16' , textvariable = self.user_answer)
        self.show_user_answer.place( x = 30 , y = 240)

        self.show_correct_answer = tk.Label(win , fg = 'green' , width = '40' , height = '9' , font = '16' , textvariable = self.correct_answer)
        self.show_correct_answer.place ( x = 410 , y = 240)
    
    def _get_new_win(self):
        tmp_win = tk.Tk()
        tmp_win.geometry("1000x200")
        self.center(tmp_win)
        return tmp_win
        
    def _get_user_answer(self,eff,input_entry):
        if(self.start_flag == False):
            new_win = self._get_new_win()
            start_label = tk.Label (new_win, text = "You haven't load files yet" , font = 'Courier 35 bold' ).pack()           
     
        if(self.answer == input_entry.get()):
            print('hi')
            self.show_user_answer['fg'] = 'green'
        else:
            self.show_user_answer['fg'] = 'red'
        
        self.correct_answer.set(self.answer)
        self.user_answer.set(input_entry.get())
        input_entry.delete(0,'end')
        self._change_definition()

        
    def _change_definition(self):
        
        if(self.start_flag == False):
            new_win = self._get_new_win()
            start_label = tk.Label (new_win, text = "You haven't load files yet" , font = 'Courier 35 bold' ).pack()

        index = random.randint(0,(self.msg_len-1))
        self.message.set(self.vocabularies[index][1])
        self.answer = self.vocabularies[index][0]
        self.hint_variable.set('Hint : '+self.answer[0:2])
    
    def _loadfile(self):
        self.start_flag = True
        with open('gre_word_2.txt') as f:
            for line in f:
                split_data = line.split('\t')
                self.vocabularies.append(split_data)
                self.msg_len += 1
        self._change_definition()
         
    def _exit(self):
        sys.exit(0)
        
    def center(self,toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
    