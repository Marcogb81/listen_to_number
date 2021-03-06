from tkinter import *
import tkinter as tk
# import
import pyttsx3
import random
# Info
__dedicated_to__="Elenuchy"
__author__ ="Marco Baturan Garcia"
__date__ ="2018/03/23"
__license__="GNU & SLUC, Open Source"
__collaborators__="Elenuchy, Reset Reboot"
__description__=""" Listen to number.
                It's an Open SOurce software for training
                auditive memory by listening
                of random integers series."""

"""TODO: resolve order matrix"""

class Program:
    # Main class
    def __init__(self):
        # Elements  of main window
        self.master = Tk()
        self.master.title("Listen to number. 2.2") # Title main window.
        # variables of all program
        self.how_many_numbers = 0
        self.entry_number_to_compare = []
        self.lista = []
        self.v = IntVar()
        self.v.set(1)
        self.vlanguage = IntVar()
        self.vlanguage.set(1)
        self.basic = 0
        self.e1 = 0
        self.e2 = 0
        self.lista_I = 0
        self.list_compare = 0
        self.button_clicks = 0
        self.ico_spain = PhotoImage(file="spain.png")
        self.ico_eo = PhotoImage(file="eo.gif")
        self.ico_uk = PhotoImage(file="uk.png")
        
    def random_numbers_list(self):
         """ Generate a list of random integer numbers."""
         self.how_many_numbers = int(self.e1.get())
         if self.how_many_numbers == 0: # control if the entry box is empty
            engine = pyttsx3.init()
            engine.say("The field is empty. Please, enter a digit.")
            engine.runAndWait() # speech advice of empty entry box
         else: # generate list of numbers and store the info
             for i in range(self.how_many_numbers):
                 self.lista.append(random.randint(1, 99))
         self.lista_I = self.lista
         self.how_many_numbers == 0

    def voice(self):
        # generate digital voy from list of numbers =
        if self.v.get() == 1: # manage the speed of voyce
            speed = -100 # slow
        else:
            speed = 200 # fast
                                                    
        self.random_numbers_list() # import function
                                                    
        voice_list = self.lista_I # call variable
        engine = pyttsx3.init()
        engine.setProperty('rate', speed)
        engine.say(voice_list)
        engine.runAndWait()  # speak the numbers
        self.e1.delete(0,'end')
        
    def trasnlations(self):
        if self.vlanguage.get() == 1:
            # english
            self.lbl_enter.configure(text ='Enter number of numbers')
            self.lbl_speed.configure(text='Speed of voice')
            self.r1.configure(text='slow')
            self.r2.configure(text='fast')
            self.btn_intro.configure(text='introduce')
            self.btn_quit.configure(text='quit')
            self.btn_compare.configure(text='compare lists')
            self.btn_say.configure(text='say numbers')
            self.lbl_entry.configure(text='list from entry')
            self.lbl_voice.configure(text='List from voice:')
            self.btn_close.configure(text='Close')
            self.lbl_result.configure(text='introduce the result')
            
        if self.vlanguage.get() == 3:
            # Español
            self.lbl_enter.configure(text ='cuantos numeros')
            self.lbl_speed.configure(text='velocidad de la voz ')
            self.r1.configure(text='lento')
            self.r2.configure(text='rapido')
            self.btn_intro.config(text='Introduzca')
            self.btn_quit.configure(text='salir')
            self.btn_compare.configure(text='comparar listas')
            self.btn_say.configure(text='recitar numeros')
            self.lbl_entry.configure(text='lista introducida')
            self.lbl_voice.configure(text='lista recitada')
            self.btn_close.configure(text='cerrar')
            self.lbl_result.configure(text='Introdizca el resultado')
            
        if self.vlanguage.get() == 2:
            # Esperanto
            self.lbl_enter.configure(text ='kiom da nombroj')
            self.lbl_speed.configure(text='rapido de vocxo')
            self.r2.configure(text='malrapida')
            self.r2.configure(text='rapida')
            self.btn_intro.config(text='eniri')
            self.btn_quit.configure(text='forigi')
            self.btn_compare.configure(text='kompari listojn')
            self.btn_say.configure(text='diru nombroj')
            self.lbl_entry.configure(text='listo enkondukita')
            self.lbl_voice.configure(text='reklamita listo')
            self.btn_close.configure(text='fermu')
            self.lbl_result.configure(text='enui la rizulto')
        
    def compare_voice_list_write_list(self):
        # Compare voice list vs a write list by user
        # And raise a matrix composed by two list
        # And put in red the diference.
        self.window = Toplevel(self.master) # Title second window
        self.window.title('Compare the list:')
        #self.lista.reverse()
        list_voice = self.lista_I
        #self.entry_number_to_compare.reverse()
        list_compare = self.entry_number_to_compare
        self.lbl_voice = Label(self.window, text="List from voice: ")
        self.lbl_voice.grid(row=0, column=0)
        for i in list_voice:
            label_voice = Button(self.window, text=i).grid(row=0, column= i + 1)
        self.lbl_entry=Label(self.window, text="List from entry: ")
        self.lbl_entry.grid(row=1, column=0)
        for ii in list_compare:
            # list for compare
            if ii not in list_voice:
                color ='red'
            else:
                color='light grey'
            label_entry_I = Button(self.window, text=ii ,background=color)
            label_entry_I.grid(row=1, column= ii + 1)
        self.btn_close=Button(self.window, text='Close', command=self.close)
        self.btn_close.grid(row=2, column=0)
        
    def close(self):
        # It's close and destroy the window: COmpare the list
        self.window.destroy() # destroy window
        self.lista.clear() # clear the list
        self.entry_number_to_compare.clear() # clear variable
        
    def introduce(self):
        # read de entry of number of numbers
        # append to list
        # and delete de entry, wait for the next input
        for value in self.e2.get().split():
            self.entry_number_to_compare.append(int(value))
        length_lista=len(self.lista)
        length_entry=len(self.entry_number_to_compare)
        if length_lista == length_entry:
            self.compare_voice_list_write_list()
        else:
            pass
        self.e2.delete(0,'end')
        
    def click(self, event): 
        # self for calll inn everey part, event for call from keyboard
        self.introduce()
        
    def run(self):
        # Labels
        self.lbl_enter = Label(self.master, text="Enter number of numbers: ")
        self.lbl_enter.grid(row=0, column=0) # label one
        self.lbl_speed =Label(self.master, text="Speed of voice: ") #label speed
        self.lbl_speed.grid(row=1, column=0)
        self.lbl_result =Label(self.master, text="Introduce the result: ") #label speed
        self.lbl_result.grid(row=3,column=0)
        # input elements
        self.e1 = Entry(self.master) # entry number of integers
        self.e1.insert(0,self.basic) # Insert value in entry
        self.e2 = Entry(self.master) # Insert values for comparation
        self.e2.insert(0, self.basic) # insert basic value for reset
        self.e2.bind("<Return>", self.click) # bind button return
        self.r1 = Radiobutton(self.master, text="Slow", variable=self.v, value=1) # option of 1,2,3 seconds
        self.r2 = Radiobutton(self.master, text="Fast", variable=self.v, value=2)
        # grid section for input
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=3, column=1)
        self.r1.grid(row=1, column=1)
        self.r2.grid(row=2, column=1)
        # grid section of buttons
        # language
        es=Radiobutton(self.master, image = self.ico_spain,width="16",height="16",variable=self.vlanguage, value=3,command=self.trasnlations).grid(row=5, column=0) # spanish
        eo=Radiobutton(self.master, image = self.ico_eo,width="16",height="16",variable=self.vlanguage, value=2,command=self.trasnlations).grid(row=5, column=1) # esperanto
        en=Radiobutton(self.master, image = self.ico_uk,width="16",height="16",variable=self.vlanguage, value=1,command=self.trasnlations).grid(row=5, column=2) # english
        # controls
        self.btn_intro=Button(self.master, text='Introduce', command=self.introduce) # introduce
        self.btn_intro.grid(row=3, column=2, sticky=E, pady=4)
        self.btn_quit=Button(self.master, text='Quit', command=self.master.quit)# close program
        self.btn_quit.grid(row=4, column=0, sticky=W, pady=4) 
        self.btn_say=Button(self.master, text='Say numbers', command=self.voice)#speak
        self.btn_say.grid(row=4, column=1, sticky=W, pady=4) 
        self.btn_compare=Button(self.master, text='Compare lists', command=self.compare_voice_list_write_list)
        self.btn_compare.grid(row=4, column=2, sticky=W, pady=4)
        self.master.mainloop() # create main window

if __name__=='__main__': # call the main program
    program = Program() # instance class
    program.run() # remember, any terminal function has () for run
