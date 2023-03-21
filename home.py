import tkinter as tk
from tkinter import *
import sys
import subprocess
import threading 
import webbrowser

from PIL import Image, ImageTk
import os 
import tempfile
from tkinter import filedialog
from pyautogui import alert





# from win32com import client
import time

# --- classes ---
# root = tk.Tk()
def doNothing():
    print("ok ok I won't ...")    

class Redirect():

    def __init__(self, widget, autoscroll=True):
        self.window1 = root
        menu = Menu(root)
        self.window1.menu = Menu(root)
        self.window1.config(menu=menu)
        self.subMenu = Menu(menu)
        # self.menu.add_cascade(label="File",menu=subMenu)
        self.window1.title("Virtual Assistant Home")
        self.window1.geometry("1280x800+0+0")
        self.widget = widget
        self.autoscroll = autoscroll

        def save_file():
            types = [("Text Files", "*.text"),
                     ("python Files", "*.py"),
                     ("word files", "*.docx"),
                     ("writer files", "*.odt"),
                     ("All Files", "*.*")]

            file_path =filedialog.asksaveasfilename(title = "Custom save Title", filetypes = types, initialdir=".")   
            data = text.get('1.0',END)

            if file_path !="":

                file_writer = open(file_path, mode = ('w'))
                file_writer.write(data)
                file_writer.close()
                # print(data)

        


        def clear_data():
            text.delete('1.0', END)
        
        def home_data():
            text.delete('1.0', END)

            # obj =  Redirect() 
            
            name=("\n\n\n\n\n\n\n\n\t\t\t\t\t\t Welcome to Ramsey virtual Assistant \n\n\n\n\n\n\t\t\t\t\t" +("."*50) + "\n\n\n\n\n\n\t\t\t\t\t\t\t How can i help you!!")  
            text.insert('insert', name)

        def redo_edit():
            self.text.editable(True)
           

        label =Label (root, bg="gray")
        menu = Menu(root)
        root.config(menu=menu)

        subMenu = Menu(menu)
        menu.add_cascade(label="File",menu=subMenu)
        # menu.place(x=20,y=20)

        subMenu.add_command(label="HOME", command =home_data)
        subMenu.add_separator()
        subMenu.add_command(label="New", command =clear_data)
        subMenu.add_separator()
        subMenu.add_command(label="save", command =save_file)
        subMenu.add_separator()
        subMenu.add_command(label="Exit", command =lambda:redirect_window(self))

        editMenu = Menu(menu)
        menu.add_cascade(label="Edit", menu=editMenu)
        subMenu.add_separator()
        editMenu.add_command(label="Edit ",command=redo_edit)   
       


            
    def write(self, text):
        self.widget.insert('end', text)
        if self.autoscroll:
            self.widget.see("end")  # autoscroll
            
    def flush(self):
        pass

    # --- imports ----
    # --- Alexa import----
def run_home():
    while (1):
        text.delete('1.0', END)
        from main import main, asis,person
        ran_app
        # voice_data = record_audio("Recording.....") # get the voice input
        # print("Done")
        # print("Q:", voice_data)
        # respond(voice_data) # respond


def redirect_window(self):
    
               
    self.window1.destroy() 
    from login_page import LoginP
            # exit()
             
            
    root = Tk()
    obj = LoginP(root)
    root.mainloop()        
        
        






    


def test():
    print("Thread: start")

    p = subprocess.Popen("ping -c 4 stackoverflow.com".split(), stdout=subprocess.PIPE, bufsize=1, text=True)
    while p.poll() is None:
        msg = p.stdout.readline().strip() # read a line from the process output
        if msg:
            print(msg)

    print("Thread: end")

def flush(self):
    pass     

# --- main ---    


root = Tk()

# - Frame with Text and Scrollbar -
def browserChat():
    print("ok ok I won't ...")
    # from app import chatbot, browser_launch
    # browser_launch()
    webbrowser.open('http://127.0.0.1:7860')

def print_command():
        # print_item = tempfile.mktemp('.txt')
        # open(print_item, 'w').write(txt)
        # os.open(print_item, print)
    
    print_item = filedialog.askopenfilename(
    initialdir="/", title="Select file", 
    filetypes=(("Text files", "*.txt"), ("all files", "*.*")))

    if print_item:
        value = open(print_item, 'r+').read()
        # print(value)
        
        if sys.platform == "win32":
            os.startfile(value, 'print')
            print(value)
        alert(text="Print Successful",title="Success",button='ok')
    else:
        alert(text="error printing")






    
    
    

toolbar =Frame (root, bg="grey")

printButt = Button(toolbar, text="Print", command=lambda: print_command())
# printButt = Button(toolbar, text="Print", command=print_command(Text))
printButt.pack(side=RIGHT, padx=2, pady=5)

insertButt = Button(toolbar, text="ChatGPT", command=lambda: browserChat())
insertButt.pack(side=RIGHT, padx=2, pady=5)



toolbar.pack(side=TOP, fill=X) 
                     

                     


frame = tk.Frame(root)
frame.place(x=200, y=100, width=500,height=635, relheight = 1)
frame.pack(expand=True, fill='both')

text = tk.Text(frame)
text.pack(side='left', fill='both', expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

text['yscrollcommand'] = scrollbar.set
scrollbar['command'] = text.yview

old_stdout = sys.stdout    
sys.stdout = Redirect(text)

# - rest -

button = tk.Button(root, text='launch', command=lambda:run_home())
button.pack()

root.mainloop()

# - after close window -

sys.stdout = old_stdout