from tkinter import *
from random import choice
from NGA_MN import MN_darabszam

"""
https://youtu.be/rQ9XMB-0hu0?t=14m33s
"""

window_size_factor = 10
window_width_ratio = 30
window_height_ratio = 50
window_actual_width = window_width_ratio * window_size_factor
window_actual_height = window_height_ratio * window_size_factor
calculated_target = 40 #choice(range(1, 10000))
darab = 0

class PyckApp():
    
    def __init__(self):
        self.root = Tk()
        self.root.title("Pyx")
        self.root.geometry("{}x{}".format(window_actual_width, window_actual_height))
        self.root.resizable(False, False)
        
        frame1 = Frame(self.root, background="green")
        frame2 = Frame(self.root, background="blue")
        
        frame1.grid(row = 0, column = 0)
        frame1.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        frame2.grid(row = 1, column = 0)
        frame2.place(relx=0.7, rely=0.5, anchor=CENTER)
        
        self.target = Label(text="The target is: "+str(calculated_target))
        self.target.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        self.darab = 20 #MN_darabszam(5)
        
        self.gombsorszam = Label(text="The number of buttons is: "+str(self.darab)+".")
        self.gombsorszam.place(relx=0.5, rely=0.15, anchor=CENTER)
        
        self.showing = Button(frame2, text="Testing", command=lambda x: self.answering())
        self.showing.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        self.message = Label(text="")
        self.message.place(relx=0.5, rely=0.9, anchor=CENTER)
        
        self.solution = Label(text="")
        self.solution.place(relx=0.5, rely=0.2, anchor=CENTER)
        
        answer = 0
        if calculated_target % self.darab != 0:
            answer = calculated_target % self.darab
        else:
            answer = self.darab
        
        row = 0
        column = 0
        sorszam = 1
        for i in range(1, self.darab+1):
            print("Mezo: "+str(i) + ". Sorszama: " + str(sorszam) + ".")
            if i == self.darab:
                button = Button(frame1, text=str(i), command=lambda enter=0: self.checking(enter))
            else:
                button = Button(frame1, text=str(i), command=lambda i=i: self.checking(i))

            button.config(height=1, width=2)
            
            if sorszam == 1:
                column = 0
                row = 0
                sorszam += 1
            elif 1 < sorszam <= 12:
                column = sorszam - 1
                row = 0
                sorszam += 1
            elif 12 < sorszam:
                column = sorszam % 13
                row = sorszam // 13
                sorszam += 1
            
            button.grid(row=row, column=column)
        
        self.root.mainloop()
        
    def checking(self, enter):
        if calculated_target % self.darab == enter:
            print("Congrats, Button "+str(enter)+" was the answer.")
            self.message["text"] = "Correct answer!"
        else:
            print("Sorry, Button "+str(enter)+" was not the answer.")
            self.message["text"] = "Sorry, the answer was incorrect."
    
    def answering():
        self.solution["text"] = "The answer is "+str(answer)+"."
    

Pyck = PyckApp()
